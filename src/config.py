from pathlib import Path
from dotenv import load_dotenv
import os, sys

ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
if ENV_PATH.exists():
    load_dotenv(ENV_PATH)
else:
    print(".env が見つかりません。必ず SERPAPI_API_KEY と IMGUR_CLIENT_ID を設定してください。", file=sys.stderr)
    sys.exit(1)

SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")
IMGUR_CLIENT_ID = os.getenv("IMGUR_CLIENT_ID")

if not SERPAPI_KEY or not IMGUR_CLIENT_ID:
    raise RuntimeError("環境変数が不足しています。")
