# -*- coding: utf-8 -*-
"""
批次抓取 Wikimedia Commons 車輛實拍圖 -> AI 去背 (rembg) -> 合成純白底圖 (#FFFFFF)
輸出至 assets/cars/<gen_id>.jpg
"""
import io
import json
import time
from pathlib import Path
import requests
from PIL import Image
from rembg import remove, new_session

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "cars_db.json"
OUT_DIR = ROOT / "assets" / "cars"
CREDITS_PATH = OUT_DIR / "credits.json"

HEADERS = {
    "User-Agent": "GEN-UsedCars-Taiwan/1.0 (https://github.com/bossliugen/Used_Cars9918)"
}

def fetch_wikimedia_image(query):
    api_url = (
        "https://commons.wikimedia.org/w/api.php"
        "?action=query&generator=search&gsrnamespace=6"
        f"&gsrsearch={requests.utils.quote(query)}"
        "&gsrlimit=6&prop=imageinfo&iiprop=url|extmetadata&iiurlwidth=640&format=json"
    )
    resp = requests.get(api_url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    pages = list((data.get("query") or {}).get("pages", {}).values())

    valid_png = next(
        (p for p in pages if (p.get("title") or "").lower().endswith(".png") and p.get("imageinfo", [{}])[0].get("thumburl")),
        None,
    )
    valid_jpg = next(
        (
            p
            for p in pages
            if any((p.get("title") or "").lower().endswith(ext) for ext in (".jpg", ".jpeg"))
            and p.get("imageinfo", [{}])[0].get("thumburl")
        ),
        None,
    )
    chosen = valid_png or valid_jpg
    if not chosen:
        return None

    info = chosen["imageinfo"][0]
    return {
        "url": info["thumburl"],
        "license": info.get("extmetadata", {}).get("LicenseShortName", {}).get("value", "CC"),
        "pageUrl": info.get("descriptionurl") or f"https://commons.wikimedia.org/wiki/{chosen['title']}",
    }


def make_white_cutout(img_bytes, session):
    cutout_bytes = remove(img_bytes, session=session)
    fg = Image.open(io.BytesIO(cutout_bytes)).convert("RGBA")

    # 裁切透明邊界讓車體置中放大
    bbox = fg.getbbox()
    if bbox:
        fg = fg.crop(bbox)

    target_w, target_h = 640, 420
    pad = 24
    fg.thumbnail((target_w - pad * 2, target_h - pad * 2), Image.Resampling.LANCZOS)

    canvas = Image.new("RGB", (target_w, target_h), (255, 255, 255))
    x = (target_w - fg.width) // 2
    y = (target_h - fg.height) // 2
    canvas.paste(fg, (x, y), fg)
    return canvas


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    db = json.loads(DB_PATH.read_text(encoding="utf-8"))
    credits = json.loads(CREDITS_PATH.read_text(encoding="utf-8")) if CREDITS_PATH.exists() else {}

    gens = []
    for car in db["cars"]:
        for gen in car["generations"]:
            gens.append((car["brand"], car["model"], gen))

    print(f"總計 {len(gens)} 個世代需要檢查/去背...", flush=True)
    session = new_session("u2net")

    ok_count = 0
    for idx, (brand, model, gen) in enumerate(gens, 1):
        gid = gen["gen_id"]
        out_file = OUT_DIR / f"{gid}.jpg"
        if out_file.exists() and out_file.stat().st_size > 2000:
            ok_count += 1
            continue

        query = gen.get("photo_query") or f"{brand} {model}"
        try:
            meta = fetch_wikimedia_image(query)
            if not meta:
                fallback_q = f"{brand} {model} {gen['years'][0]}" if gen.get("years") else f"{brand} {model}"
                meta = fetch_wikimedia_image(fallback_q)
            if not meta:
                meta = fetch_wikimedia_image(f"{brand} {model}")
            if not meta:
                print(f"[{idx}/{len(gens)}] 找不到圖片: {gid} ({query})", flush=True)
                continue

            img_resp = requests.get(meta["url"], headers=HEADERS, timeout=20)
            img_resp.raise_for_status()
            white_img = make_white_cutout(img_resp.content, session)
            white_img.save(out_file, format="JPEG", quality=88, optimize=True)

            credits[gid] = {
                "license": meta["license"],
                "pageUrl": meta["pageUrl"],
            }
            ok_count += 1
            print(f"[{idx}/{len(gens)}] OK -> {gid}.jpg ({brand} {model})", flush=True)
            time.sleep(0.25)
        except Exception as exc:
            print(f"[{idx}/{len(gens)}] 失敗 {gid}: {exc}", flush=True)

    CREDITS_PATH.write_text(json.dumps(credits, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"完成！共產出 {ok_count}/{len(gens)} 張白底去背車圖。", flush=True)


if __name__ == "__main__":
    main()
