import json
import requests
import pandas as pd
from tqdm.notebook import tqdm

df = pd.read_csv("NAS.csv", index_col=0)
stock_list = df.index.to_list()

api_key = YOUR_API_KEY  # You may find your api key here https://site.financialmodelingprep.com/developer/docs/api-keys

all = pd.DataFrame()
for stock in tqdm(stock_list):
    for page in tqdm(range(500)):
        url = f"https://financialmodelingprep.com/api/v3/stock_news?tickers={stock}&page={page+1}&apikey={api_key}"
        res = requests.get(url)
        res = json.loads(res.text)
        if len(res) == 0:
            break
        else:
            res = pd.DataFrame(res)
            all = pd.concat([all, res])

all = all.reset_index(drop=True)
all.to_csv("dataset_more.csv")