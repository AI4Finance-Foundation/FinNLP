# Natural Language Dataset for Finance

The demos will be shown in [ChatGPT for FinTech](https://github.com/AI4Finance-Foundation/ChatGPT-for-FinTech)


**Disclaimer: We are sharing codes for academic purpose under the MIT education license. Nothing herein is financial advice, and NOT a recommendation to trade real money. Please use common sense and always first consult a professional before trading or investing.**


## Ⅰ. Data sources

### 1. News

|                           Platform                           | Data Type  | Related Market |                         Data Source                          | Specified Company | Range  Type  |      Source Type      |                  Limits                   |
| :----------------------------------------------------------: | :--------: | :------------: | :----------------------------------------------------------: | :---------------: | ---------- | :-------------------: | :---------------------------------------: |
|              [Yahoo]((https://news.yahoo.com/))              |  Financial News   |   US Stocks    |    [Finnhub News](./finnlp/data_sources/news/finnhub.py)     |         √         | Date Range | Third party |         Account-specific （Free）         |
| [Sina](https://news.sina.com.cn/roll/#pageid=153&lid=2516&k=&num=50&page=1) |   Financial News    |   CN Stocks    |  [Sina Finance](./finnlp/data_sources/news/sina_finance.py)  |         ×         | Date Range |   Official     |               Not too much                |
|             [CCTV](http://tv.cctv.com/lm/xwlb/)              | Governemnt News |   CN Stocks    |  [Akshare cctv](./finnlp/data_sources/news/akshare_cctv.py)  |         ×         | Date Range | Third party|                    N/A                    |
|                   US Mainstream Media                   |   Financial News    |   US Stocks    |    [Finnhub News](./finnlp/data_sources/news/finnhub.py)     |         √         | Date Range |       Third party       |         Account-specific （Free）         |
|                   CN Mainstream Media                   |   Financial News    |   CN Stocks    | [Tushare Major News](./finnlp/data_sources/news/tushare_major_news.py) |         ×         | Date Range |       Third party       | Account-specific（About ￥500 per year ） |



### 2. Social Media

|                           Platform                           | Data Type | Related Market |                         Data Source                          | Specified Company | Range Type | Source Type | Limits |
| :----------------------------------------------------------: | :-------: | :------------: | :----------------------------------------------------------: | :---------------: | :--------: | :---------: | :----: |
|              [Twitter](https://www.twitter.com)              |  Tweets   |   US Stocks    | [Twitter Downloader](./finnlp/data_sources/social_media/twitter.py) |         √         | Date Range |  Official   |  N/A   |
|              [Twitter](https://www.twitter.com)              | Sentiment |   US Stocks    | [Finnhub Sentiment](./finnlp/data_sources/social_media/finnhub.py) |         √         | Date Range | Third Party |  N/A   |
|            [StockTwits](https://stocktwits.com/)             |  Tweets   |   US Stocks    | [Stocktwits Downloader](./finnlp/data_sources/social_media/stocktwits.py) |         √         |  Lastest   |  Official   |  N/A   |
| [Reddit (wallstreetbets)](https://www.reddit.com/r/wallstreetbets/new/) |  Threads  |   US Stocks    | [Reddit Downloader](./finnlp/data_sources/social_media/reddit.py) |         ×         |  Lastest   |  Official   |  N/A   |
|              [Reddit](https://www.reddit.com/)               | Sentiment |   US Stocks    | [Finnhub Sentiment](./finnlp/data_sources/social_media/finnhub.py) |         √         | Date Range | Third Party |  N/A   |
|                  [Weibo](https://weibo.com)                  |  Tweets   |   CN Stocks    |                             Soon                             |         -         |     -      |      -      |   -    |

### 3. Company Announcement
|                           Platform                           | Data Type | Related Market |                         Data Source                          | Specified Company | Range Type | Source Type |    Limits    |
| :----------------------------------------------------------: | :-------: | :------------: | :----------------------------------------------------------: | :---------------: | :--------: | :---------: | :----------: |
| [Juchao (Official Website)](http://www.cninfo.com.cn/new/index) |   Text    |   CN Stocks    | [Juchao Annoumcement Downloader](./finnlp/data_sources/company_announcement/juchao.py) |         √         | Date Range |  Official   | Not too much |
|        [SEC(Official Website)](https://www.sec.gov/)         |   Text    |   US Stocks    |                             Soon                             |         √         | Date Range |  Official   | Not too much |
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

## Ⅱ. Large Language Models (LLM)
### 1. Chat
* [ChatGPT (GPT 3.5)](https://openai.com/blog/chatgpt)
* [GPT 4.0](https://openai.com/research/gpt-4)
* [ChatGLM](https://github.com/THUDM/ChatGLM-6B)
* [PaLM](https://developers.googleblog.com/2023/03/announcing-palm-api-and-makersuite.html)
* [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/)


### 2. Sentiment/Embedding
* [ChatGPT (GPT 3.5)](https://openai.com/blog/chatgpt)
* [GPT 4.0](https://openai.com/research/gpt-4)
* [ChatGLM](https://github.com/THUDM/ChatGLM-6B)
* [PaLM](https://developers.googleblog.com/2023/03/announcing-palm-api-and-makersuite.html)
* [LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/)
* [FinBERT](https://github.com/yya518/FinBERT)
* [Hugging Face](https://huggingface.co/)
