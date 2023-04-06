# Natural Language Dataset for Finance

The demos are shown in [FinGPT](https://github.com/AI4Finance-Foundation/ChatGPT-for-FinTech)

**Disclaimer: We are sharing codes for academic purpose under the MIT education license. Nothing herein is financial advice, and NOT a recommendation to trade real money. Please use common sense and always first consult a professional before trading or investing.**

## Ⅰ. How to Use

### 1. News

* US

  ``` python
  from finnlp.data_sources.news.finnhub_date_range import Finnhub_Date_Range
  
  start_date = "2023-01-01"
  end_date = "2023-01-03"
  config = {
      "use_proxy": "us_free",    # use proxies to prvent ip blocking
      "max_retry": 5,
      "proxy_pages": 5,
      "token": "YOUR_FINNHUB_TOKEN"  # Avaliable at https://finnhub.io/dashboard
  }
  
  news_downloader = Finnhub_Date_Range(config)                      # init
  news_downloader.download_date_range_stock(start_date,end_date)    # Download headers
  news_downloader.gather_content()                                  # Download contents
  
  df = news_downloader.dataframe
  selected_columns = ["headline", "content"]
  df[selected_columns].head(10)
  
  --------------------
  
  	headline						content
  0	My 26-Stock $349k Portfolio Gets A Nice Petrob...	Home\nInvesting Strategy\nPortfolio Strategy\n...
  1	Apple’s Market Cap Slides Below $2 Trillion fo...	Error
  2	US STOCKS-Wall St starts the year with a dip; ...	(For a Reuters live blog on U.S., UK and Europ...
  3	Buy 4 January Dogs Of The Dow, Watch 4 More	Home\nDividends\nDividend Quick Picks\nBuy 4 J...
  4	Apple's stock market value falls below $2 tril...	Jan 3 (Reuters) - Apple Inc's \n(AAPL.O)\n sto...
  5	CORRECTED-UPDATE 1-Apple's stock market value ...	Jan 3 (Reuters) - Apple Inc's \n(AAPL.O)\n sto...
  6	Apple Stock Falls Amid Report Of Product Order...	Apple stock got off to a slow start in 2023 as...
  7	US STOCKS-Wall St starts the year with a dip; ...	Summary\nCompanies\nTesla shares plunge on Q4 ...
  8	More than $1 trillion wiped off value of Apple...	apple store\nMore than $1 trillion has been wi...
  9	McLean's Iridium inks agreement to put its sat...	The company hasn't named its partner, but it's...
  ```

  

* China

    ``` python
    # Sina Finance
    from finnlp.data_sources.news.sina_finance_date_range import Sina_Finance_Date_Range
    
    start_date = "2016-01-01"
    end_date = "2016-01-02"
    config = {
        "use_proxy": "china_free",   # use proxies to prvent ip blocking
        "max_retry": 5,
        "proxy_pages": 5,
    }
    
    news_downloader = Sina_Finance_Date_Range(config)                # init
    news_downloader.download_date_range_all(start_date,end_date)	 # Download headers
    news_downloader.gather_content()		                        # Download contents
    
    df = news_downloader.dataframe
    selected_columns = ["title", "content"]
    df[selected_columns].head(10)
    
    --------------------
    
            title	                                 content
    0	分析师：伊朗重回国际原油市场无法阻止	        新浪美股讯 北京时间1月1日晚CNBC称，加拿大皇家银行（RBC）分析师Helima Cro...
    1	FAA：波音767的逃生扶梯存在缺陷	          新浪美股讯 北京时间1日晚，美国联邦航空局（FAA）要求航空公司对波音767机型的救生扶梯进...
    2	非制造业新订单指数创新高 需求回升力度明显	   中新社北京1月1日电 （记者 刘长忠）记者1日从中国物流与采购联合会获悉，在最新发布的201...
    3	雷曼兄弟针对大和证券提起索赔诉讼	          新浪美股讯 北京时间1日下午共同社称，2008年破产的美国金融巨头雷曼兄弟公司的清算法人日前...
    4	国内钢铁PMI有所回升 钢市低迷形势有所改善	   新华社上海1月1日专电（记者李荣）据中物联钢铁物流专业委员会1日发布的指数报告，2015年1...
    5	马息岭凸显朝鲜旅游体育战略	                 新浪美股北京时间1日讯 三位单板滑雪手将成为最早拜访马息岭滑雪场的西方专业运动员，他们本月就...
    6	五洲船舶破产清算 近十年来首现国有船厂倒闭	   （原标题：中国首家国有船厂破产倒闭）\n低迷的中国造船市场，多年来首次出现国有船厂破产清算的...
    7	过半城市房价环比上涨 百城住宅均价加速升温	    资料图。中新社记者 武俊杰 摄\n中新社北京1月1日电 (记者 庞无忌)中国房地产市场在20...
    8	经济学人：巴西病根到底在哪里	              新浪美股北京时间1日讯 原本，巴西人是该高高兴兴迎接2016年的。8月间，里约热内卢将举办南...
    9	中国首家国有船厂破产倒闭:五洲船舶目前已停工	 低迷的中国造船市场，多年来首次出现国有船厂破产清算的一幕。浙江海运集团旗下的五洲船舶修造公司...
    ```

## Ⅱ. Supported Data Sources

### 1. News

|                           Platform                           | Data Type  | Related Market |                         Data Source                          | Specified Company | Range  Type  |      Source Type      |                  Limits                   |
| :----------------------------------------------------------: | :--------: | :------------: | :----------------------------------------------------------: | :---------------: | ---------- | :-------------------: | :---------------------------------------: |
|              [Yahoo]((https://news.yahoo.com/))              |  Financial News   |   US Stocks    |    [Finnhub News](./finnlp/data_sources/news/finnhub.py)     |         √         | Date Range | Third party |         Account-specific （Free）         |
| [Sina](https://news.sina.com.cn/roll/#pageid=153&lid=2516&k=&num=50&page=1) |   Financial News    |   CN Stocks    |  [Sina Finance](./finnlp/data_sources/news/sina_finance.py)  |         ×         | Date Range |   Official     |               Not too much                |
|             [CCTV](http://tv.cctv.com/lm/xwlb/)              | Governemnt News |   CN Stocks    |  [Akshare cctv](./finnlp/data_sources/news/akshare_cctv.py)  |         ×         | Date Range | Third party|                    N/A                    |
|                   US Mainstream Media                   |   Financial News    |   US Stocks    |    [Finnhub News](./finnlp/data_sources/news/finnhub.py)     |         √         | Date Range |       Third party       |         Account-specific （Free）         |
|                   CN Mainstream Media                   |   Financial News    |   CN Stocks    | [Tushare Major News](./finnlp/data_sources/news/tushare_major_news.py) |         ×         | Date Range |       Third party       | Account-specific（About ￥500 per year ） |



### 2. Social Media

|                           Platform                           | Data Type | Related Market |                         Data Source                          | Specified Company |     Range Type     | Source Type | Limits |
| :----------------------------------------------------------: | :-------: | :------------: | :----------------------------------------------------------: | :---------------: | :----------------: | :---------: | :----: |
|              [Twitter](https://www.twitter.com)              |  Tweets   |   US Stocks    | [Twitter Downloader](./finnlp/data_sources/social_media/twitter.py) |         √         |     Date Range     |  Official   |  N/A   |
|              [Twitter](https://www.twitter.com)              | Sentiment |   US Stocks    | [Finnhub Sentiment](./finnlp/data_sources/social_media/finnhub.py) |         √         |     Date Range     | Third Party |  N/A   |
|            [StockTwits](https://stocktwits.com/)             |  Tweets   |   US Stocks    | [Stocktwits Downloader](./finnlp/data_sources/social_media/stocktwits.py) |         √         |      Lastest       |  Official   |  N/A   |
| [Reddit (wallstreetbets)](https://www.reddit.com/r/wallstreetbets/new/) |  Threads  |   US Stocks    | [Reddit Downloader](./finnlp/data_sources/social_media/reddit.py) |         ×         |      Lastest       |  Official   |  N/A   |
|              [Reddit](https://www.reddit.com/)               | Sentiment |   US Stocks    | [Finnhub Sentiment](./finnlp/data_sources/social_media/finnhub.py) |         √         |     Date Range     | Third Party |  N/A   |
|                  [Weibo](https://weibo.com)                  |  Tweets   |   CN Stocks    |           [Weibo Date Range]()/[Weibo Streaming]()           |         √         | Date Range/Lastest |  Official   |  N/A   |

### 3. Company Announcement
|                           Platform                           | Data Type | Related Market |                         Data Source                          | Specified Company | Range Type | Source Type |    Limits    |
| :----------------------------------------------------------: | :-------: | :------------: | :----------------------------------------------------------: | :---------------: | :--------: | :---------: | :----------: |
| [Juchao (Official Website)](http://www.cninfo.com.cn/new/index) |   Text    |   CN Stocks    | [Juchao Annoumcement Downloader](./finnlp/data_sources/company_announcement/juchao.py) |         √         | Date Range |  Official   | Not too much |
|        [SEC (Official Website)](https://www.sec.gov/)        |   Text    |   US Stocks    |                     [SEC Annoumcement]()                     |         √         | Date Range |  Official   | Not too much |
| [Sina](https://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllBulletin/stockid/600519.phtml) |   Text    |   CN Stocks    | [Sina Annoumcement Downloader](./finnlp/data_sources/company_announcement/sina.py) |         √         |  Lastest   | Third Party | Not too much |

### 4. Trends

|                         Platform                          | Data Type | Related Market |                       Data Source                       | Specified Company | Range Type | Source Type | Limits |
| :-------------------------------------------------------: | :-------: | :------------: | :-----------------------------------------------------: | :---------------: | :--------: | :---------: | :----: |
| [Google Trends](https://trends.google.com/trends/explore) |   Index   |   US Stocks    | [Google Trends](./finnlp/data_sources/trends/google.py) |         √         | Date Range |  Official   |  N/A   |
|  [Baidu Index](https://index.baidu.com/v2/index.html#/)   |   Index   |   CN Stocks    |                          Soon                           |         -         |     -      |      -      |   -    |


### 5. Data Sets
  |   Data Source    | Type | Stocks | Dates | Avaliable |
  | :--------------: | :----: | :----: | :-------: | :--------------: |
  | [AShare](https://github.com/JinanZou/Astock)  | News |   3680   |   2018-07-01 to 2021-11-30   |  √  |
  | [stocknet-dataset](https://github.com/yumoxu/stocknet-dataset) | Tweets |   87   |   2014-01-02 to 2015-12-30   |  √  |
  | [CHRNN](https://github.com/wuhuizhe/CHRNN) | Tweets | 38 | 2017-01-03 to 2017-12-28 | √ |

## Ⅲ. Related Large Language Models (LLMs)
* [ChatGPT (GPT 3.5)](https://openai.com/blog/chatgpt)
* [GPT 4.0](https://openai.com/research/gpt-4)
* [ChatGLM](https://github.com/THUDM/ChatGLM-6B)
* [PaLM](https://developers.googleblog.com/2023/03/announcing-palm-api-and-makersuite.html)
* [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/)
* [FinBERT](https://github.com/yya518/FinBERT)
* [Hugging Face](https://huggingface.co/)
