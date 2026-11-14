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

REFERENCE_YEAR = 2026


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

            analyzed_gens.append(
                {
                    **gen,
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


def build_database():
    """產出 data/cars_db.json"""
    data_dir = ROOT_DIR / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    output_path = data_dir / "cars_db.json"

    result = compute_analytics(CARS_DATABASE, DATA_SOURCES)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

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

    httpd = socketserver.TCPServer(("127.0.0.1", actual_port), QuietHandler)
    url = f"http://127.0.0.1:{actual_port}/index.html"
    print(f"[SERVER] 本地分析網站已啟動: {url}")
    print("[INFO] 若要關閉伺服器，請直接關閉此視窗或按 Ctrl+C")

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
