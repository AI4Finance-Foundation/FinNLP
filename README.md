# Natural Language Dataset for Finance

The demos will be shown in [ChatGPT for FinTech](https://github.com/AI4Finance-Foundation/ChatGPT-for-FinTech)


**Disclaimer: We are sharing codes for academic purpose udner the MIT education license. Nothing herein is financial advice, and NOT a recommendation to trade real money. Please use common sense and always first consult a professional before trading or investing.**

## Ⅰ. Data sources

### 1. News

  |                         Data Source                          |      Source Type      |                  Limits                   | Avaliable |
  | :----------------------------------------------------------: | :--------------: | :---------------------------------------: | :-------: |
  | [Sina Finance](https://news.sina.com.cn/roll/#pageid=153&lid=2516&k=&num=50&page=1) | Official Website |                    N/A                    |     √     |
  |           [Yahoo Finance](https://news.yahoo.com/)           | Official Website |                    N/A                    |   Soon    |
  | [Akshare CCTV](https://akshare.akfamily.xyz/data/others/others.html#id6) | Official Website |                    N/A                    |     √     |
  | [Tushare Major News](https://tushare.pro/document/2?doc_id=195) |  Tushare Sever   | Account-specific（About ￥500 per year ） |     √     |




### 2. Social Media

  |   Data Source    | Source Type | Limits | Avaliable |
  | :--------------: | :----: | :----: | :-------: |
  | Twitter  | Official Website |   -    |  Soon  |
  | Weibo | Official Website |   -    |  Soon  |
  | StockTwits| Official Website |   -    |  Soon  |

### 3. Trends

  |   Data Source    | Source Type | Limits | Avaliable |
  | :--------------: | :----: | :----: | :-------: |
  | Google Trends  | Official Website |   -    |  Soon  |
  | Baidu index | Official Website |   -    |  Soon  |
  | Weibo Trends| Official Website |   -    |  Soon  |

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
