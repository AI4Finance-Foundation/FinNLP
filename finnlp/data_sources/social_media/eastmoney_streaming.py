import warnings
warnings.filterwarnings("ignore")
import requests
from lxml import etree
from tqdm import tqdm
import pandas as pd
import json
import time
from finnlp.data_sources.social_media._base import Social_Media_Downloader

# TODO:
# 1. Contents

class Eastmoney_Streaming(Social_Media_Downloader):
    def __init__(self, args = {}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_stock(self, keyword = "600519", rounds = 3, delay = 0.5):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }
        print('Downloading ...', end =' ')
        for page in range(rounds):
            url = f"https://guba.eastmoney.com/list,{keyword}_{page+1}.html"
            res = requests.get(url=url, headers=headers)
            if res.status_code != 200:
                break

            res = etree.HTML(res.text)
            res = res.xpath("//script")[3].xpath("text()")[0]
            article_list, other_list = res.split('var article_list=')[1].strip(";").split(';    var other_list=')
            article_list = json.loads(article_list)
            tmp = pd.DataFrame(article_list['re'])
            self.dataframe = pd.concat([self.dataframe, tmp])

            print(page, end =' ')
            time.sleep(delay)
        
        self.dataframe = self.dataframe.reset_index(drop= True)


        