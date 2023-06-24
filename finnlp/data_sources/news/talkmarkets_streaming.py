import warnings
warnings.filterwarnings("ignore")
import requests
from lxml import etree
from tqdm import tqdm
import pandas as pd
import json
import time
from finnlp.data_sources.news._base import News_Downloader

# TODO:
# 1. Contents

class TalkMarkets_Streaming(News_Downloader):
    
    def __init__(self, args={}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_search(self, keyword = "appple", rounds = 3, delay = 0.5):
        # 1. obtain cx
        cx = self._obtain_cx(keyword)

        # 2. obtain ces token
        ces_token = self._obtain_cse_token(cx)

        # 3. get content (Due to limit of the platform, the max rouund is 10, about 100 news)
        print("Downloading...", end = ' ')
        for i in range(rounds):
            url = "https://cse.google.com/cse/element/v1"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
            }
            params = {
                'rsz': 'filtered_cse',
                'num': '20',
                'hl': 'en',
                'source': 'gcsc',
                'gss': '.com',
                'start': i*20,
                'cselibv': '827890a761694e44',
                'cx': cx,
                'q': 'apple',
                'safe': 'off',
                'cse_tok': ces_token,
                'sort': 'date', 
                'exp': 'csqr,cc',
                'callback': 'google.search.cse.api1861',
            }
            res = requests.get(url = url, headers= headers, params = params)
            if res.status_code != 200:
                break

            res = eval(res.text[34:-2])
            tmp = pd.DataFrame(res["results"])
            self.dataframe = pd.concat([self.dataframe, tmp])

            time.sleep(delay)
            print(i, end = ' ')       

    def _obtain_cx(self, keyword):
        url = "https://talkmarkets.com/search"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }
        params = {
            "tab": "General",
            "searchQuery": keyword,
        }
        res = requests.get(url = url, headers= headers, params = params)
        if res.status_code != 200:
            print(f"Connection Error: {res.status_code}")
            return f"Connection Error: {res.status_code}"
        
        res = etree.HTML(res.text)
        cx = res.xpath('.//script[@type="text/javascript"][1]/text()')[1][40:73]
        return cx
    
    def _obtain_cse_token(self, cx, ):
        url = "https://cse.google.com/cse.js"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }
        params = {
            "cx": cx,
        }
        res = requests.get(url = url, headers= headers, params = params)
        if res.status_code != 200:
            print(f"Connection Error: {res.status_code}")
            return f"Connection Error: {res.status_code}"
        
        text = res.text
        ces_token = text[5744:5786]
        return ces_token
        
