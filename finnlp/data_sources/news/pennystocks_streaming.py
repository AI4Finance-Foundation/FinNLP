import requests
from lxml import etree
from tqdm import tqdm
import pandas as pd
import json
import time as time
from finnlp.data_sources.news._base import News_Downloader

# TODO:
# 1. More Pages
# 2. Contents

class PennyStocks_Streaming(News_Downloader):

    def __init__(self, args={}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_search(self, keyword = "apple", rounds = 3, delay = 2):
        # establish session
        self._connect_session()

        # download first page
        self._download_first_page(keyword, delay = delay)
       
        # download the following pages
        # self._download_other_pages(keyword)
        print("Only support the first page now!")


    def _connect_session(self):
        # since the server will check cookies, we need first 
        # request the main site withour cookies, then finish 
        # searching for the stock information we want.
        self.session = requests.session()
        first_url = "https://pennystocks.com/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        }
        print("Requesting https://pennystocks.com ...", end = " ")
        res = self.session.get(headers = headers, url = first_url)
        if res.status_code !=200:
            raise ConnectionError("Can't request https://pennystocks.com. Please check your connection or report this issue on Github")
        
        print("succeed!")

    def _download_first_page(self, keyword = "apple", max_retry = 5, delay = 2):
        url = f"https://pennystocks.com/?s={keyword}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        }
        res = self.session.get(url = url, headers = headers)
        res = etree.HTML(res.text)
        articles = res.xpath("/html/body/div[3]/div/div[1]/div/div/div/main/div/div[1]/div/article")
        # not sure why but this really works
        
        while max_retry and len(articles) == 0:
            import time
            time.sleep(delay)
            print("Gathering again ..", end = ' ')
            res = requests.get(url = url, headers = headers, cookies=self.session.cookies)
            res = etree.HTML(res.text)
            articles = res.xpath("/html/body/div[3]/div/div[1]/div/div/div/main/div/div[1]/div/article")
            max_retry -= 1
            print(f"Remaining Retry: {max_retry}")


        for a in articles:
            title = a.xpath("./header/h2/a//text()")[0]
            time = a.xpath("./div[3]/div/div/ul/li[1]/text()")[0]
            brief = a.xpath("./div[3]/div/div/text()")[0]
            reading_time = a.xpath("./div[3]/div/div/ul/li[2]/text()")[0]
            columns = ["title", "time", "brief", "reading_time"]
            tmp = pd.DataFrame([[title, time, brief, reading_time]], columns=columns)
            self.dataframe = pd.concat([self.dataframe, tmp])


    def _download_other_pages(self, keyword = "apple"):
        pass


