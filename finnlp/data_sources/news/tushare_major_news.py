import tushare as ts
import pandas as pd
from tqdm.notebook import tqdm
from finnlp.data_sources.news._base import News_Downloader
import time

class Tushare_Major_News(News_Downloader):

    def __init__(self, args = {}):
        token = args["token"] if "token" in args.keys() else "27080ec403c0218f96f388bca1b1d85329d563c91a43672239619ef5"
        ts.set_token(token)
        self.pro = ts.pro_api()

    def download_news(self, start_date, end_date, stock = "all"):
        self.date_list = pd.date_range(start_date,end_date)
        res = pd.DataFrame()
        for date in tqdm(self.date_list):
            tmp = self.gather_one_day_news(date)
            res = pd.concat([res,tmp])
        self.dataframe = res

    def gather_one_day_news(self,date,stock = "all",delay = 0.1):
        date = self.transfer_standard_date_to_nonstandard(date)
        res = self.pro.major_news(start_date = date,end_date = date)
        time.sleep(delay)
        return res

    def clean_data(self):
        pass

    def transfer_standard_date_to_nonstandard(self,date):
        return date.strftime("%Y-%m0%d 00:00:00")