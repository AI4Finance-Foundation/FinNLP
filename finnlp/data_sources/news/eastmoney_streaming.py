import requests
from lxml import etree
from tqdm import tqdm
import pandas as pd
from finnlp.data_sources.news._base import News_Downloader


class Eastmoney_Streaming(News_Downloader):

    def __init__(self, args={}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_streaming_stock(self, stock = "600519", rounds = 3):
        print( "Geting pages: ", end = "")
        if rounds > 0:
            for r in range(rounds):
                br = self._gather_pages(stock, r)
                if br == "break":
                    break
        else:
            r = 1
            error_count = 0
            while 1:
                br = self._gather_pages(stock, r)
                if br == "break":
                    break
                elif br == "Error":
                    error_count +=1
                if error_count>10:
                    print("Connection Error")
                r += 1
        print( f"Get total {r+1} pages.")
        self.dataframe = self.dataframe.reset_index(drop = True)
    
    def _gather_pages(self, stock, page):
        print( page, end = " ")
        url = f"https://guba.eastmoney.com/list,{stock},1,f_{page}.html"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }

        requests.DEFAULT_RETRIES = 5  # 增加重试连接次数
        s = requests.session()
        s.keep_alive = False  # 关闭多余连接
        
        response = self._request_get(url, headers=headers)
        if response.status_code != 200:
            return "Error"
        
        # gather the comtent of the first page
        page = etree.HTML(response.text)
        trs = page.xpath('//*[@id="mainlist"]/div/ul/li[1]/table/tbody/tr')
        have_one = False
        for item in trs:
            have_one = True
            read_amount = item.xpath("./td[1]//text()")[0]
            comments = item.xpath("./td[2]//text()")[0]
            title = item.xpath("./td[3]/div/a//text()")[0]
            content_link = item.xpath("./td[3]/div/a/@href")[0]
            author = item.xpath("./td[4]//text()")[0]
            time = item.xpath("./td[5]//text()")[0]
            tmp = pd.DataFrame([read_amount, comments, title, content_link, author, time]).T
            columns = [ "read amount", "comments", "title", "content link", "author", "create time" ]
            tmp.columns = columns
            self.dataframe = pd.concat([self.dataframe, tmp])
            #print(title)
        if have_one == False:
            return "break"
