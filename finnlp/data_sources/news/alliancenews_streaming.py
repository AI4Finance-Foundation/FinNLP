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

## Download Alliance News from Interactive Investor (https://www.ii.co.uk/news/source/alliance-news)

class AllianceNews_Streaming(News_Downloader):

    def __init__(self, args={}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_search(self, keyword = "appple", rounds = 3, delay = 0.5):
        # download first page
        url = "https://api-prod.ii.co.uk/api/1/content/articles"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'Referer': 'https://www.ii.co.uk/news/source/alliance-news',
            'Ii-Consumer-Type': 'web.public'
        }
        params = {
            'pageSize': '12',
            'source': 'ALLIANCE',
        }
        res = requests.get(url = url, headers= headers, params = params)
        if res.status_code != 200:
            print(f"Connection Error: {res.status_code}")
            return f"Connection Error: {res.status_code}"
        
        res = json.loads(res.text)
        nextId = res["nextId"]
        tmp = pd.DataFrame(res["results"])
        self.dataframe = pd.concat([self.dataframe, tmp])

        # download other pages
        for i in range(rounds-1):
            params["nextId"] = nextId
            res = requests.get(url = url, headers= headers, params = params)
            if res.status_code != 200:
                break
            
            res = json.loads(res.text)
            if "nextId" in res.keys():
                nextId = res["nextId"]
            else:
                break

            tmp = pd.DataFrame(res["results"])
            self.dataframe = pd.concat([self.dataframe, tmp])
