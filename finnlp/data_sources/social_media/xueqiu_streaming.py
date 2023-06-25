import warnings
warnings.filterwarnings("ignore")
import requests
from lxml import etree
from tqdm import tqdm
import pandas as pd
import json
import time
from finnlp.data_sources.social_media._base import Social_Media_Downloader

# TODO:
# 1. Contents

class Xueqiu_Streaming(Social_Media_Downloader):
    def __init__(self, args = {}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_stock(self, keyword = "茅台", rounds = 3, delay = 0.5):
        # first get cookie
        self._get_cookie(keyword = keyword)

        url = "https://xueqiu.com/query/v1/search/status.json"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }
        print("Downloading ...", end = ' ')
        for page in range(rounds):
            params = {
                'sortId': '2',
                'q': keyword,
                'count': '10',
                'page': page,
            }

            res = self.session.get(url = url, headers= headers, params = params)
            if res.status_code != 200:
                break

            res = json.loads(res.text)
            tmp = pd.DataFrame(res["list"])
            self.dataframe = pd.concat([self.dataframe, tmp])

            print(page, end = ' ')

            time.sleep(delay)
        
        self.dataframe["created_at"] = pd.to_datetime(self.dataframe["created_at"], unit = 'ms')
        

    def _get_cookie(self, keyword = "茅台"):
        first_url = "https://xueqiu.com/k"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }
        params = {
            'q': keyword
        }

        self.session = requests.session()

        res = self.session.get(headers = headers, url = first_url, params=params)
        if res.status_code != 200:
            print(f"Connection Error: {res.status_code}")
            return f"Connection Error: {res.status_code}"


