# SEC DATA DOWNLOADER

Please checkout this repo that I am building on SEC Question Answering Agent [SEC-QA](https://github.com/Athe-kunal/SEC-QA-Agent)

This repository downloads all the texts from SEC documents (10-K and 10-Q). Currently, it is not supporting documents that are amended, but that will be added in the near futures.

Install the required dependencies

```
python install -r requirements.txt
```

The SEC Downloader expects 5 attributes

* tickers: It is a list of valid tickers
* amount: Number of documents that you want to download
* filing_type: 10-K or 10-Q filing type
* num_workers: It is for multithreading and multiprocessing. We have multi-threading at the ticker level and multi-processing at the year level for a given ticker
* include_amends: To include amendments or not.


## REFERENCES
1. Unstructured SEC Filings API: [repo link](https://github.com/Unstructured-IO/pipeline-sec-filings/tree/main)
2. SEC Edgar Downloader: [repo link](https://github.com/jadchaar/sec-edgar-downloader)

