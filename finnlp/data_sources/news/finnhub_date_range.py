import warnings
warnings.filterwarnings("ignore")

from finnlp.data_sources.news._base import News_Downloader

from tqdm import tqdm
from lxml import etree
import pandas as pd
import requests
import finnhub
import time
import json

class Finnhub_Date_Range(News_Downloader):
    def __init__(self, args = {}):
        super().__init__(args)
        assert "token" in args.keys(), "Please input your finnhub token. Avaliable at https://finnhub.io/dashboard"
        self.finnhub_client = finnhub.Client(api_key=args["token"])

    def download_date_range_stock(self, start_date, end_date, stock = "AAPL"):
        self.date_list = pd.date_range(start_date,end_date)
        self.dataframe = pd.DataFrame()

        days_each_time = 4
        date_list = self.date_list
        # cal total lenth
        if len(date_list)%days_each_time == 0:
            total = len(date_list)//days_each_time
        else:
            total = len(date_list)//days_each_time+1

        with tqdm(total=total, desc= "Downloading Titles") as bar:
            while len(date_list):
                tmp_date_list = date_list[:days_each_time]
                date_list = date_list[days_each_time:]
                tmp_start_date = tmp_date_list[0].strftime("%Y-%m-%d")
                tmp_end_date = tmp_date_list[-1].strftime("%Y-%m-%d")
                res = self._gather_one_part(tmp_start_date,tmp_end_date,stock = stock )
                self.dataframe = pd.concat([self.dataframe,res])
                bar.update(1)

        # res  = self.finnhub_client.company_news(stock, _from=start_date, to=end_date)
        self.dataframe.datetime = pd.to_datetime(self.dataframe.datetime,unit = "s")
        self.dataframe = self.dataframe.reset_index(drop = True)

    def _gather_one_part(self, start_date, end_date, stock = "AAPL", delay = 1):
        res = self.finnhub_client.company_news(stock, _from=start_date, to=end_date)
        time.sleep(delay)
        return pd.DataFrame(res) 
    
    def gather_content(self, delay = 0.01):
        pbar = tqdm(total = self.dataframe.shape[0], desc= "Gathering news contents")
        self.dataframe["content"] = self.dataframe.apply(lambda x:self._gather_content_apply(x, pbar, delay), axis = 1)

    def _gather_content_apply(self,x, pbar, delay = 0.01):
        time.sleep(delay)
        url = x.url
        source = x.source
        response = self._request_get(url = url)
        # response = self._request_get(url= url, headers= headers)
        pbar.update(1)
        if response is None:
            return "Connection Error"
        else:
            page = etree.HTML(response.text)
        
        try:
            # Yahoo Finance
            if source == "Yahoo":
                page = page.xpath("/html/body/div[3]/div[1]/div/main/div[1]/div/div/div/div/article/div/div/div/div/div/div[2]/div[4]")
                content = page[0].xpath(".//text()")
                content = "\n".join(content)
                return content
            
            # Reuters
            elif source == "Reuters":
                page = page.xpath("/html/body/div[1]/div[3]/div/main/article/div[1]/div[2]/div/div/div[2]")
                content = page[0].xpath(".//text()")
                content = "\n".join(content)
                return content
            
            # SeekingAlpha
            elif source == "SeekingAlpha":
                page = page.xpath("/html/body/div[2]/div/div[1]/main/div/div[2]/div/article/div/div/div[2]/div/section[1]/div/div/div")
                content = page[0].xpath(".//text()")
                content = "\n".join(content)
                return content

            # PennyStocks
            elif source == "PennyStocks":
                page = page.xpath("/html/body/div[3]/div/div[1]/div/div/div/main/article/div[2]/div[2]/div")
                content = page[0].xpath(".//text()")
                content = "\n".join(content)
                return content
            
            # MarketWatch
            elif source == "MarketWatch":
                page = page.xpath('//*[@id="js-article__body"]')
                content = page[0].xpath(".//text()")
                content = "".join(content)
                while "  " in content:
                    content = content.replace("  ", " ")
                while "\n \n"in content:
                    content = content.replace("\n \n", " ")
                while "\n  "in content:
                    content = content.replace("\n  ", " ")
                return content
            
            # Seeking Alpha
            elif source == "Seeking Alpha":
                # first get Seeking Alpha URL
                page = page.xpath('/html/body/div[5]/div[2]/section[1]/article[2]/div/div[2]/p/a/@href')
                url_new = page[0]
                response = self._request_get(url= url_new)
                if response is None:
                    return "Connection Error"
                else:
                    page = etree.HTML(response.text)

                content = page[0].xpath(".//text()")
                content = "\n".join(content)
                return content

            # Alliance News
            elif source == "Alliance News":
                page = page.xpath('//*[@id="comtext"]')
                content = page[0].xpath(".//text()")
                content = [c for c in content if not str(c).startswith("\r\n")]
                content = "\n".join(content)
                return content
            
            # Thefly.com
            elif source == "Thefly.com":
                page = page.xpath('/html/body/div[5]/div[2]/section[1]/article[2]/div/div[2]/p/a/@href')
                url_new = page[0]
                response = self._request_get(url= url_new, verify= False)
                if response is None:
                    return "Connection Error"
                else:
                    page = etree.HTML(response.text)

                page = page.xpath('/html/body/div[2]/div/div/div/div/div[2]/div[2]//text()')
                # content = page[0].xpath(".//text()")
                # content = [c for c in content if not str(c).startswith("\r\n")]
                content = "\n".join(page)
                content = content.replace("\r\n","")

                return content
            
            # TalkMarkets
            elif source == "TalkMarkets":
                return "Not supported yet"

            # CNBC
            elif source == "CNBC":
                page = page.xpath('/html/body/div[3]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div[3]//text()')
                content = "\n".join(page)

                return content
            
            # GuruFocus
            elif source == "GuruFocus":
                page = page.xpath('/html/body/div[5]/div[2]/section[1]/article[2]/div/div[2]/p/a/@href')
                url_new = page[0]
                response = self._request_get(url= url_new)
                if response is None:
                    return "Connection Error"
                else:
                    page = etree.HTML(response.text)
                
                page = page.xpath('/html/body/div[1]/div/section/section/main/section/main/div[1]/div/div/div[1]/div[2]/div//text()')
                page_new = []
                for c in page:
                    while "\n"  in c:
                        c = c.replace("\n","")
                    while "  "in c:
                        c = c.replace("  ","")
                    
                    page_new.append(c)

                content = "\n".join(page_new)

                return content
            
            # InvestorPlace
            elif source == "InvestorPlace":
                page = page.xpath('/html/body/div[5]/div[2]/section[1]/article[2]/div/div[2]/p/a/@href')
                url_new = page[0]
                response = self._request_get(url= url_new)
                if response is None:
                    return "Connection Error"
                else:
                    page = etree.HTML(response.text)
                    page = page.xpath('//script[@type="application/ld+json"]')[1]
                    content = page.xpath(".//text()")
                    content = json.loads(content[0])
                    content = content["articleBody"]

                    return content

            # TipRanks
            elif source == "TipRanks":
                page = page.xpath('/html/body/div[5]/div[2]/section[1]/article[2]/div/div[2]/p/a/@href')
                url_new = page[0]
                response = self._request_get(url= url_new)
                if response is None:
                    return "Connection Error"
                else:
                    page = etree.HTML(response.text)
                    # /html/body/div[1]/div[2]/div[5]/div[2]/div[2]/div/div[6]/div/article/p[1]/p
                    page = page.xpath('/html/body/div[1]/div[1]/div[4]/div[2]/div[2]/div[1]/div[6]//text()')
                    # content = page[0].xpath('.//text()')
                    page = [p.replace("\n","") for p in page]
                    content = "".join(page)
                    return content
            
            else:
                return "Not supported yet"
        
        except:
            return "Error"

