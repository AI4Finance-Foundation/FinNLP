from finnlp.data_sources.social_media._base import Social_Media_Downloader

from lxml import etree
import requests
import pandas as pd
import json


class Reddit_Streaming(Social_Media_Downloader):

    def __init__(self, args = {}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_all(self, rounds = 3):
        # Download the first page by url
        base_url = "https://www.reddit.com/r/wallstreetbets/new/"

        res = self._request_get(base_url)
        if res is None:
            raise ConnectionError
        
        # get the info from init page
        html = etree.HTML(res.text)
        init = html.xpath("//*[@id='data']/text()")[0]
        init = json.loads(init[14:][:-1])
        init = init["posts"]["models"]
        tmp_df = pd.DataFrame(init).T.reset_index(drop = True)
        self.dataframe = tmp_df

    