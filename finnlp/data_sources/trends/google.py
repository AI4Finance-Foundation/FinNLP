from pytrends.request import TrendReq
import pandas as pd

class Google_Trends:
    def __init__(self,args = {}):
        # https://github.com/GeneralMills/pytrends
        self.pytrends = TrendReq(hl='en-US', tz=360)
  
    def download(self, start_date, end_date, stock = 'apple' ):
        self.date_list = pd.date_range(start_date,end_date)
        timeframe = [f"{start_date} {end_date}"]
        kw_list = [stock]
        self.pytrends.build_payload(kw_list=kw_list, timeframe=timeframe)
        res = self.pytrends.interest_over_time()
        # res.columns = ["date","value"]
        return res
