from finnlp.data_sources.social_media._base import Social_Media_Downloader

import requests
import pandas as pd
from tqdm.notebook import tqdm
import json

class Stocktwits_Downloader(Social_Media_Downloader):

    def __init__(self, args = {}):
        self.dataframe = pd.DataFrame()

    def download_newest(self, stock = "AAPL", rounds = 3):
        url = f"https://api.stocktwits.com/api/2/streams/symbol/{stock}.json"
        headers = {
            'accept': 'application/json',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'OAuth 8a881f43cbc7af061ec2aa35deec9b44f7e3cc09',
            'dnt': '1',
            'origin': 'https://stocktwits.com',
            'referer': 'https://stocktwits.com/',
            
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        }
        for i in tqdm(range(rounds)):
            if i == 0:
                params = { 
                "filter":"top",
                "limit":1000,
                # "max":410000000,
                }
            else:
                params = { 
                "filter":"top",
                "limit":1000,
                "max":max,
                }
            response = requests.get(url = url,headers=headers,params=params)
            if response.status_code != 200:
                print(f"Fetch data fail. Please check your stock name :{stock} and connections. You may raise an issue if you can't solve this problem")
                break
            else:
                res = json.loads(response.text)
                max = res["cursor"]["since"]
                res = pd.DataFrame(res["messages"])
                self.dataframe = pd.concat([self.dataframe,res])
        
        self.dataframe = self.dataframe.reset_index(drop = True)

    def clean_data(self):
        pass

    def gather_one_day_news(self,date,stock = "all",delay = 0.1):
        pass

    def transfer_standard_date_to_nonstandard(self,date):
        pass