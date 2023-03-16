from finnlp.data_sources.social_media._base import Social_Media_Downloader
from lxml import etree
import requests
import pandas as pd
import json


class Reddit_Downloader(Social_Media_Downloader):

    def __init__(self, args = {}):
        self.dataframe = pd.DataFrame()

    def download_latest(self, pages = 1, stock = "all"):
        # Download the first page by url
        base_url = "https://www.reddit.com/r/wallstreetbets/new/"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        }

        res = requests.get(url = base_url, headers= headers)
        if res.status_code != 200:
            raise ConnectionError
        
        # get the info from init page
        html = etree.HTML(res.text)
        init = html.xpath("//*[@id='data']/text()")[0]
        init = json.loads(init[14:][:-1])
        init = init["posts"]["models"]
        tmp_df = pd.DataFrame(init).T.reset_index(drop = True)
        self.dataframe = tmp_df

    