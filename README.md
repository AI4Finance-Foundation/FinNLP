# Natural Language Dataset for Finance

The demos will be shown in [ChatGPT for FinTech](https://github.com/AI4Finance-Foundation/ChatGPT-for-FinTech)


**Disclaimer: We are sharing codes for academic purpose under the MIT education license. Nothing herein is financial advice, and NOT a recommendation to trade real money. Please use common sense and always first consult a professional before trading or investing.**


## Ⅰ. Data sources

### 1. News

|             Data Source              |    Source Type    |    Sources    |    Related Market    |    News Type    |    Specified Company    |          Limits          | Avaliable |
| :-------------------------------: | :---------: | :-------------------------: | :-------: | :-------: | :-------: | :-------: | --------- |
| [Sina Finance](https://news.sina.com.cn/roll/#pageid=153&lid=2516&k=&num=50&page=1) | Official Website | Sina | CN Securities | Finance | × |           Not too much      |   √   |
|      [Yahoo Finance](https://news.yahoo.com/)      | Official Website | Yahoo | US Stocks | Finance | × |           N/A           |  Soon   |
| [Finnhub](https://github.com/Finnhub-Stock-API/finnhub-python) | Gathering| Yahoo, SeekingAlpha, MarketWatch, CNBC, Fintel，Reuters, Associated Press, DowJones, Seeking Alpha, GuruFocus, Thefly.com, TalkMarkets, TipRanks, InvestorPlace, StockMarket，Alliance News, PennyStocks, Nasdaq ... | US Stocks | Finance | √ |Account-specific （Free）|√|
| [Akshare CCTV](https://akshare.akfamily.xyz/data/others/others.html#id6) | Gathering | CCTV | CN Securities | Official | × |           N/A           |   √   |
| [Tushare Major News](https://tushare.pro/document/2?doc_id=195) |  Gathering  |    |  CN Securities  |  Finance  |  ×  | Account-specific（About ￥500 per year ） |   √   |




### 2. Social Media

|  Data Source   | Source Type | Sources | Limits | Avaliable |
| :--------------: | :----: | :----: | :-------: | :-------: |
| Twitter  | Content | Twitter |  -   |  Soon  |
| Weibo | Content | Weibo |  -   |  Soon  |
| StockTwits| Content | StockTwits |  -   |  Soon  |
| [Finnhub](https://finnhub.io/docs/api/social-sentiment)| Sentiment Score | Reddit、Twitter |  N/A  |  √  |

### 3. Trends

  |   Data Source    | Source Type | Limits | Avaliable |
  | :--------------: | :----: | :----: | :-------: |
  | [Google Trends](https://trends.google.com/trends/explore)  | Official Website |   N/A    |  √  |
  | Baidu index | Official Website |   -    |  Soon  |
  | Weibo Trends| Official Website |   -    |  Soon  |

### 4. Company Announcement

  |   Data Source    | Source Type | Limits | Avaliable |
  | :--------------: | :----: | :----: | :-------: |
  | [Sina](https://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllBulletin/stockid/600519.phtml)  | Official Website |   Not too much    |  √  |


### 5. Data Sets
  |   Data Source    | Type | Stocks | Dates | Avaliable |
  | :--------------: | :----: | :----: | :-------: | :--------------: |
  | [AShare](https://github.com/JinanZou/Astock)  | News |   -   |   -   |  √  |
  | [stocknet-dataset](https://github.com/yumoxu/stocknet-dataset) | Tweets |   87   |   2014-01-02 to 2015-12-30   |  √  |
  | [CHRNN](https://github.com/wuhuizhe/CHRNN) | Tweets | 38 | 2017-01-03 to 2017-12-28 | √ |

### 4. Other resources

* [[Github] Google Trends Data for automated stock trading using Reinforcement learning.](https://github.com/Athe-kunal/Reinforcement-learning-trading-agent-using-Google-trends-data)

## Ⅱ. Large Language Models (LLM)
*  GPT-3
*  PaML
*  [FinBERT](https://github.com/yya518/FinBERT)

## Ⅲ. Files Structure

``` python
- demo
- finnlp
    - data_sources
        - _base.py
        - __init__.py
        - news
            - akshare_cctv.py
            - sina_finance.py
            - tushare.py
        - social_media
            - stocktwits.py
            - twitter.py
            - weibo.py
        - trends
            - baidu.py
            - google.py
    - large_language_models
        - __init__.py
        - embeddings
            - bert.py
            - finbert.py
        - sentiment
            - gpt3.py
            - paml.py
- .... 
```



## Ⅳ. Roadmaps

#### 1. Connect to existed News sources (新闻联播/Financial media..)
#### 2. Connect to Google Trends / Baidu Index
#### 3. Connect to Twitter / Weibo
