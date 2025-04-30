## セットアップ 

```bash
git clone https://github.com/YuseiSato0302/test_serp_api
cd test_serp_api
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env            
# SERPAPI_API_KEY を書く。SERPAPI_API_KEYは以下のurlから取得。
# https://serpapi.com/
```

## 実行方法

```bash
# 画像 URL をそのまま渡す
python -m src.main {画像URL}
# → test_serp_api.csv が生成
```