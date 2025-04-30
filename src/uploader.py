"""
画像を Imgur に匿名アップロードして公開 URL を返すモジュール
参考: Imgur API /3/image  エンドポイント :contentReference[oaicite:2]{index=2}
"""
import requests
from pathlib import Path
from .config import IMGUR_CLIENT_ID

def upload_to_imgur(path: Path) -> str:
    headers = {"Authorization": f"Client-ID {IMGUR_CLIENT_ID}"}
    with path.open("rb") as fp:
        resp = requests.post("https://api.imgur.com/3/image", headers=headers, files={"image": fp})
    resp.raise_for_status()
    return resp.json()["data"]["link"]
