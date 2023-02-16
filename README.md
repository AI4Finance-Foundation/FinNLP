# Natural Language Processing in Finance
# 

The demos will be shown in [ChatGPT for FinTech](https://github.com/AI4Finance-Foundation/ChatGPT-for-FinTech)


## Data sources

### 1. News

* Tushare
* Akshare
* Yahoo Finance

### 2. Social Media

* Twitter
* Weibo

### 3. Trends

* Google trends
* Baidu index

* [[Github] Google Trends Data for automated stock trading using Reinforcement learning.](https://github.com/Athe-kunal/Reinforcement-learning-trading-agent-using-Google-trends-data)

## Large Language Models (LLM)
### 1. GPT-3
### 2. PaML
### 3. [FinBERT](https://github.com/yya518/FinBERT)

## Files Structure

``` python
- demo
- finnlp
    - data_sources
        - _base.py
        - __init__.py
        - news
            -akshare.py
            -tushare.py
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



## Next Steps

### 1. Connect to existed News sources (新闻联播/Financial media..)
### 2. Connect to Google Trends / Baidu Index
### 3. Connect to Twitter / Weibo
