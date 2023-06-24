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

class Yicai_Streaming(News_Downloader):

    def __init__(self, args={}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_search(self, keyword = "茅台", rounds = 3, delay = 0.5):
        url = "https://www.yicai.com/api/ajax/getSearchResult"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'Referer':'https://www.yicai.com/search?keys=%E8%8C%85%E5%8F%B0',
            'X-Requested-With': 'XMLHttpRequest',
        }

        print("Downloading ...", end = ' ')
        for page in range(rounds):
            params = {
                'page': page,
                'pagesize': '20',
                'keys': keyword,
                'type': '0',
            }
            res = requests.get(url = url, headers = headers, params = params)
            if res.status_code != 200:
                break
            res = json.loads(res.text)
            res = res['results']
            tmp = pd.DataFrame(res["docs"])
            self.dataframe = pd.concat([self.dataframe, tmp])

            print(page, end = ' ')

            time.sleep(delay)