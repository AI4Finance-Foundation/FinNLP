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
# 2. More pages

class GuruFocus_Streaming(News_Downloader):

    def __init__(self, args={}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_search(self, keyword = "AAPL", rounds = 3, delay = 0.5):
        url = f"https://www.gurufocus.com/stock/{keyword}/article"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }
        res = requests.get(url = url, headers= headers)
        if res.status_code != 200:
            print(f"Connection Error: {res.status_code}")
            return f"Connection Error: {res.status_code}"
        
        res = etree.HTML(res.text)
        divs = res.xpath("/html/body/div[1]/div/section/section/main/div[1]/div[4]/div[1]/div/div")[1:]
        titles = []
        views = []
        sources = []
        datetimes = []
        for div in divs:
            # title
            title = " ".join(div.xpath("./div[1]/h4/a//text()"))
            title = title.replace("\n",  '').strip(" ")
            titles.append(title)

            # summary
            summary = " ".join(div.xpath("div[5]/text()")).replace('\n','').strip(' ')
            view ,source, datetime = summary.split(' \xa0\xa0 ')
            views.append(view)
            sources.append(source)
            datetimes.append(datetime)

        tmp = pd.DataFrame([titles, views, sources, datetimes]).T
        tmp.columns = ["title", "view" ,"source", "datetime"]
        self.dataframe = pd.concat([self.dataframe, tmp])

        print("Only support first page now!")

