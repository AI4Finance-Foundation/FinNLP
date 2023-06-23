import requests
from lxml import etree
from tqdm import tqdm
import pandas as pd
import json
import time
from finnlp.data_sources.news._base import News_Downloader

# TODO:
# 1. More pages
# 2. Contents


class MarketWatch_Streaming(News_Downloader):

    def __init__(self, args={}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_search(self, keyword = "apple", rounds = 3, delay = 0.5):
        # download first page
        self._download_first_page(keyword, delay = delay)
       
        # download the following pages
        # self._download_other_pages(keyword)
        print("Only support the first page now!")

    def download_date_range_search(self, start_date , end_date, keyword = "apple", rounds = 1000, delay = 0.5):
        # download first page
        self._download_first_page(keyword, delay = delay, start_date = start_date, end_date = end_date)
       
        # download the following pages
        # self._download_other_pages(keyword)
        print("Only support the first page now!")

    def _download_first_page(self, keyword = "apple", delay = 0.5, start_date = None, end_date = None):
        url = "https://www.marketwatch.com/search"
        params = {
            'q': keyword,
            'ts': '0',
            'tab': 'All News',
            'sd': start_date,
            'ed': end_date,
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        }

        res = requests.get(url = url, headers= headers, params=params)
        if res.status_code != 200:
            print(f'Connection Error: {res.status_code}')
            return f'Connection Error: {res.status_code}'

        res = etree.HTML(res.text)
        divs = res.xpath("body/main/div/div[2]/div[2]/div[2]/div[2]/mw-tabs/div[2]/div[1]/div/div[1]/div")
        titles = []
        times = []
        authors = []
        for div in divs:
            # title
            title = div.xpath("./div/h3/a/text()")
            # time
            time_ = div.xpath("./div/div/span[1]/text()")
            # author
            author = div.xpath("./div/div/span[2]/text()")

            if len(title)>0:
                titles.append(' '.join(title).replace("\n","").strip(" "))
                times.append(' '.join(time_))
                authors.append(' '.join(author))

        # concat results
        tmp = pd.DataFrame([titles, times, authors]).T
        tmp.columns = ["title", "time", "author"]
        self.dataframe = pd.concat([self.dataframe, tmp])

        # sleep
        time.sleep(delay)




class MarketWatch_Date_Range(News_Downloader):

    def __init__(self, args={}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_date_range_search(self, start_date , end_date, keyword = "apple", delay = 0.5):
        # download first page
        self._download_first_page(keyword, delay = delay, start_date = start_date, end_date = end_date)
       
        # download the following pages
        # self._download_other_pages(keyword)
        print("Only support the first page now!")

    def _download_first_page(self, keyword = "apple", delay = 0.5, start_date = None, end_date = None):
        url = "https://www.marketwatch.com/search"
        params = {
            'q': keyword,
            'ts': '0',
            'tab': 'All News',
            'sd': start_date,
            'ed': end_date,
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        }

        res = requests.get(url = url, headers= headers, params=params)
        if res.status_code != 200:
            print(f'Connection Error: {res.status_code}')
            return f'Connection Error: {res.status_code}'

        res = etree.HTML(res.text)
        divs = res.xpath("body/main/div/div[2]/div[2]/div[2]/div[2]/mw-tabs/div[2]/div[1]/div/div[1]/div")
        titles = []
        times = []
        authors = []
        for div in divs:
            # title
            title = div.xpath("./div/h3/a/text()")
            # time
            time_ = div.xpath("./div/div/span[1]/text()")
            # author
            author = div.xpath("./div/div/span[2]/text()")

            if len(title)>0:
                titles.append(' '.join(title).replace("\n","").strip(" "))
                times.append(' '.join(time_))
                authors.append(' '.join(author))

        # concat results
        tmp = pd.DataFrame([titles, times, authors]).T
        tmp.columns = ["title", "time", "author"]
        self.dataframe = pd.concat([self.dataframe, tmp])

        # sleep
        time.sleep(delay)
    