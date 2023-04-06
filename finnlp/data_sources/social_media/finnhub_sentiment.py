from finnlp.data_sources.social_media._base import Social_Media_Downloader
from tqdm.notebook import tqdm
import pandas as pd
import finnhub
import time

class Finnhub_Sentiment(Social_Media_Downloader):
    def __init__(self, args = {}):
        super().__init__(args)
        assert "token" in args.keys(), "Please input your finnhub token. Avaliable at https://finnhub.io/dashboard"
        self.finnhub_client = finnhub.Client(api_key=args["token"])
        self.delay = args["delay"] if "dalay" in args.keys() else 0.7

    def download_sentiment(self, start_date, end_date, stock = "APPL"):
        self.reddit = pd.DataFrame()
        self.twitter = pd.DataFrame()
        self.date_list = pd.date_range(start_date,end_date)
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
                reddit, _stock_name, twitter = self.gather_one_day_sentiment(tmp_start_date,tmp_end_date,stock = stock )
                self.reddit = pd.concat([self.reddit,reddit])
                self.twitter = pd.concat([self.twitter,twitter])
                bar.update(1)
        self.reddit = self.reddit.sort_values("atTime")
        self.twitter = self.twitter.sort_values("atTime")

    def gather_one_day_sentiment(self,start_date, end_date, stock = "APPL"):
        res  = self.finnhub_client.stock_social_sentiment(stock, _from=start_date, to=end_date)
        reddit = res["reddit"]
        symbol = res["symbol"]
        twitter = res["twitter"]
        reddit = pd.DataFrame(reddit)
        # print(reddit)
        
        twitter = pd.DataFrame(twitter)
        try:
            reddit["atTime"] = pd.to_datetime(reddit["atTime"],errors = "ignore")
            twitter["atTime"] = pd.to_datetime(twitter["atTime"],errors = "ignore")
        except:
            pass
        time.sleep(self.delay)
        return reddit,symbol,twitter
