import warnings
warnings.filterwarnings("ignore")

import json
import requests
import pandas as pd
from lxml import etree
from tqdm import tqdm
from datetime import datetime

from finnlp.data_sources.news._base import News_Downloader

class SeekingAlpha_Date_Range(News_Downloader):
    def __init__(self, args = {}):
        super().__init__(args)
        
    def download_date_range_stock(self, start_date, end_date, stock = "AAPL", proxies = None):
        self.dataframe = pd.DataFrame()
        start_timestamp = int(datetime.strptime(start_date+'-13', "%Y-%m-%d-%H").timestamp())
        end_timestamp = int(datetime.strptime(end_date+'-13', "%Y-%m-%d-%H").timestamp())
        # Downloading First Page
        data, totalpages = self._gather_by_page(start_timestamp, end_timestamp, stock, 1, proxies)
        self.dataframe = pd.concat([self.dataframe, data])
        
        # Downloading Other Pages
        with tqdm(total=totalpages, desc= "Downloading Titles") as bar:
            bar.update(1)
            for page in range(2, totalpages+1):
                data,_ = self._gather_by_page(start_timestamp, end_timestamp, stock, page, proxies)
                self.dataframe = pd.concat([self.dataframe, data])
                bar.update(1)
        self.dataframe = self.dataframe.reset_index(drop = True)

    def _gather_by_page(self, start_timestamp, end_timestamp, stock, page = 1, proxies = None):
        url = f"https://seekingalpha.com/api/v3/symbols/{stock}/news?filter[since]={start_timestamp}&filter[until]={end_timestamp}&id={stock}&include=author%2CprimaryTickers%2CsecondaryTickers%2Csentiments&isMounting=true&page[size]=40&page[number]={page}"
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
            'Referer':f'https://seekingalpha.com/symbol/aapl/news?from=2009-12-31T16%3A00%3A00.000Z&to=2022-01-01T15%3A59%3A59.999Z'
        }
        response = requests.get(url, headers=headers, proxies=proxies)
        if response.status_code != 200:
            print(f"stock: {stock}, page: {page} went wrong!")
            return pd.DataFrame(), 1
        else:
            res = json.loads(response.text)
            data = pd.DataFrame(res["data"])
            # make new features
            new_columns = ["publishOn", "isLockedPro", "commentCount", "gettyImageUrl", "videoPreviewUrl", "themes", "title", "isPaywalled"]
            data[new_columns] = data.apply(lambda x:list(x.attributes.values()), axis = 1,result_type ="expand" )
            new_columns = ["author", "sentiments", "primaryTickers", "secondaryTickers", "otherTags"]
            data[new_columns] = data.apply(lambda x:list(x.relationships.values()), axis = 1,result_type ="expand" )

            # total pages
            totalpages = res["meta"]["page"]["totalPages"]
            return data, totalpages


