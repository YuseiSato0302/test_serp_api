#!/usr/bin/env python3
"""
使い方:
$ python -m src.main path/to/photo.jpg
"""
import argparse, csv, sys
from pathlib import Path
from .uploader import upload_to_imgur
from .lens_search import lens_search
from .filters import extract_links

def main():
    ap = argparse.ArgumentParser(description="Google Lens × SerpApi でフリマ出品リンクを探すツール")
    ap.add_argument("image", type=Path, help="ローカルの画像ファイル")
    ap.add_argument("-o", "--output", default="fleamarket_links.csv", help="CSV 出力先")
    args = ap.parse_args()

    if not args.image.exists():
        ap.error("画像ファイルが見つかりません")

    print("↗️  画像をアップロード中...")
    img_url = upload_to_imgur(args.image)
    print("   →", img_url)

    print("🔍 Google Lens で検索中...")
    results = lens_search(img_url)

    print("🗂 URL を抽出中...")
    links = extract_links(results)
    if not links:
        print("⚠️  フリマサイトのリンクは見つかりませんでした")
        sys.exit(0)

    with open(args.output, "w", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        writer.writerow(["URL"])
        writer.writerows([[l] for l in links])

    print(f"✅ {len(links)} 件のリンクを {args.output} に保存しました")

if __name__ == "__main__":
    main()
