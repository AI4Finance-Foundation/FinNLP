import requests
from lxml import etree
from tqdm import tqdm
import pandas as pd
import json
import time
from finnlp.data_sources.news._base import News_Downloader

# TODO:
# 1. Contents

class TipRanks_Streaming(News_Downloader):

    def __init__(self, args={}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_search(self, keyword = "apple", rounds = 10000, delay = 0.5):
        url = "https://www.tipranks.com/api/news/posts"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }
        print("Downloading:", end = " ")
        for r in range(rounds):
            params = {
                'page': r,
                'per_page': '50',
                'search': keyword,
            }
            res = requests.get(url = url, headers= headers, params=params)
            if res.status_code != 200:
                break
            try:
                res = json.loads(res.text)
                tmp = pd.DataFrame(res['data'])
                self.dataframe = pd.concat([self.dataframe, tmp])
            except:
                print(res.text)
            # sleep
            time.sleep(delay)
            print(r, end = " ")