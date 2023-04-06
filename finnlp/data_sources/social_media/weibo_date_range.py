from finnlp.data_sources.social_media._base import Social_Media_Downloader

from tqdm import tqdm
from lxml import etree
import pandas as pd
import numpy as np
import requests
import datetime
import time
import json
import re

class Weibo_Date_Range(Social_Media_Downloader):
    def __init__(self, args = {}):
        super().__init__(args)
        if "cookies" not in args.keys():
            raise ValueError("You need first log in at https://weibo.com/ and then copy you cookies and use it as the [value] of [key] \'cookies\' ")
        self.cookies = args["cookies"]
        self.dataframe = pd.DataFrame()

    def download_date_range_stock(self, start_date, end_date, start_hour= 0,end_hour = 0,stock = "茅台", delay = 0.01):
        self.date_list = pd.date_range(start_date, end_date)
        for date in tqdm(self.date_list, desc = "Downloading by dates..."):
            date = date.strftime("%Y-%m-%d")
            self._gather_one_day(date, start_hour, end_hour, stock, delay)
        self.dataframe = self.dataframe.reset_index(drop = True)

    def _gather_one_day(self,date,start_hour, end_hour, stock = "茅台", delay = 0.01):
        if start_hour == 0 and end_hour == 0:
            start_date = datetime.datetime.strptime(date, "%Y-%m-%d")
            end_date = start_date + datetime.timedelta(days=1)
            start_date = start_date.strftime("%Y-%m-%d")
            end_date = end_date.strftime("%Y-%m-%d")
        else:
            start_date = date, end_date = date 

        # first page
        all_urls = self._gather_first_page(start_date, end_date, start_hour, end_hour, stock, delay)
        # another pages
        if len(all_urls)>1:
            base_url=  "https://s.weibo.com/"
            for url_new in all_urls:
                url_new = base_url + url_new
                self._gather_other_pages(date, url_new, delay)
         
    def _gather_first_page(self,start_date, end_date, start_hour, end_hour, stock = "茅台", delay = 0.01):  
        
        headers = {
            "cookie": self.cookies,
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0", 
            }
        
        params = {
            "q": stock,
            "typeall": "1",
            "suball": "1",
            "timescope":f"custom:{start_date}-{start_hour}:{end_date}-{end_hour}",
            "Refer":"g",
            "page":"1"
        }

        url = f"https://s.weibo.com/weibo"
        resp = self._request_get(url, headers=headers, params = params)
        
        if resp is None:
            return "Error"

        if "passport.weibo.com" in resp.url:
            raise ValueError("Your cookies is useless. Please first log in at https://weibo.com/ and then copy you cookies and use it as the [value] of [key] \'cookies\' ")

        res = etree.HTML(resp.content)
        # get all pages
        all_pages = res.xpath('//*[@id="pl_feedlist_index"]/div[3]/div[1]/span/ul/li//@href')
        items = res.xpath('//div[@class="card-wrap"]')
        for i in items:
            ps = i.xpath('.//div[@class="content"]//p')
            try:
                content = ps[0].xpath(".//text()")
                content = ''.join(content)
                content = content.replace('\n',"")
                content = content.replace(' ',"")
                content = content.replace('\u200b',"")
            except:
                continue
            
            info = ps[1].xpath(".//text()")
            try:
                date_content = info[1]
                date_content = date_content.replace('\n',"")
                date_content = date_content.replace(' ',"")
            except:
                date_content = np.nan

            try:
                source = info[3]
            except:
                source = np.nan
            
            tmp = pd.DataFrame([start_date, date_content, source, content]).T
            tmp.columns = ["date","date_content", "source", "content"]
            self.dataframe = pd.concat([self.dataframe, tmp])

        time.sleep(delay)

        return all_pages
    
    def _gather_other_pages(self, date, url, delay = 0.01):
        
        headers = {
            "cookie": self.cookies,
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0", 
            }
        
        resp = self._request_get(url, headers=headers)

        if resp is None:
            return "Error"

        if "passport.weibo.com" in resp.url:
            raise ValueError("Your cookies is useless. Please first log in at https://weibo.com/ and then copy you cookies and use it as the [value] of [key] \'cookies\' ")

        res = etree.HTML(resp.content)
        # get all pages
        all_pages = res.xpath('//*[@id="pl_feedlist_index"]/div[3]/div[1]/span/ul/li//@href')
        items = res.xpath('//div[@class="card-wrap"]')
        for i in items:
            ps = i.xpath('.//div[@class="content"]//p')
            try:
                content = ps[0].xpath(".//text()")
                content = ''.join(content)
                content = content.replace('\n',"")
                content = content.replace(' ',"")
                content = content.replace('\u200b',"")
            except:
                continue
            
            info = ps[1].xpath(".//text()")
            try:
                date_content = info[1]
                date_content = date_content.replace('\n',"")
                date_content = date_content.replace(' ',"")
            except:
                date_content = np.nan

            try:
                source = info[3]
            except:
                source = np.nan
            
            tmp = pd.DataFrame([date, date_content, source, content]).T
            tmp.columns = ["date", "date_content", "source", "content"]
            self.dataframe = pd.concat([self.dataframe, tmp])

        time.sleep(delay)
