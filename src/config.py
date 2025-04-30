from pathlib import Path
from dotenv import load_dotenv
import os, sys

ROOT = Path(__file__).resolve().parent.parent
ENV = ROOT / ".env"
if ENV.exists():
    load_dotenv(ENV)
else:
    print(".env が見つかりません。SERPAPI_API_KEY を設定してください。", file=sys.stderr)
    sys.exit(1)

SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")
if not SERPAPI_KEY:
    raise RuntimeError("SERPAPI_API_KEY が未設定です。")
