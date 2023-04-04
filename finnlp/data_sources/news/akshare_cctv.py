import pandas as pd
import akshare as ak
from tqdm.notebook import tqdm
from finnlp.data_sources.news._base import News_Downloader


class Akshare_cctv(News_Downloader):

    def __init__(self, args={}):
        pass

    def download_news(self, start_date, end_date, stock="all"):
        self.date_list = pd.date_range(start_date, end_date)
        res = pd.DataFrame()
        for date in tqdm(self.date_list):
            tmp = self.gather_one_day_news(date)
            res = pd.concat([res, tmp])
        self.dataframe = res

    def clean_data(self):
        pass

    def gather_one_day_news(self, date, stock="all", delay=0.1):
        date = self.transfer_standard_date_to_nonstandard(date)
        res = ak.news_cctv(date=date)
        return res

    def transfer_standard_date_to_nonstandard(self, date):
        return date.strftime("%Y%m%d")