# -*- coding: utf-8 -*-
"""
台灣中古車時價分析引擎 (Python)
功能：
1. 讀取台灣中古車世代規格、通病與行情基準資料庫
2. 計算車商認證價、非第三方/個人自售實價、權威天書收購價、殘值率(%)、車商/自售價差、年均折舊
3. 產出靜態 JSON 資料庫 (data/cars_db.json)，支援直接掛載於 GitHub Pages
4. 可選擇啟動本地端 HTTP 伺服器並自動開啟瀏覽器檢視
"""

import argparse
import http.server
import json
import os
import socket
import socketserver
import sys
import threading
import webbrowser
from datetime import datetime
from pathlib import Path

# 確保能匯入同目錄下的 raw_database
SCRIPT_DIR = Path(__file__).resolve().parent
ROOT_DIR = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from raw_database import CARS_DATABASE, DATA_SOURCES
from raw_database_extra import EXTRA_CARS_DATABASE
from raw_database_catalog import CATALOG_EXTRA_CARS
from raw_database_catalog_part2 import CATALOG_EXTRA_CARS_PART2
from raw_database_catalog_part3 import CATALOG_EXTRA_CARS_PART3, EXTRA_GENS_BY_CAR_ID
from raw_database_taiwan_2000 import TAIWAN_2000_CARS

REFERENCE_YEAR = 2026


def calc_taiwan_annual_tax(cc):
    """依據台灣自用小客車排氣量級距計算年度牌照稅 + 燃料費 (新台幣)"""
    if cc <= 0:
        return 0
    if cc <= 600:
        return 1620 + 2880
    elif cc <= 1200:
        return 4320 + 4320
    elif cc <= 1800:
        return 7120 + 4800
    elif cc <= 2400:
        return 11230 + 6180
    elif cc <= 3000:
        return 15210 + 7200
    elif cc <= 3600:
        return 28220 + 8640
    return 28220 + 9830


def compute_analytics(cars_db, sources):
    """計算各車款、各世代、各年份的殘值率、價差與折舊分析"""
    analyzed_cars = []

    for car in cars_db:
        timeline = []
        analyzed_gens = []

        for gen in car["generations"]:
            gen_points = []
            yearly_prices = gen.get("yearly_prices", {})
            sorted_years = sorted(int(y) for y in yearly_prices.keys())

            for idx, yr in enumerate(sorted_years):
                p = yearly_prices[str(yr)]
                msrp = float(p["msrp"])
                dealer = float(p["dealer"])
                private = float(p["private"])
                book = float(p["book"])

                age = max(1, REFERENCE_YEAR - yr)
                res_dealer = round((dealer / msrp) * 100, 1)
                res_private = round((private / msrp) * 100, 1)
                res_book = round((book / msrp) * 100, 1)
                spread_wan = round(dealer - private, 1)
                spread_pct = round(((dealer - private) / private) * 100, 1) if private > 0 else 0.0
                avg_annual_loss = round((msrp - private) / age, 2)

                is_major_here = bool(
                    gen.get("is_major_change") and yr == gen.get("major_change_year")
                )
                # 若該世代首年即為大改款年份，或該年剛好符合 major_change_year
                if idx == 0 and gen.get("is_major_change") and not any(
                    pt["year"] == yr and pt["is_major_change"] for pt in timeline
                ):
                    is_major_here = True

                point = {
                    "year": yr,
                    "gen_id": gen["gen_id"],
                    "gen_name": gen["gen_name"],
                    "msrp": msrp,
                    "dealer": dealer,
                    "private": private,
                    "book": book,
                    "residual_dealer_pct": res_dealer,
                    "residual_private_pct": res_private,
                    "residual_book_pct": res_book,
                    "dealer_private_spread_wan": spread_wan,
                    "dealer_private_spread_pct": spread_pct,
                    "avg_annual_depreciation_wan": avg_annual_loss,
                    "age_years": age,
                    "is_major_change": is_major_here,
                    "alert_level": gen["depreciation_alert"]["level"],
                }
                gen_points.append(point)
                timeline.append(point)

            # 計算該世代整體平均殘值率
            avg_res_dealer = (
                round(sum(pt["residual_dealer_pct"] for pt in gen_points) / len(gen_points), 1)
                if gen_points
                else 0.0
            )
            avg_res_private = (
                round(sum(pt["residual_private_pct"] for pt in gen_points) / len(gen_points), 1)
                if gen_points
                else 0.0
            )

            trims_with_tax = []
            for t in gen.get("trims", []):
                tax = calc_taiwan_annual_tax(int(t.get("displacement_cc", 1800)))
                trims_with_tax.append({**t, "annual_tax_ntd": tax})

            analyzed_gens.append(
                {
                    **gen,
                    "trims": trims_with_tax,
                    "avg_residual_dealer_pct": avg_res_dealer,
                    "avg_residual_private_pct": avg_res_private,
                    "year_points": gen_points,
                }
            )

        # 依年份排序總時間軸
        timeline.sort(key=lambda x: (x["year"], x["gen_id"]))

        analyzed_cars.append(
            {
                "id": car["id"],
                "brand": car["brand"],
                "model": car["model"],
                "model_zh": car["model_zh"],
                "category": car["category"],
                "summary": car["summary"],
                "generations": analyzed_gens,
                "timeline": timeline,
            }
        )

    return {
        "meta": {
            "title": "台灣中古車時價分析與世代通病資料庫",
            "reference_year": REFERENCE_YEAR,
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "currency": "新台幣 (萬元)",
            "total_models": len(analyzed_cars),
            "total_generations": sum(len(c["generations"]) for c in analyzed_cars),
            "total_year_records": sum(len(c["timeline"]) for c in analyzed_cars),
        },
        "data_sources": sources,
        "cars": analyzed_cars,
    }


def export_photo_specs(analyzed_cars):
    """產出給補圖代理專用的詳細規格表：assets/cars/PHOTO_SPEC.json 與 PHOTO_SPEC.md"""
    cars_dir = ROOT_DIR / "assets" / "cars"
    cars_dir.mkdir(parents=True, exist_ok=True)

    specs = []
    ready_cnt = 0
    needs_cnt = 0

    for car in analyzed_cars:
        for gen in car["generations"]:
            gen_id = gen["gen_id"]
            jpg_path = cars_dir / f"{gen_id}.jpg"
            has_photo = jpg_path.exists() and jpg_path.stat().st_size > 1000
            status = "READY" if has_photo else "NEEDS_PHOTO"
            if has_photo:
                ready_cnt += 1
            else:
                needs_cnt += 1

            ps = gen.get("photo_spec") or {}
            yrs = gen.get("years") or []
            yr_range = f"{yrs[0]}-{yrs[-1]}" if yrs else ""

            specs.append(
                {
                    "gen_id": gen_id,
                    "status": status,
                    "expected_filename": f"assets/cars/{gen_id}.jpg",
                    "brand": car["brand"],
                    "model": car["model"],
                    "gen_name": gen["gen_name"],
                    "years": yr_range,
                    "origin": gen.get("origin", ""),
                    "body_style": ps.get("body_style", car.get("category", "")),
                    "photo_query": gen.get("photo_query", f"{car['brand']} {car['model']} {yr_range}"),
                    "visual_cues": ps.get("visual_cues", gen.get("major_change_note", "")),
                    "target_dimensions": ps.get("dimensions", "640x420"),
                    "background": ps.get("background", "#FFFFFF (純白背景去背，車輛置中占畫面約 80%-85%)"),
                    "angle": ps.get("angle", "前斜側 45 度 (Front 3/4 view)"),
                }
            )

    spec_json = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "summary": {
            "total_slots": len(specs),
            "ready_photos": ready_cnt,
            "needs_photo": needs_cnt,
        },
        "global_requirements": {
            "format": "JPEG (.jpg)",
            "resolution": "640 x 420 px (4:2.625 橫向)",
            "background": "純白背景 (#FFFFFF)，車身完整去背不裁切輪胎或後視鏡，底部可保留極淡自然陰影",
            "angle": "前斜側 45 度角（車頭朝左或朝右皆可），優先挑選台灣市售對應規格外觀",
            "naming": "務必完全符合 expected_filename，即 assets/cars/<gen_id>.jpg",
        },
        "items": specs,
    }

    with open(cars_dir / "PHOTO_SPEC.json", "w", encoding="utf-8") as f:
        json.dump(spec_json, f, ensure_ascii=False, indent=2)

    md_lines = [
        "# 實車去背照片規格清單 (PHOTO_SPEC)",
        "",
        f"- 產生時間：{spec_json['generated_at']}",
        f"- 總車款世代槽位：**{len(specs)}** 張（已完成：**{ready_cnt}** 張 / **待補圖：{needs_cnt}** 張）",
        "- 統一規格：`640 x 420 px` JPG、純白背景 (`#FFFFFF`) 去背、前斜側 45 度角、勿裁切車頭尾。",
        "",
        "## 待補照片清單 (NEEDS_PHOTO)",
        "",
        "| `gen_id` | 品牌 / 車款 / 世代 | 年份 | 關鍵搜尋詞 (`photo_query`) | 必看外觀辨識特徵 (`visual_cues`) | 目標檔名 |",
        "|---|---|---|---|---|---|",
    ]
    for s in specs:
        if s["status"] == "NEEDS_PHOTO":
            cues = str(s["visual_cues"]).replace("|", "/")
            md_lines.append(
                f"| `{s['gen_id']}` | {s['brand']} {s['model']} — {s['gen_name']} | {s['years']} | `{s['photo_query']}` | {cues} | `{s['expected_filename']}` |"
            )

    md_lines.extend(["", "## 已有照片清單 (READY)", "", "| `gen_id` | 品牌 / 車款 / 世代 | 年份 | 檔名 |", "|---|---|---|---|"])
    for s in specs:
        if s["status"] == "READY":
            md_lines.append(
                f"| `{s['gen_id']}` | {s['brand']} {s['model']} — {s['gen_name']} | {s['years']} | `{s['expected_filename']}` |"
            )

    with open(cars_dir / "PHOTO_SPEC.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines) + "\n")

    print(f"[OK] 已輸出補圖規格書: PHOTO_SPEC.json / PHOTO_SPEC.md (總計 {len(specs)} 槽位: 已有 {ready_cnt} / 待補 {needs_cnt})")


def build_database():
    """產出 data/cars_db.json 與 PHOTO_SPEC"""
    data_dir = ROOT_DIR / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    output_path = data_dir / "cars_db.json"

    import copy
    base_cars = copy.deepcopy(CARS_DATABASE + EXTRA_CARS_DATABASE)
    by_id = {c["id"]: c for c in base_cars}
    seen_brand_model = {(c["brand"].lower(), c["model"].lower()) for c in base_cars}

    # 合併既有車系的細分世代
    for cid, extra_gens in EXTRA_GENS_BY_CAR_ID.items():
        if cid in by_id:
            existing_ids = {g["gen_id"] for g in by_id[cid]["generations"]}
            for g in extra_gens:
                if g["gen_id"] not in existing_ids:
                    by_id[cid]["generations"].append(copy.deepcopy(g))
            by_id[cid]["generations"].sort(key=lambda x: x["years"][0] if x.get("years") else 9999)

    for extra_car in CATALOG_EXTRA_CARS + CATALOG_EXTRA_CARS_PART2 + CATALOG_EXTRA_CARS_PART3 + TAIWAN_2000_CARS:
        bm_key = (extra_car["brand"].lower(), extra_car["model"].lower())
        if extra_car["id"] not in by_id and bm_key not in seen_brand_model:
            car_copy = copy.deepcopy(extra_car)
            base_cars.append(car_copy)
            by_id[car_copy["id"]] = car_copy
            seen_brand_model.add(bm_key)

    # 確保同一車款跨世代年份不重疊（較新世代優先），並同步 years 與 yearly_prices
    for car in base_cars:
        gens = car.get("generations", [])
        gens.sort(key=lambda x: (min((int(y) for y in x.get("yearly_prices", {}).keys()), default=9999), x["gen_id"]))
        claimed_years = set()
        for g in reversed(gens):
            yp = g.get("yearly_prices", {})
            for yr in list(yp.keys()):
                if yr in claimed_years:
                    del yp[yr]
                else:
                    claimed_years.add(yr)
            if yp:
                g["years"] = sorted(int(y) for y in yp.keys())
        car["generations"] = [g for g in gens if g.get("yearly_prices")]

    all_cars = base_cars
    result = compute_analytics(all_cars, DATA_SOURCES)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    export_photo_specs(result["cars"])

    print(f"[OK] 已成功計算並輸出資料庫: {output_path}")
    print(
        f"     共 {result['meta']['total_models']} 款車系 / "
        f"{result['meta']['total_generations']} 個獨立世代 / "
        f"{result['meta']['total_year_records']} 筆年份行情紀錄"
    )
    return output_path


def find_free_port(preferred=8000):
    for port in range(preferred, preferred + 20):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    return 0


def serve_website(port=8000):
    os.chdir(ROOT_DIR)
    actual_port = find_free_port(port)

    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            pass

    class ReusableTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    httpd = ReusableTCPServer(("127.0.0.1", actual_port), QuietHandler)
    url = f"http://127.0.0.1:{actual_port}/index.html"
    print(f"[SERVER] 本地分析網站已啟動: {url}", flush=True)
    print("[INFO] 若要關閉伺服器，請直接關閉此視窗或按 Ctrl+C", flush=True)

    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[INFO] 伺服器已停止。")
        httpd.server_close()


def main():
    parser = argparse.ArgumentParser(description="台灣中古車時價分析資料庫產生器與本地伺服器")
    parser.add_argument("--build-only", action="store_true", help="僅重新計算並產出 JSON 資料庫")
    parser.add_argument("--serve", action="store_true", help="產出資料庫並啟動網頁伺服器")
    parser.add_argument("--port", type=int, default=8000, help="伺服器連接埠 (預設 8000)")
    args = parser.parse_args()

    build_database()
    if args.serve or not args.build_only:
        serve_website(args.port)


if __name__ == "__main__":
    main()
