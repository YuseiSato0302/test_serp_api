## セットアップ 

```bash
git clone https://github.com/YuseiSato0302/test_serp_api
cd test_serp_api
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env            
```
.env内に 自身で取得した SERPAPI_API_KEY を上書きする。SERPAPI_API_KEYは以下のurlから取得。
https://serpapi.com/

## プログラムの実行方法

```bash
python -m src.main 'https://example.com/image.jpg?foo=1&bar=2'
```

## 出力されたデータの確認方法
fleamarket_links_YYYYMMDD_HHMMSS.csv が`output_url_csv/` ディレクトリ内に生成

CSV 先頭に以下のメタ情報が入ります（`#` 始まりのコメント行）:

```bash
# command: python -m src.main <URL>
# input_url: <URL>
# 続いて `link` 列に検索結果 URL が並びます。
```