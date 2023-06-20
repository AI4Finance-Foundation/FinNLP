import time
import requests
from lxml import etree
from tqdm.notebook import tqdm
import pandas as pd

class Sina_Announcement_Downloader:

    def __init__(self, args = {}):
        pass

    def download(self, stock = "all",max_page = 100):
        page = 0
        df = pd.DataFrame()
        print(f"Getting page: ",end = "")
        while page < max_page:
            print(page, end = " ")
            headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
                'Accept-Encoding':'gzip, deflate, br',}
            url = f"https://vip.stock.finance.sina.com.cn/corp/view/vCB_AllBulletin.php?stockid={stock}&Page={page}"
            response = requests.get(url = url,headers=headers)
            # response.encoding = "GBK"
            # print(response.content.decode('GBK'))
            text = response.content.decode('GBK')
            html = etree.HTML(text)

            # get announcement date
            date_list = html.xpath("/html/body/div[6]/div[2]/div[2]/table[2]/tr/td[2]/div[1]/ul/text()")
            if len(date_list) <= 0:
                break
            date_list = [date.strip('.\r').strip('.\n').strip('.\xa0').strip(' ') for date in date_list]
            date_list = [date for date in date_list if len(date) == 10]


            # get headlines and urls
            url_root = "https://vip.stock.finance.sina.com.cn"
            a_list = html.xpath("/html/body/div[6]/div[2]/div[2]/table[2]/tr/td[2]/div[1]/ul/a")
            headline_list = [a.xpath("./text()")[0] for a in a_list ]
            url_list = [url_root + a.xpath("./@href")[0] for a in a_list ]
            
            tmp_df = {
                "date": date_list,
                "headline": headline_list,
                "url": url_list,
            }
            tmp_df = pd.DataFrame(tmp_df)
            df = pd.concat([df,tmp_df])
            page += 1
        
        
        with tqdm(total = df.shape[0],desc = "Getting Announcement content" ) as pbar:
            df["content"] = df.apply(lambda x: self.get_content(x,pbar), axis=1 )
        
        df = df.reset_index(drop=True)

        return df
        
    def get_content(self,x,pbar,delay = 0.1):
        time.sleep(delay)
        url = x.url
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
                'Accept-Encoding':'gzip, deflate, br',}
        response = requests.get(url = url,headers=headers)
        if response.status_code == 200:
            try:
                text = response.content.decode('GBK')
                html = etree.HTML(text)

                # clean content
                content_list = html.xpath("//*[@id='content']//text()")
                content_list = [content.strip('.\t').strip('.\n').strip('.\r') for content in content_list]
                content_list = [content for content in content_list if len(content) != 0]
                content = "".join(content_list)
            except:
                return "can't get content"
        else:
            return "can't get content"

        pbar.update(1)

        return content

    def clean_data(self):
        pass

    def transfer_standard_date_to_nonstandard(self,date):
        pass