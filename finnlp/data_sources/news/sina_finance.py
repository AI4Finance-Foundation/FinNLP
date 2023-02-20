import requests
import pandas as pd
import json
import pytz
import time
from tqdm.notebook import tqdm
from finnlp.data_sources.news._base import News_Downloader


class Sina_Finance(News_Downloader):
    def __init__(self,args = {}):
        self.dataframe = pd.DataFrame()

    def download_news(self,start_date,end_date,stock = "all"):
        self.date_list = pd.date_range(start_date,end_date)
        res = pd.DataFrame()
        for date in tqdm(self.date_list):
            tmp = self.gather_one_day_news(date)
            res = pd.concat([res,tmp])
        self.dataframe = res
        
    def gather_one_day_news(self,date,stock = "all",delay = 0.1):
        end_timestamp = pd.to_datetime(f"{date} 16:00:00").timestamp()
        start_timestamp = end_timestamp - 60*60*24
        
        res = pd.DataFrame()
        for page in range(100):
            url = f"https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2516&etime={start_timestamp}&stime={end_timestamp}&ctime={end_timestamp}&date={date}&k=&num=50&page={page}"
            response = requests.get(url = url)
            response = requests.get(url = url)
            response.encoding = 'unicode'   
            text = response.text
            text = json.loads(text, strict=True)
            text = text["result"]
            text = text["data"]
            if len(text)==0:
                break

            for i in text:
                for ii in i.keys():
                    i[ii] = [i[ii]]
                tmp = pd.DataFrame(i)
                res = pd.concat([res,tmp])
            time.sleep(delay)

        res.ctime = pd.to_datetime(res.ctime,unit = "s",utc = True)
        res.mtime = pd.to_datetime(res.mtime,unit = "s",utc = True)
        res.intime = pd.to_datetime(res.intime,unit = "s",utc = True)

        tz = pytz.timezone("Asia/Shanghai")
        res.ctime = [t.astimezone(tz) for t in res.ctime]
        res.mtime = [t.astimezone(tz) for t in res.mtime]
        res.intime = [t.astimezone(tz) for t in res.intime]

        return res
    
    def clean_data(self):
        pass

    def filter_news(self):
        pass