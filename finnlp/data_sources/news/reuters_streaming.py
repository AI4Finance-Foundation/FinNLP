import requests
from lxml import etree
from tqdm import tqdm
import pandas as pd
import json
import time
from finnlp.data_sources.news._base import News_Downloader

# TODO:
# 1. Contents


class Reuters_Streaming(News_Downloader):

    def __init__(self, args={}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_search(self, keyword = "apple", rounds = 3, delay = 0.5):
        news_per_page = 20
        url = "https://www.reuters.com/pf/api/v3/content/fetch/articles-by-search-v2"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "Referer": "https://www.reuters.com/site-search/?query=AAPL&sort=newest&offset=0"
        }

        print( "Geting pages: ", end = "")
        for i in range(rounds):
            offset = i * news_per_page
            params = {
                "query": f'{{"keyword":"{keyword}","offset":{offset},"orderby":"display_date:desc","size":20,"website":"reuters"}}',
                "d": "144",
                "_website": "reuters",
            }
            response = self._request_get(url, headers=headers, params = params)
            
            # check connection error
            if response.status_code != 200:
                return "Error"
            
            # Phrase response
            response = json.loads(response.text)

            # check whether return content
            if response["statusCode"] != 200:
                print("Early Stopping")
                break
            
            # make pandas DataFrame
            tmp = pd.DataFrame(response["result"]["articles"])
            self.dataframe = pd.concat([self.dataframe, tmp])

            # finish
            print( i+1, end = " ")
            time.sleep(delay)
