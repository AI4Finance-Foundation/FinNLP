import warnings
warnings.filterwarnings("ignore")
import requests
from lxml import etree
from tqdm import tqdm
import pandas as pd
import json
import time
from finnlp.data_sources.news._base import News_Downloader

# TODO:
# 1. Contents
# 2. More pages

class TheFly_Streaming(News_Downloader):

    def __init__(self, args={}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_search(self, keyword = "AAPL",end_date = None, rounds = 3, delay = 0.5):
        # download first page
        self._download_first_page(keyword, delay = delay, end_date = end_date)
       
        # download the following pages
        # self._download_other_pages(keyword)
        print("Only support the first page now!")

    def _download_first_page(self, keyword = "AAPL", delay = 0.5, end_date = None):
        url = "https://thefly.com/news.php"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }
        params = {
            'fecha': end_date,
            'market_stories': 'on',
            'hot_stocks_filter': 'on',
            'rumors_filter': 'on',
            'general_news_filter': 'on',
            'periodicals_filter': 'on',
            'earnings_filter': 'on',
            'technical_analysis_filter': 'on',
            'options_filter': 'on',
            'syndicates_filter': 'on',
            'onthefly': 'on',
            'insight_filter': 'on',
            'market_mover_filter': 'on',
            'e_inter_filter': 'on',
            'mid_wrap_filter': 'on',
            'sec_wrap_filter': 'on',
            'analyst_wrap_filter': 'on',
            'analyst_recommendations': 'on',
            'upgrade_filter': 'on',
            'downgrade_filter': 'on',
            'initiate_filter': 'on',
            'no_change_filter': 'on',
            'events': 'on',
            'symbol': keyword, 
        }
        res = requests.get(url = url, headers= headers, params = params, verify=False)
        if res.status_code != 200:
            print(f'Connection Error: {res.status_code}')
            return f'Connection Error: {res.status_code}'
        
        res = etree.HTML(res.text)
        tables = res.xpath("/html/body/div[2]/div/div/div[1]/table")[1:]
        titles = []
        stocks = []
        abstracts = []
        dates = []
        times = []
        for table in tables:
            trs = table.xpath("./tr")
            for tr in trs:
                title = tr.xpath("./td[2]/div[1]/a/span//text()")
                if len(title) > 0:
                    titles.append(' '.join(title))
                    stocks.append(' '.join(tr.xpath("./td[2]/div[1]/div/span/text()")))
                    abstracts.append(' '.join(tr.xpath("./td[2]/div[2]/dd/p[1]/text()")))
                    dates.append(' '.join(tr.xpath("./td[2]/div[1]/span[2]/small/span[3]/text()")))
                    times.append(' '.join(tr.xpath("./td[2]/div[1]/span[2]/small/span[3]/div/text()")))

        tmp = pd.DataFrame([titles, stocks, abstracts, dates, times]).T
        tmp.columns = ["title", "stock", "abstract", "date", "time"]
        self.dataframe = pd.concat([self.dataframe, tmp])

        time.sleep(delay)
