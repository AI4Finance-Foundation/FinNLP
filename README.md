# Internet-scale Financial Data

The demos are shown in [FinGPT](https://github.com/AI4Finance-Foundation/ChatGPT-for-FinTech)

[FinNLP Website](https://ai4finance-foundation.github.io/FinNLP/) 

**Disclaimer: We are sharing codes for academic purposes under the MIT education license. Nothing herein is financial advice, and NOT a recommendation to trade real money. Please use common sense and always first consult a professional before trading or investing.**

## Ⅰ. How to Use

### 1. News

* US

  ``` python
  # Finnhub (Yahoo Finance, Reuters, SeekingAlpha, CNBC...)
  from finnlp.data_sources.news.finnhub_date_range import Finnhub_Date_Range
  
  start_date = "2023-01-01"
  end_date = "2023-01-03"
  config = {
      "use_proxy": "us_free",    # use proxies to prvent ip blocking
      "max_retry": 5,
      "proxy_pages": 5,
      "token": "YOUR_FINNHUB_TOKEN"  # Available at https://finnhub.io/dashboard
  }
  
  news_downloader = Finnhub_Date_Range(config)                      # init
  news_downloader.download_date_range_stock(start_date,end_date)    # Download headers
  news_downloader.gather_content()                                  # Download contents
  df = news_downloader.dataframe
  selected_columns = ["headline", "content"]
  df[selected_columns].head(10)
  
  --------------------
  
  # 	headline						content
  # 0	My 26-Stock $349k Portfolio Gets A Nice Petrob...	Home\nInvesting Strategy\nPortfolio Strategy\n...
  # 1	Apple’s Market Cap Slides Below $2 Trillion fo...	Error
  # 2	US STOCKS-Wall St starts the year with a dip; ...	(For a Reuters live blog on U.S., UK and Europ...
  # 3	Buy 4 January Dogs Of The Dow, Watch 4 More	Home\nDividends\nDividend Quick Picks\nBuy 4 J...
  # 4	Apple's stock market value falls below $2 tril...	Jan 3 (Reuters) - Apple Inc's \n(AAPL.O)\n sto...
  # 5	CORRECTED-UPDATE 1-Apple's stock market value ...	Jan 3 (Reuters) - Apple Inc's \n(AAPL.O)\n sto...
  # 6	Apple Stock Falls Amid Report Of Product Order...	Apple stock got off to a slow start in 2023 as...
  # 7	US STOCKS-Wall St starts the year with a dip; ...	Summary\nCompanies\nTesla shares plunge on Q4 ...
  # 8	More than $1 trillion wiped off value of Apple...	apple store\nMore than $1 trillion has been wi...
  # 9	McLean's Iridium inks agreement to put its sat...	The company hasn't named its partner, but it's...
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
    
    #         title	                                 content
    # 0	分析师：伊朗重回国际原油市场无法阻止	        新浪美股讯 北京时间1月1日晚CNBC称，加拿大皇家银行（RBC）分析师Helima Cro...
    # 1	FAA：波音767的逃生扶梯存在缺陷	          新浪美股讯 北京时间1日晚，美国联邦航空局（FAA）要求航空公司对波音767机型的救生扶梯进...
    # 2	非制造业新订单指数创新高 需求回升力度明显	   中新社北京1月1日电 （记者 刘长忠）记者1日从中国物流与采购联合会获悉，在最新发布的201...
    # 3	雷曼兄弟针对大和证券提起索赔诉讼	          新浪美股讯 北京时间1日下午共同社称，2008年破产的美国金融巨头雷曼兄弟公司的清算法人日前...
    # 4	国内钢铁PMI有所回升 钢市低迷形势有所改善	   新华社上海1月1日专电（记者李荣）据中物联钢铁物流专业委员会1日发布的指数报告，2015年1...
    # 5	马息岭凸显朝鲜旅游体育战略	                 新浪美股北京时间1日讯 三位单板滑雪手将成为最早拜访马息岭滑雪场的西方专业运动员，他们本月就...
    # 6	五洲船舶破产清算 近十年来首现国有船厂倒闭	   （原标题：中国首家国有船厂破产倒闭）\n低迷的中国造船市场，多年来首次出现国有船厂破产清算的...
    # 7	过半城市房价环比上涨 百城住宅均价加速升温	    资料图。中新社记者 武俊杰 摄\n中新社北京1月1日电 (记者 庞无忌)中国房地产市场在20...
    # 8	经济学人：巴西病根到底在哪里	              新浪美股北京时间1日讯 原本，巴西人是该高高兴兴迎接2016年的。8月间，里约热内卢将举办南...
    # 9	中国首家国有船厂破产倒闭:五洲船舶目前已停工	 低迷的中国造船市场，多年来首次出现国有船厂破产清算的一幕。浙江海运集团旗下的五洲船舶修造公司...
    
    # Easymoney
    from finnlp.data_sources.news.eastmoney_streaming import Eastmoney_Streaming
    
    pages = 3
    stock = "600519"
    config = {
        "use_proxy": "china_free",
        "max_retry": 5,
        "proxy_pages": 5,
    }
    
	news_downloader = Eastmoney_Streaming(config)
	news_downloader.download_streaming_stock(stock,pages)
	df = news_downloader.dataframe
	selected_columns = ["title", "create time"]
    df[selected_columns].head(10)
    
    --------------------
    
    #     title	create time
    # 0	茅台2022年报的12个小秘密	04-09 19:40
    # 1	东北证券维持贵州茅台买入评级 预计2023年净利润同比	04-09 11:24
    # 2	贵州茅台：融资余额169.34亿元，创近一年新低（04-07	04-08 07:30
    # 3	贵州茅台：融资净买入1248.48万元，融资余额169.79亿	04-07 07:28
    # 4	贵州茅台公益基金会正式成立	04-06 12:29
    # 5	贵州茅台04月04日获沪股通增持19.55万股	04-05 07:48
    # 6	贵州茅台：融资余额169.66亿元，创近一年新低（04-04	04-05 07:30
    # 7	4月4日北向资金最新动向（附十大成交股）	04-04 18:48
    # 8	大宗交易：贵州茅台成交235.9万元，成交价1814.59元（	04-04 17:21
    # 9	第一上海证券维持贵州茅台买入评级 目标价2428.8元	04-04 09:30
    ```

### 2. Social Media

* US

  ``` python
  # Stocktwits
  from finnlp.data_sources.social_media.stocktwits_streaming import Stocktwits_Streaming
  
  pages = 3
  stock = "AAPL"
  config = {
      "use_proxy": "us_free",
      "max_retry": 5,
      "proxy_pages": 2,
  }
  
  downloader = Stocktwits_Streaming(config)
  downloader.download_date_range_stock(stock, pages)
  selected_columns = ["created_at", "body"]
  downloader.dataframe[selected_columns].head(10)
  
  --------------------
  
  # created_at	body
  # 0	2023-04-07T15:24:22Z	NANCY PELOSI JUST BOUGHT 10,000 SHARES OF APPL...
  # 1	2023-04-07T15:17:43Z	$AAPL $SPY \n \nhttps://amp.scmp.com/news/chi...
  # 2	2023-04-07T15:17:25Z	$AAPL $GOOG $AMZN I took a Trump today. \n\nH...
  # 3	2023-04-07T15:16:54Z	$SPY $AAPL will take this baby down, time for ...
  # 4	2023-04-07T15:11:37Z	$SPY $3T it ALREADY DID - look at the pre-COV...
  # 5	2023-04-07T15:10:29Z	$AAPL $QQQ $STUDY We are on to the next one! A...
  # 6	2023-04-07T15:06:00Z	$AAPL was analyzed by 48 analysts. The buy con...
  # 7	2023-04-07T14:54:29Z	$AAPL both retiring. \n \nCraig....
  # 8	2023-04-07T14:40:06Z	$SPY $QQQ $TSLA $AAPL SPY 500 HAS STARTED🚀😍 BI...
  # 9	2023-04-07T14:38:57Z	Nancy 🩵 (Tim) $AAPL
  ```
  
  ``` python
  # Reddit Wallstreetbets
  from finnlp.data_sources.social_media.reddit_streaming import Reddit_Streaming
  
  pages = 3
  config = {
      "use_proxy": "us_free",
      "max_retry": 5,
      "proxy_pages": 2,
  }
  
  downloader = Reddit_Streaming(config)
  downloader.download_streaming_all(pages)
  selected_columns = ["created", "title"]
  downloader.dataframe[selected_columns].head(10)
  
  --------------------
  
  # created	title
  # 0	2023-04-07 15:39:34	Y’all making me feel like spooderman
  # 1	2022-12-21 04:09:42	Do you track your investments in a spreadsheet...
  # 2	2022-12-21 04:09:42	Do you track your investments in a spreadsheet...
  # 3	2023-04-07 15:29:23	Can a Blackberry holder get some help 🥺
  # 4	2023-04-07 14:49:55	The week of CPI and FOMC Minutes… 4-6-23 SPY/ ...
  # 5	2023-04-07 14:19:22	Well let’s hope your job likes you, thanks Jerome
  # 6	2023-04-07 14:06:32	Does anyone else feel an overwhelming sense of...
  # 7	2023-04-07 13:47:59	Watermarked Jesus explains the market being cl...
  # 8	2023-04-07 13:26:23	Jobs report shows 236,000 gain in March. Hot l...
  # 9	2023-04-07 13:07:15	The recession is over! Let's buy more stocks!
  ```
  
* China (Weibo)

  ``` python
  # Weibo
  from finnlp.data_sources.social_media.weibo_date_range import Weibo_Date_Range
  
  start_date = "2016-01-01"
  end_date = "2016-01-02"
  stock = "茅台"
  config = {
      "use_proxy": "china_free",
      "max_retry": 5,
      "proxy_pages": 5,
      "cookies": "Your_Login_Cookies",
  }
  
  downloader = Weibo_Date_Range(config)
  downloader.download_date_range_stock(start_date, end_date, stock = stock)
  df = downloader.dataframe
  df = df.drop_duplicates()
  selected_columns = ["date", "content"]
  df[selected_columns].head(10)
  
  --------------------
  
  # date	content
  # 0	2016-01-01		#舆论之锤#唯品会发声明证实销售假茅台-手机腾讯网O网页链接分享来自浏览器！
  # 2	2016-01-01		2016元旦节快乐酒粮网官方新品首发，茅台镇老酒，酱香原浆酒：酒粮网茅台镇白酒酱香老酒纯粮原...
  # 6	2016-01-01		2016元旦节快乐酒粮网官方新品首发，茅台镇老酒，酱香原浆酒：酒粮网茅台镇白酒酱香老酒纯粮原...
  # 17	2016-01-01		开心，今天喝了两斤酒（茅台+扎二）三个人，开心！
  # 18	2016-01-01		一家专卖假货的网站某宝，你该学学了！//【唯品会售假茅台：供货商被刑拘顾客获十倍补偿】O唯品...
  # 19	2016-01-01		一家专卖假货的网站//【唯品会售假茅台：供货商被刑拘顾客获十倍补偿】O唯品会售假茅台：供货商...
  # 20	2016-01-01		前几天说了几点不看好茅台的理由，今年过节喝点茅台支持下，个人口感，茅台比小五好喝，茅台依然是...
  # 21	2016-01-01		老杜酱酒已到货，从明天起正式在甘肃武威开卖。可以不相信我说的话，但一定不要怀疑@杜子建的为人...
  # 22	2016-01-01		【唯品会售假茅台后续：供货商被刑拘顾客获十倍补偿】此前，有网友投诉其在唯品会购买的茅台酒质量...
  # 23	2016-01-01		唯品会卖假茅台，供货商被刑拘，买家获十倍补偿8888元|此前，有网友在网络论坛发贴（唯品会宣...
  ```

### 3. Company Announcement

* US

  ``` python
  # SEC
  from finnlp.data_sources.company_announcement.sec import SEC_Announcement
  
  start_date = "2020-01-01"
  end_date = "2020-06-01"
  stock = "AAPL"
  config = {
      "use_proxy": "us_free",
      "max_retry": 5,
      "proxy_pages": 3,
  }
  
  downloader = SEC_Announcement(config)
  downloader.download_date_range_stock(start_date, end_date, stock = stock)
  selected_columns = ["file_date", "display_names", "content"]
  downloader.dataframe[selected_columns].head(10)
  
  --------------------
  
  # file_date	display_names	content
  # 0	2020-05-12	[KONDO CHRIS (CIK 0001631982), Apple Inc. (A...	SEC Form 4 \n FORM 4UNITED STATES SECURITIES...
  # 1	2020-04-30	[JUNG ANDREA (CIK 0001051401), Apple Inc. (A...	SEC Form 4 \n FORM 4UNITED STATES SECURITIES...
  # 2	2020-04-17	[O'BRIEN DEIRDRE (CIK 0001767094), Apple Inc....	SEC Form 4 \n FORM 4UNITED STATES SECURITIES...
  # 3	2020-04-17	[KONDO CHRIS (CIK 0001631982), Apple Inc. (A...	SEC Form 4 \n FORM 4UNITED STATES SECURITIES...
  # 4	2020-04-09	[Maestri Luca (CIK 0001513362), Apple Inc. (...	SEC Form 4 \n FORM 4UNITED STATES SECURITIES...
  # 5	2020-04-03	[WILLIAMS JEFFREY E (CIK 0001496686), Apple I...	SEC Form 4 \n FORM 4UNITED STATES SECURITIES...
  # 6	2020-04-03	[Maestri Luca (CIK 0001513362), Apple Inc. (...	SEC Form 4 \n FORM 4UNITED STATES SECURITIES...
  # 7	2020-02-28	[WAGNER SUSAN (CIK 0001059235), Apple Inc. (...	SEC Form 4 \n FORM 4UNITED STATES SECURITIES...
  # 8	2020-02-28	[LEVINSON ARTHUR D (CIK 0001214128), Apple In...	SEC Form 4 \n FORM 4UNITED STATES SECURITIES...
  # 9	2020-02-28	[JUNG ANDREA (CIK 0001051401), Apple Inc. (A...	SEC Form 4 \n FORM 4UNITED STATES SECURITIES...
  ```

* China

  ``` python
  # Juchao
  from finnlp.data_sources.company_announcement.juchao import Juchao_Announcement
  
  start_date = "2020-01-01"
  end_date = "2020-06-01"
  stock = "000001"
  config = {
      "use_proxy": "china_free",
      "max_retry": 5,
      "proxy_pages": 3,
  }
  
  downloader = Juchao_Announcement(config)
  downloader.download_date_range_stock(start_date, end_date, stock = stock, get_content = True, delate_pdf = True)
  selected_columns = ["announcementTime", "shortTitle","Content"]
  downloader.dataframe[selected_columns].head(10)
  
  --------------------
  
  # announcementTime	shortTitle	Content
  # 0	2020-05-27	关于2020年第一期小型微型企业贷款专项金融债券发行完毕的公告	证券代码： 000001 证券简称：平安银行 ...
  # 1	2020-05-22	2019年年度权益分派实施公告	1 证券代码： 000001 证券简称：平安银行 ...
  # 2	2020-05-20	关于获准发行小微企业贷款专项金融债券的公告	证券代码： 000001 证券简称：平安银行 ...
  # 3	2020-05-16	监事会决议公告	1 证券代码： 000001 证券简称： 平安银行 ...
  # 4	2020-05-15	2019年年度股东大会决议公告	1 证券代码： 000001 证券简称：平安银行 ...
  # 5	2020-05-15	2019年年度股东大会的法律意见书	北京总部 电话 : (86 -10) 8519 -1300 传真 : (86 -10...
  # 6	2020-04-30	中信证券股份有限公司、平安证券股份有限公司关于公司关联交易有关事项的核查意见	1 中信证券股份有限公司 、平安证券股份有限 公司 关于平安银行股份有限公司 关联交易 有...
  # 7	2020-04-30	独立董事独立意见	1 平安银行股份有限公司独立董事独立意见 根据《关于在上市公司建立独立董事制度的指导...
  # 8	2020-04-30	关联交易公告	1 证券代码： 000001 证券简称：平安银行 ...
  # 9	2020-04-21	2020年第一季度报告全文	证券代码： 000001 证券简称：平安银行 ...
  ```


## Ⅱ. Data Sources

### 1. News

|      Platform       |    Data Type    | Related Market | Specified Company | Range  Type |        Limits        | Support |
| :----------------------------------------------------------: | :--------: | :------------: | :----------------------------------------------------------: | :---------------: | :-------------------: | ------------------------------------------------------------ |
|        Yahoo        | Financial News  |   US Stocks    |         √         | Date Range  |         N/A          |    √    |
|       Reuters       | General News |   US Stocks    |         ×         | Date Range  |         N/A          |    Soon    |
| Seeking Alpha | Financial News | US Stocks | √ | Streaming | N/A | √ |
|        Sina         | Financial News  |   CN Stocks    |         ×         | Date Range  |         N/A          |    √    |
|      Eastmoney      | Financial News  |   CN Stocks    |         √         | Date Range  |         N/A          |    √    |
|        Yicai        | Financial News  |   CN Stocks    |         √         | Date Range  |         N/A          |  Soon   |
|        CCTV         | General News |   CN Stocks    |         ×         | Date Range  |         N/A          |    √    |
| US Mainstream Media | Financial News  |   US Stocks    |         √         | Date Range  |    Account (Free)    |    √    |
| CN Mainstream Media | Financial News  |   CN Stocks    |         ×         | Date Range  | Account (￥500/year) |    √    |

### 2. Social Media

|        Platform         | Data Type | Related Market | Specified Company | Range Type | Source Type | Limits  | Support |
| :---------------------: | :-------: | :------------: | :---------------: | :--------: | :---------: | :-----: | :-----: |
|         Twitter         |  Tweets   |   US Stocks    |         √         | Date Range |  Official   |   N/A   |    √    |
|         Twitter         | Sentiment |   US Stocks    |         √         | Date Range | Third Party |   N/A   |    √    |
|       StockTwits        |  Tweets   |   US Stocks    |         √         |  Lastest   |  Official   |   N/A   |    √    |
| Reddit (wallstreetbets) |  Threads  |   US Stocks    |         ×         |  Lastest   |  Official   |   N/A   |    √    |
|         Reddit          | Sentiment |   US Stocks    |         √         | Date Range | Third Party |   N/A   |    √    |
|          Weibo          |  Tweets   |   CN Stocks    |         √         | Date Range |  Official   | Cookies |    √    |
|          Weibo          |  Tweets   |   CN Stocks    |         √         |  Lastest   |  Official   |   N/A   |    √    |

### 3. Company Announcement
|         Platform          | Data Type | Related Market | Specified Company | Range Type | Source Type | Limits | Support |
| :-----------------------: | :-------: | :------------: | :---------------: | :--------: | :---------: | :----: | :-----: |
| Juchao (Official Website) |   Text    |   CN Stocks    |         √         | Date Range |  Official   |  N/A   |    √    |
|  SEC (Official Website)   |   Text    |   US Stocks    |         √         | Date Range |  Official   |  N/A   |    √    |
|           Sina            |   Text    |   CN Stocks    |         √         |  Lastest   | Third Party |  N/A   |    √    |


### 4. Data Sets
  |   Data Source    | Type | Stocks | Dates | Available |
  | :--------------: | :----: | :----: | :-------: | :--------------: |
  | [AShare](https://github.com/JinanZou/Astock)  | News |   3680   |   2018-07-01 to 2021-11-30   |  √  |
  | [stocknet-dataset](https://github.com/yumoxu/stocknet-dataset) | Tweets |   87   |   2014-01-02 to 2015-12-30   |  √  |
  | [CHRNN](https://github.com/wuhuizhe/CHRNN) | Tweets | 38 | 2017-01-03 to 2017-12-28 | √ |

## Ⅲ. Large Language Models (LLMs)
* [ChatGPT (GPT 3.5)](https://openai.com/blog/chatgpt)
* [GPT 4.0](https://openai.com/research/gpt-4)
* [ChatGLM](https://github.com/THUDM/ChatGLM-6B)
* [PaLM](https://developers.googleblog.com/2023/03/announcing-palm-api-and-makersuite.html)
* [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/)
* [FinBERT](https://github.com/yya518/FinBERT)
* [Hugging Face](https://huggingface.co/)
