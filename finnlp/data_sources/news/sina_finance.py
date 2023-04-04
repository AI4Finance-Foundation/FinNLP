import json
import pytz
import time
import requests
import pandas as pd
from lxml import etree
from tqdm.notebook import tqdm
from finnlp.data_sources.news._base import News_Downloader


class Sina_Finance(News_Downloader):

    def __init__(self, args={}):
        self.dataframe = pd.DataFrame()

    def download_date_range_all(self, start_date, end_date, stock = None):
        self.date_list = pd.date_range(start_date, end_date)
        res = pd.DataFrame()
        for date in tqdm(self.date_list, desc= "Downloading Titles"):
            tmp = self._gather_one_part_news(date)
            res = pd.concat([res, tmp])
        self.dataframe = res

    def _gather_one_part_news(self, date, stock = None, delay = 0.1):
        end_timestamp = pd.to_datetime(f"{date} 16:00:00").timestamp()
        start_timestamp = end_timestamp - 60 * 60 * 24

        res = pd.DataFrame()
        for page in range(100):
            url = f"https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2516&etime={start_timestamp}&stime={end_timestamp}&ctime={end_timestamp}&date={date}&k=&num=50&page={page}"
            response = requests.get(url=url)
            response.encoding = 'unicode'
            text = response.text
            text = json.loads(text, strict=True)
            text = text["result"]
            text = text["data"]
            if len(text) == 0:
                break

            for i in text:
                for ii in i.keys():
                    i[ii] = [i[ii]]
                tmp = pd.DataFrame(i)
                res = pd.concat([res, tmp])
            time.sleep(delay)

        res.ctime = pd.to_datetime(res.ctime, unit="s", utc=True)
        res.mtime = pd.to_datetime(res.mtime, unit="s", utc=True)
        res.intime = pd.to_datetime(res.intime, unit="s", utc=True)

        tz = pytz.timezone("Asia/Shanghai")
        res.ctime = [t.astimezone(tz) for t in res.ctime]
        res.mtime = [t.astimezone(tz) for t in res.mtime]
        res.intime = [t.astimezone(tz) for t in res.intime]

        return res

    def gather_content(self, delay = 0.01):
        pbar = tqdm(total = self.dataframe.shape[0], desc= "Gathering news contents")
        self.dataframe["content"] = self.dataframe.apply(lambda x:self._gather_content_apply(x, pbar, delay), axis = 1)

    def _gather_content_apply(self,x, pbar, delay = 0.01):
        url = x.url
        response = requests.get(url=url)

        # process
        response.encoding = 'unicode'
        text = response.text
        page = etree.HTML(text)
        page = page.xpath("//*[@id='artibody']/p")
        page = [p.xpath(".//text()") for p in page]
        page = [''.join(p) for p in page]
        content = "\n".join(page)
        content = content.replace("\u3000","")

        # update
        pbar.update(1)
        time.sleep(delay)

        return content
        