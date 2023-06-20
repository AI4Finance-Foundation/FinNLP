from finnlp.data_sources.company_announcement._base import Company_Announcement_Downloader

from tqdm import tqdm
from lxml import etree
import pandas as pd
import requests
import json
import time

class SEC_Announcement(Company_Announcement_Downloader):

    def __init__(self, args = {}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()

    def download_date_range_stock(self, start_date, end_date, stock = "AAPL", delay = 0.1):
        entityName = self._get_entity_name(stock)
        # first page
        total_pages = self._gather_one_page(start_date, end_date, 1, entityName, delay)
        # other pages
        if total_pages>1:
            for page in tqdm(range(1, total_pages), desc="Downloading other page..."):
                self._gather_one_page(start_date, end_date, page + 1, entityName, delay )

        self.dataframe = self.dataframe.reset_index(drop = True)
        
    def _get_entity_name(self, stock = "AAPL"):
        url = "https://efts.sec.gov/LATEST/search-index"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        }
        params = {
            "keysTyped":stock
        }
        resp = self._request_get(url = url, headers= headers, params= params)
        if resp is None:
            raise ConnectionError("Can't get entity name")
        
        res = json.loads(resp.text)
        item_list = res["hits"]["hits"]
        entityName_list = []
        for item in item_list:
            c_name_one = item["_source"]["entity_words"]
            c_name_two = item["_id"].zfill(10)
            entityName = f"{c_name_one} (CIK {c_name_two})"
            entityName_list.append(entityName)
        
        entityName = entityName_list[0]

        return entityName
    
    def _gather_one_page(self, start_date, end_date, page, entityName = "Apple Inc. (AAPL) (CIK 0000320193)", delay = 0.01):
        from_ = (page-1)*100
        url = "https://efts.sec.gov/LATEST/search-index"
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        }
        params = {
            "dateRange": "all",
            "entityName": entityName,
            "startdt": start_date,
            "enddt": end_date,
            "from" : from_,
            "page" : page,
        }

        resp = self._request_get(url = url, headers= headers, params= params)
        
        if resp is None:
            return 'Error'
        res = json.loads(resp.text)

        # total
        total_items = res["hits"]["total"]["value"]
        if total_items % 100 == 0:
            total_pages = total_items // 100 
        else:
            total_pages = total_items // 100 + 1

        items = res["hits"]["hits"]

        url_base = "https://www.sec.gov/Archives/edgar/data"

        for item in tqdm(items, desc="Downloading by item..." ):
            url_third = item["_source"]["xsl"]
            url_second, url_fourth = item["_id"].split(":")
            url_second = url_second.split("-")
            url_first = url_second[0]
            url_first = url_first.strip("0")
            url_second = ''.join(url_second)
            url_first, url_second, url_fourth

            if url_third is not None:
                url_new = f"{url_base}/{url_first}/{url_second}/{url_third}/{url_fourth}"
            else:
                url_new = f"{url_base}/{url_first}/{url_second}/{url_fourth}"
            respn = self._request_get(url = url_new, headers= headers)
            if respn is None:
                continue
            try:
                res = etree.HTML(respn.text)
                content = res.xpath("/html/body//text()")
                content = [c for c in content if c != "\n"]
                content = "".join(content)
                
                _id = item["_id"]
                ciks = item["_source"]["ciks"]
                period_ending = item["_source"]["period_ending"]
                root_form = item["_source"]["root_form"]
                file_num = item["_source"]["file_num"]
                display_names = item["_source"]["display_names"]
                xsl = item["_source"]["xsl"]
                sequence = item["_source"]["sequence"]
                file_date = item["_source"]["file_date"]
                biz_states = item["_source"]["biz_states"]
                sics = item["_source"]["sics"]
                form = item["_source"]["form"]
                adsh = item["_source"]["adsh"]
                film_num = item["_source"]["film_num"]
                biz_locations = item["_source"]["biz_locations"]
                file_type = item["_source"]["file_type"]
                file_description = item["_source"]["file_description"]
                inc_states = item["_source"]["inc_states"]
                ite = item["_source"]["items"]

                data = [
                    _id, ciks, period_ending, root_form, file_num, display_names, xsl, sequence,
                    file_date, biz_states, sics, form, adsh, film_num, biz_locations, file_type,
                    file_description, inc_states, ite, content
                ]
                columns = [
                    "_id", "ciks", "period_ending", "root_form", "file_num", "display_names", "xsl", "sequence",
                    "file_date", "biz_states", "sics", "form", "adsh", "film_num", "biz_locations", "file_type",
                    "file_description", "inc_states", "ite", "content"
                ]
                tmp = pd.DataFrame(data = data).T
                tmp.columns = columns

                self.dataframe = pd.concat([self.dataframe, tmp])
                time.sleep(delay)
            except:
                continue
        
        return total_pages
    
