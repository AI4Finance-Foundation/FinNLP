from finnlp.data_sources.company_announcement._base import Company_Announcement_Downloader

import requests
import time
import json
import os
import pandas as pd
from tqdm import tqdm
from PyPDF2 import PdfReader

class Juchao_Announcement(Company_Announcement_Downloader):

    def __init__(self, args = {}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_date_range_stock(self,start_date, end_date, stock = "000001",max_page = 100, searchkey= "", get_content = False, save_dir = "./tmp/" , delate_pdf = False):
        self.org_dict = self._get_orgid()

        # download the first page
        res = self._get_open_page(start_date, end_date, stock, 1, searchkey)
        total_pages = res["totalpages"]+1
        
        if res["announcements"] is None:
            print(f"Nothing related to your searchkey({searchkey}) is found, you may try another one or just leave it blank")
        else:
            tmp_df = self._process_data(res)
            self.dataframe = pd.concat([self.dataframe, tmp_df])

            page = 2
            # download other page
            pbar = tqdm(total=total_pages,desc="Downloading by page...")
            
            for _ in range(max_page):
                res = self._get_open_page(start_date, end_date, stock, page, searchkey) 
                if res["announcements"] is None:
                    break
                tmp_df = self._process_data(res)
                self.dataframe = pd.concat([self.dataframe, tmp_df])
                pbar.update(1)
                page += 1
            pbar.update(1)
        # Convert Time
        self.dataframe.announcementTime = self.dataframe.announcementTime.apply(lambda x:time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(x/1000)))
        self.dataframe.announcementTime = pd.to_datetime(self.dataframe.announcementTime)
        
        if get_content:
            pbar = tqdm(total=self.dataframe.shape[0], desc="Getting the text data...")
            self.dataframe[["PDF_path","Content"]] = self.dataframe.apply(lambda x: self._get_pdfs(x,save_dir, delate_pdf, pbar),axis= 1,result_type  = "expand")
        if delate_pdf:
            os.removedirs(save_dir)

        self.dataframe = self.dataframe.reset_index(drop = True)
        
    def _get_open_page(self,start_date,end_date, stock,page, searchkey):
        url = "http://www.cninfo.com.cn/new/hisAnnouncement/query?"
        headers = {
            "Referer": "http://www.cninfo.com.cn/new/commonUrl/pageOfSearch?url=disclosure/list/search&lastPage=index",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        }
        data = {
            "pageNum": page,
            "pageSize": "30",
            "column": "szse",
            "tabName": "fulltext",
            "plate":"", 
            "stock":stock + "," + self.org_dict[stock] ,
            "searchkey": searchkey,
            "secid":"", 
            "category":"", 
            "trade":"", 
            "seDate": f"{start_date}~{end_date}",
            "sortName": "", 
            "sortType": "", 
            "isHLtitle": "true",
            }
        res = requests.post(url = url, headers = headers, data = data)
        if res.status_code != 200:
            raise ConnectionError
        
        res = json.loads(res.text)
        return res
    
    def _process_data(self,res):
        if res is None:
            return res
        else:
            return pd.DataFrame(res["announcements"])

    def _get_pdfs(self,x, save_dir, delate_pdf,pbar):
        os.makedirs(save_dir, exist_ok= True)
        adjunctUrl = x.adjunctUrl
        pdf_base_url = "http://static.cninfo.com.cn/"
        pdf_url = pdf_base_url + adjunctUrl
        responsepdf = self._request_get(pdf_url)
        

        if responsepdf is None:
            pbar.update(1)
            return ("Failed Download","Failed Download")

        else:
            # make preparations
            file_name = x.announcementTitle
            file_name = "".join(file_name.split("<em>"))
            file_name = "".join(file_name.split("</em>"))
            file_name
            file_name = f"{x.secCode}_{x.secName}_{file_name}.pdf"
            file_path = os.path.join(save_dir, file_name)

            # save pdf
            with open(file_path, "wb") as f:
                f.write(responsepdf.content)
            
            # analyze pdf
            with open(file_path, "rb") as filehandle:
                pdf = PdfReader(filehandle)
                text_all = ""
                for page in pdf.pages:
                    text = page.extract_text()
                    text = "".join(text.split("\n"))
                    text_all += text
            pbar.update(1)

            if delate_pdf:
                os.remove(file_path)
                return ("removed", text_all)
            else:
                return (file_path, text_all)          

    def _get_orgid(self):
        org_dict = {}
        org_json = self._request_get("http://www.cninfo.com.cn/new/data/szse_stock.json").json()["stockList"]

        for i in range(len(org_json)):
            org_dict[org_json[i]["code"]] = org_json[i]["orgId"]

        return org_dict