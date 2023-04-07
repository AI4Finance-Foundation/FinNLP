from finnlp.data_sources.social_media._base import Social_Media_Downloader

from tqdm import tqdm
from lxml import etree
import requests
import pandas as pd
import json
import base64

class Reddit_Streaming(Social_Media_Downloader):

    def __init__(self, args = {}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_all(self, rounds = 3):
        # Download the first page by url
        base_url = "https://www.reddit.com/r/wallstreetbets/new/"
        pbar = tqdm(total= rounds, desc= "Downloading by pages...")
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
        init = [i for i in init if len(i)< 12]
        last_id = init[-1]
        last_id = self._encode_base64(last_id)
        
        pbar.update(1)

        # fetch other pages
        if rounds > 1:
            for _ in range(1,rounds):
                last_id = self._fatch_other_pages(last_id, pbar)

    def _fatch_other_pages(self, last_page, pbar):
        url = 'https://gql.reddit.com/'
        headers = {
            "referer":"https://www.reddit.com/",
            "authorization": "Bearer -twjFZkBAlpR8gZnZqsGHvz-G5c49PA",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        }
        data = {
        "id": "02e3b6d0d0d7",
        "variables": {
            "name": "wallstreetbets",
            "includeIdentity": False,
            "adContext": {
            "layout": "CARD",
            "clientSignalSessionData": {
                "adsSeenCount": 4,
                "totalPostsSeenCount": 79,
                "sessionStartTime": "2023-04-07T15:32:13.933Z",
            }
            },
            "isFake": False,
            "includeAppliedFlair": False,
            "includeDevPlatformMetadata": True,
            "includeRecents": False,
            "includeTrending": False,
            "includeSubredditRankings": True,
            "includeSubredditChannels": False,
            "isAdHocMulti": False,
            "isAll": False,
            "isLoggedOutGatedOptedin": False,
            "isLoggedOutQuarantineOptedin": False,
            "isPopular": False,
            "recentPostIds": [],
            "subredditNames": [],
            "sort": "NEW",
            "pageSize": 25,
            "after": last_page
            }
        }
        response = self._request_post(url = url, headers= headers, json = data)
        data = json.loads(response.text)
        data = data["data"]["subredditInfoByName"]["elements"]["edges"]
        for d in data:
            if d["node"]["__typename"] == "SubredditPost":
                tmp = pd.DataFrame(d).T
                self.dataframe = pd.concat([self.dataframe, tmp])
                last_id = tmp.id.values[0]
        
        last_id = self._encode_base64(last_id)
        pbar.update(1)

        return last_id

    def _encode_base64(self,id):
        return base64.b64encode(id.encode('utf-8')).decode()