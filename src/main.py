#!/usr/bin/env python3
"""
Google Lens (SerpApi) を用いたリンク収集 CLI

機能
- 公開画像 URL を渡して Google Lens で検索
- 取得した全リンクを CSV に保存
- ファイル名はデフォルトでタイムスタンプ付き
- CSV 冒頭に実行コマンドと入力 URL をコメントで記録
- 生成された CSV はプロジェクト直下の output_url_csv/ に格納
  （ディレクトリが無ければ自動作成）

使い方例:
    python -m src.main https://example.com/image.jpg
    python -m src.main https://example.com/image.jpg -o result.csv
"""

import argparse
import csv
import sys
from datetime import datetime
from pathlib import Path

from .lens_search import lens_search
from .filters import extract_links


# ------------------------------------------------------------
# ユーティリティ
# ------------------------------------------------------------
def make_default_filename() -> str:
    """タイムスタンプ付き CSV ファイル名を生成"""
    return f"fleamarket_links_{datetime.now():%Y%m%d_%H%M%S}.csv"


def ensure_output_dir() -> Path:
    """
    プロジェクト直下に output_url_csv/ を用意し、その Path を返す
    - 既に存在する場合は何もしない
    """
    root = Path(__file__).resolve().parent.parent
    out_dir = root / "output_url_csv"
    out_dir.mkdir(exist_ok=True)
    return out_dir


# ------------------------------------------------------------
# メイン処理
# ------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Google Lens (SerpApi) で関連リンクを収集し CSV 出力"
    )
    parser.add_argument("url", help="画像の公開 URL")
    parser.add_argument(
        "-o",
        "--output",
        help="CSV 出力ファイル名（省略時はタイムスタンプ付き）",
    )
    args = parser.parse_args()

    # 出力パス決定
    out_dir = ensure_output_dir()
    filename = args.output or make_default_filename()
    output_path = out_dir / filename

    # 実行コマンドを文字列化
    cmd_str = "python " + " ".join(sys.argv)

    # --- SerpApi 呼び出し ---
    print("🔍 Google Lens で検索中…")
    results = lens_search(args.url)

    # --- リンク抽出 ---
    print("🗂 URL を抽出中…")
    links = extract_links(results)
    if not links:
        print("⚠️  リンクが見つかりませんでした")
        sys.exit(0)

    # --- CSV 書き込み ---
    with output_path.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)

        # コメント行でメタデータを記録
        writer.writerow([f"# command: {cmd_str}"])
        writer.writerow([f"# input_url: {args.url}"])
        writer.writerow([])  # 空行

        # 見出し行
        writer.writerow(["link"])
        writer.writerows([[link] for link in links])

    print(f"✅ {len(links)} 件のリンクを {output_path} に保存しました")


if __name__ == "__main__":
    main()
