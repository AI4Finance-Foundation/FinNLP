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

class InvestorPlace_Streaming(News_Downloader):

    def __init__(self, args={}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_search(self, keyword = "apple", rounds = 3, delay = 0.5):
        url = 'https://investorplace.com/search/'

        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }
        print("Downloading ...", end = ' ')
        for page in range(rounds):
            params = {
                'q': keyword,
                "pg": page,
            }
            res = requests.get(url = url, params=params, headers=headers)
            if res.status_code != 200:
                break

            res = etree.HTML(res.text)
            div_list = res.xpath("/html/body/main/section/div/div/div/div[2]/div[1]/div[1]/div")
            divs = []

            for div in div_list:
                divs += div.xpath("./div")

            titles = []
            times = []
            authors = []
            summaries = []

            for div in divs:
                try:
                    title = div.xpath('./h2/a//text()')[0]
                except:
                    title = ''
                try:
                    time_ = div.xpath('div/time//text()')[0].replace('\n','').replace('\t','')
                except:
                    time_ = ''
                try:
                    author = div.xpath('div/span/a/text()')[0].replace('\n','').replace('\t','')
                except:
                    author = ''
                try:
                    summary = div.xpath('p/text()')[0].replace('\n','').replace('\t','')
                except:
                    summary = ''

                titles.append(title)
                times.append(time_)
                authors.append(author)
                summaries.append(summary)
                
                titles.append(title)

            tmp = pd.DataFrame([titles, times, authors, summaries]).T
            tmp.columns = ['title', 'time', 'author', 'summary']
            self.dataframe = pd.concat([self.dataframe, tmp])

            print(page, end = ' ')

            time.sleep(delay)
