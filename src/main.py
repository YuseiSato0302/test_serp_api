#!/usr/bin/env python3
"""
使い方:
$ python -m src.main https://example.com/image.jpg
"""
import argparse, csv
from .lens_search import lens_search
from .filters import extract_links

def main() -> None:
    ap = argparse.ArgumentParser(
        description="公開画像 URL を SerpApi Google Lens で検索し、フリマ出品リンクを抽出"
    )
    ap.add_argument("url", help="画像の公開 URL")
    ap.add_argument("-o", "--output", default="fleamarket_links.csv", help="CSV 出力先")
    args = ap.parse_args()

    print("🔍 Google Lens で検索中…")
    results = lens_search(args.url)

    print("🗂 URL を抽出中…")
    links = extract_links(results)

    if not links:
        print("⚠️  フリマサイトのリンクは見つかりませんでした")
        return

    with open(args.output, "w", newline="", encoding="utf-8") as fp:
        csv.writer(fp).writerows([["URL"], *[[l] for l in links]])

    print(f"✅ {len(links)} 件のリンクを {args.output} に保存しました")

if __name__ == "__main__":
    main()
