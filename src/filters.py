"""
Google Lens の検索結果に含まれる “visual_matches” “exact_matches”
および shopping_products ページ（存在する場合）のリンクを
ドメイン制限なしで収集する。

返却値: 重複を除いた URL の昇順リスト
"""
from typing import Iterable, List
from serpapi import GoogleSearch
from .config import SERPAPI_KEY

def _iter_links(block: Iterable[dict]):
    """SerpApi の item ブロックから link を取り出す"""
    for item in block:
        link = item.get("link")
        if link:
            yield link

def extract_links(results: dict) -> List[str]:
    links = set()

    # ① visual / exact matches
    links.update(_iter_links(results.get("visual_matches", [])))
    links.update(_iter_links(results.get("exact_matches", [])))

    # ② さらに products タブ (あれば) を取得
    prod_link = results.get("serpapi_products_link")
    if prod_link:
        prod = GoogleSearch({"api_key": SERPAPI_KEY,
                             "serpapi_link": prod_link}).get_dict()
        links.update(_iter_links(prod.get("shopping_results", [])))

    return sorted(links)
