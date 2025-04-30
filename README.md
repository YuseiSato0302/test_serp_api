## test_serp_api 📸🛍

ローカル画像を投げるだけで **SerpApi Google Lens** を使い、  
メルカリ / ラクマ / ヤフオク など日本のフリマ系サイトに出品されている同一・類似商品の URL を CSV で取得する CLI ツールです。

### 1. セットアップ

```bash
git clone https://github.com/YuseiSato0302/test_serp_api
cd test_serp_api
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# .env を編集して SERPAPI_API_KEY と IMGUR_CLIENT_ID を入れる
