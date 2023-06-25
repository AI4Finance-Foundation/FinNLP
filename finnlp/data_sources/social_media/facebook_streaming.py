import warnings
warnings.filterwarnings("ignore")
import requests
from lxml import etree
from tqdm import tqdm
import pandas as pd
import json
import time
from finnlp.data_sources.social_media._base import Social_Media_Downloader

# TODO:
# 1. Better performance

import json
import time
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.by import By

class Facebook_Streaming(Social_Media_Downloader):
    def __init__(self, args = {}):
        super().__init__(args)
        self.dataframe = pd.DataFrame()
        self.cookies = args["cookies"]
        self.stealth_path = args["stealth_path"]
        self.headless = args["headless"] if "headless" in args.keys() else True

    def download_streaming_stock(self, keyword = "AAPL", rounds = 3, delay = 0.5):
        # init
        self._init_opt()

        # search for the keyword
        search_url = "https://m.facebook.com/search_results/?q=" + keyword
        self.browser.get(search_url)

        # click on the posts
        post_element = self.browser.find_elements(By.XPATH, "/html/body/div[2]/div/div[2]/div[3]/div[1]")[0]
        post_element.click()
        time.sleep(5)

        # click on recent posts
        post_element = self.browser.find_elements(By.XPATH, "/html/body/div[2]/div/div[2]/div[3]/div[1]")[0]
        post_element.click()
        time.sleep(5)
        
        # get data
        all = []
        title_divs = self.browser.find_elements(By.XPATH, "/html/body/div[2]/div/div[2]/div")
        for title_div in tqdm(title_divs):
            # title
            try:
                title = title_div.find_elements(By.XPATH,"./div[2]/div/div/div[2]/div/div/div/div")
                if len(title)>0:
                    title = title[0].text
                else:
                    title = np.nan
            except Exception as e:
                print(e)
                title = np.nan
            
            # time
            try:
                time_element = title_div.find_elements(By.XPATH, './div[2]/div/div/div[1]/div/div/div/div[2]/div[2]/div/span')
                if len(time_element)>0:
                    time_ = time_element[0].text
                else:
                    time_ = np.nan
            except:
                time_ = np.nan
            all.append((title, time_))

        # close browser
        self.browser.close()

        tmp = pd.DataFrame(all, columns=["content", "date"])
        self.dataframe = pd.concat([self.dataframe, tmp])
        self.dataframe = self.dataframe.dropna(how="all")

        print("Only support the first page now!")

    
    def _init_opt(self):
        self.chromeOptions = webdriver.ChromeOptions()
        if self.headless:
            self.chromeOptions.add_argument('--headless')
        self.chromeOptions.add_argument('--disable-blink-features=AutomationControlled')
        self.chromeOptions.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1")

        self.chromeOptions.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.browser = webdriver.Chrome(options=self.chromeOptions)
        with open(self.stealth_path) as f:
            js = f.read()
        self.browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": js
        })
        self.browser.get('https://m.facebook.com/')
        self.browser.delete_all_cookies()
        for i in self.cookies: 
            self.browser.add_cookie(i)

        self.browser.implicitly_wait(2)

