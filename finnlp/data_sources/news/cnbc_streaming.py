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

class CNBC_Streaming(News_Downloader):

    def __init__(self, args={}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_search(self, keyword = "apple", rounds = 3, delay = 0.5):
        url = "https://api.queryly.com/cnbc/json.aspx"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'Referer':'https://www.cnbc.com/',
        }
        print("Downloading ...", end = ' ')
        for page in range(rounds):
            params = {
                'queryly_key': '31a35d40a9a64ab3',
                'query': keyword,
                'endindex': page * 10,
                'batchsize': '10',
                'callback': '',
                'showfaceted': 'false',
                'timezoneoffset': '-480',
                'facetedfields': 'formats',
                'facetedkey': 'formats|',
                'facetedvalue': '!Press Release|',
                'sort': 'date',
                'additionalindexes': '4cd6f71fbf22424d,937d600b0d0d4e23,3bfbe40caee7443e,626fdfcd96444f28',
            }
            res = requests.get(url = url, headers = headers, params = params)
            if res.status_code != 200:
                break
            res = json.loads(res.text)
            tmp = pd.DataFrame(res['results'])
            self.dataframe = pd.concat([self.dataframe, tmp])

            print(page, end = ' ')

            time.sleep(delay)
