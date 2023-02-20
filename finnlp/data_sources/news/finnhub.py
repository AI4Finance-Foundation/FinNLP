from finnlp.data_sources.news._base import News_Downloader
import pandas as pd
import finnhub

class Finnhub_News(News_Downloader):
    def __init__(self, args = {}):
        assert "token" in args.keys(), "Please input your finnhub token. Avaliable at https://finnhub.io/dashboard"
        self.finnhub_client = finnhub.Client(api_key=args["token"])

    def download_news(self, start_date, end_date, stock = "APPL"):
        self.date_list = pd.date_range(start_date,end_date)
        res  = self.finnhub_client.company_news(stock, _from=start_date, to=end_date)
        self.dataframe = pd.DataFrame(res)
        self.dataframe.datetime = pd.to_datetime(self.dataframe.datetime,unit = "s")

    def clean_data(self):
        pass

    def gather_one_day_news(self,date,stock = "all",delay = 0.1):
        pass

    def transfer_standard_date_to_nonstandard(self,date):
        pass