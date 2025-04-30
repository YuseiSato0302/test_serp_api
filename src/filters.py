"""
Google Lens 結果から日本フリマ・オークション系 URL を拾うフィルタ
ドメイン一覧は適宜拡張してください。
"""
import re
from typing import Iterable, List

FLEA_PAT = re.compile(
    r"(mercari\.com|rakuma\.rakuten\.co\.jp|auctions\.yahoo\.co\.jp|paypayfleamarket\.yahoo\.co\.jp)",
    re.I,
)  # :contentReference[oaicite:4]{index=4}

def extract_links(results: dict) -> List[str]:
    def iter_links(block: Iterable[dict]):
        for item in block:
            link = item.get("link")
            if link and FLEA_PAT.search(link):
                yield link

    links = set()
    links.update(iter_links(results.get("visual_matches", [])))
    links.update(iter_links(results.get("exact_matches", [])))

    # SerpApi が products_link を返す場合は追加で取得
    prod_link = results.get("serpapi_products_link")
    if prod_link:
        from serpapi import GoogleSearch
        prod = GoogleSearch({"api_key": SERPAPI_KEY, "serpapi_link": prod_link}).get_dict()
        links.update(iter_links(prod.get("shopping_results", [])))

    return sorted(links)
