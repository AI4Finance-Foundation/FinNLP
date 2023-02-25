from finnlp.data_sources.news._base import News_Downloader
from tqdm.notebook import tqdm
import pandas as pd
import finnhub
import time

class Finnhub_News_xx(News_Downloader):
    def __init__(self, args = {}):
        assert "token" in args.keys(), "Please input your finnhub token. Avaliable at https://finnhub.io/dashboard"
        self.finnhub_client = finnhub.Client(api_key=args["token"])

    def download_news(self, start_date, end_date, stock = "APPL"):
        self.date_list = pd.date_range(start_date,end_date)
        self.dataframe = pd.DataFrame()

        days_each_time = 4
        date_list = self.date_list
        # cal total lenth
        if len(date_list)%days_each_time == 0:
            total = len(date_list)//days_each_time
        else:
            total = len(date_list)//days_each_time+1

        with tqdm(total=total) as bar:
            while len(date_list):
                tmp_date_list = date_list[:days_each_time]
                date_list = date_list[days_each_time:]
                tmp_start_date = tmp_date_list[0].strftime("%Y-%m-%d")
                tmp_end_date = tmp_date_list[-1].strftime("%Y-%m-%d")
                res = self.gather_one_day_news(tmp_start_date,tmp_end_date,stock = stock )
                self.dataframe = pd.concat([self.dataframe,res])
                bar.update(1)

        res  = self.finnhub_client.company_news(stock, _from=start_date, to=end_date)
        
        self.dataframe.datetime = pd.to_datetime(self.dataframe.datetime,unit = "s")

    def clean_data(self):
        pass

    def gather_one_day_news(self,start_date,end_date,stock = "all",delay = 1):
        res = self.finnhub_client.company_news(stock, _from=start_date, to=end_date)
        time.sleep(delay)
        return pd.DataFrame(res) 

    def transfer_standard_date_to_nonstandard(self,date):
        pass