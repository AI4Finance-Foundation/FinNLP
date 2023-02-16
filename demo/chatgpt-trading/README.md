# ChatGPT Trading Bot

[ChatGPT for FinTech](https://github.com/AI4Finance-Foundation/ChatGPT-for-FinTech)

Let's fully use the ChatGPT to create an FinRL agent that trades as smartly as ChatGPT. The codes are available [here](https://github.com/oliverwang15/Alternative-Data/blob/main/demo/chatgpt-trading/main.ipynb)

## 1. Price Data and Tweets Data Preparation

* First, we fetch price data and Tweets data from [stocknet-dataset](https://github.com/yumoxu/stocknet-dataset)
* Second, We input the Tweets data to two GPT models, "text-curie-001" and "text-davinci-003" model and get the sentiment scores
* Third, we save the sentiment scores to the pickle files under `./data`

## 2. ChatGPT Trading Agent

* We used the GPT model to analyze the sentiment of each day's tweets and use the mean of sentiment scores to make trading decisions. 

* Parameters of GPT Model are:

  ``` PyThon
  "model_name": "text-davinci-003",  # "text-curie-001","text-davinci-003"
  "source": "local",                 # "local","openai"
  "api_key": OPEN_AI_TOKEN,          # not necessary when the "source" is "local"
  "buy_threshold": 0.3,              # the max positive sentiment is 1, so this should range from 0 to 1 
  "sell_threshold": -0.3             # the min negative sentiment is -1, so this should range from -1 to 0
  ```

* The `buy_threshold` and `sell_threshold` may have a huge impact on the final results, so they should be considered carefully.

* We don't suggest using  `openai` for the `source` since free accounts may reach limits quickly.

## 3. Trading Market 

* In order to test the trading ability of the Chatgpt trading agent, a special trading environment was designed. This environment can not only be used for the Chatgpt trading agent but also used for the reinforcement learning. 

* Parameters of the Trading Environment are:

  ``` PyThon
  "stock_name" : "AAPL",        # please refer to the stocks provided by stocknet-dataset
  "start_date":"2014-01-01",    # should be later than 2014-01-01
  "end_date":"2015-12-30",      # should be earlier than 2015-12-30
  "init_cash": 100,             # initial avaliable cash
  "init_hold": 0,               # initial avaliable stock holdings
  "cal_on": "Close",            # The column that used to calculate prices
  "trade_volumn": 100,          # Volumns to trade
  ```

* The start price will be normalized to 1, so `init_cash` denotes shares available for buying, and `init_hold` denotes shares available for selling.

* If  you use `stocknet-dataset` the `cal_on` and be `Close` ,`Adj Close` or even `open`,`high`,`low`.

* The environment will adjust the trading volume automatically when the cash is not enough or the holding is not enough, to make sure that the cash is always >= 0 and the holding is always >= 0.

## 4. Final results

* The result shows that the agent have given buy signals when the stock price was about to raise and sell signals when the stock price was about to drop

  ![image-20230216004801458](https://cdn.jsdelivr.net/gh/oliverwang15/imgbed@main/img/Chatgpt_trading_res.png)

* The final backtest results are listed below. 
  |        item         | result  |
  | :-----------------: | :-----: |
  |    Annual return    | 30.603% |
  | Cumulative returns  | 66.112% |
  |  Annual volatility  | 13.453% |
  |    Sharpe ratio     |  2.06   |
  |    Calmar ratio     |  4.51   |
  |      Stability      |  0.87   |
  |    Max drawdown     | -6.778% |
  |     Omega ratio     |  2.00   |
  |    Sortino ratio    |  4.30   |
  |     Tail ratio      |  1.84   |
  | Daily value at risk | -1.585% |
  |        Alpha        |  0.24   |
  |        Beta         |  0.31   |

## 5. TODOs

1. Combing price features

2. Train an FinRL agent on the sentiment scores given by GPT models
