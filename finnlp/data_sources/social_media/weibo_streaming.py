from finnlp.data_sources.social_media._base import Social_Media_Downloader

from tqdm import tqdm
from lxml import etree
import pandas as pd
import requests
import time
import json
import re

class Weibo_Streaming(Social_Media_Downloader):
    def __init__(self, args = {}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_stock(self, stock = "茅台", rounds = 3):
        for r in tqdm(range(rounds), desc="Downloading by page.."):
            page = r+1
            self._gather_one_page(page, stock)

    def _gather_one_page(self,page, stock = "茅台", delay = 0.01):
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0"
            }
        params = {
            "containerid": f"100103type=61&q={stock}&t=",
            "page_type": "searchall",
            "page":page
        }
        url = f"https://m.weibo.cn/api/container/getIndex"
        resp = self._request_get(url, headers=headers, params = params)

        if resp is None:
            return "Error"
        
        res = json.loads(resp.text)
        res = res["data"]["cards"]
        res = pd.DataFrame(res)

        pbar = tqdm(total = res.shape[0], desc = "Processing the text content and downloading the full passage...")
        res[["content_short","content"]] = res.apply(lambda x:self._process_text(x, pbar, delay), axis= 1, result_type= "expand")

        self.dataframe = pd.concat([self.dataframe, res]) 
    
    def _process_text(self,x, pbar, delay = 0.01):
        text = x["mblog"]["text"]
        text = etree.HTML(text)
        content_short = text.xpath(".//text()")
        content_short = ''.join(content_short)
        
        link = text.xpath('.//a/@href')
        link = [l for l in link if "status" in l ]
        if len(link) >0:
            base_url = "https://m.weibo.cn/"
            url_new = base_url + link[0]
            headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0"
            }
            resp = self._request_get(url_new, headers= headers) 
            if resp is None:
                content = content_short
            else:
                res = etree.HTML(resp.content)
                scripts = res.xpath('//script')
                content = scripts[2].xpath("text()")
                pattern=re.compile('"text": "(.+),\n')
                result = pattern.findall(content[0])
                content = etree.HTML(result[0])
                content = content.xpath("//text()")
                content = ''.join(content)
        else:
            content = content_short

        pbar.update(1)
        time.sleep(delay)

        return content_short, content

