"""
SerpApi Google Lens API で画像検索し、JSON を返す
API パラメータ: engine=google_lens, url, api_key, hl, country :contentReference[oaicite:3]{index=3}
"""
from serpapi import GoogleSearch
from .config import SERPAPI_KEY

def lens_search(image_url: str, *, lang: str = "ja", country: str = "jp") -> dict:
    params = {
        "engine": "google_lens",
        "api_key": SERPAPI_KEY,
        "url": image_url,
        "hl": lang,
        "country": country,
        "no_cache": "true",
    }
    return GoogleSearch(params).get_dict()
