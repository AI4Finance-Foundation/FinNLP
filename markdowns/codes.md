# FinNLP

## Codes

### Data Sources

#### News (Finnhub, Sina)

``` python
class News_Downloader:
    
    def __init__(self, args = {}):
        pass

    def download_date_range_all(self, start_date, end_date):
        pass
    
    def download_date_range_stock(self, start_date, end_date, stock = "AAPL"):
        pass
    
    def download_streaming_all(self, rounds = 3):
        pass
    
    def download_streaming_stock(self, stock = None, rounds = 3):
        pass

    def clean_data(self):
        pass
    
    def gather_content(self, delay = 0.01):
        pass
```



#### Social Media (Twitter, Stocktwits, Reddit, Weibo)

``` python
class Social_Media_Downloader:

    def __init__(self, args = {}):
        pass

    def download_date_range_all(self, start_date, end_date):
        pass
    
    def download_date_range_stock(self, start_date, end_date, stock = "AAPL"):
        pass
    
    def download_streaming_all(self, rounds = 3):
        pass
    
    def download_streaming_stock(self, stock = None, rounds = 3):
        pass

    def clean_data(self):
        pass
```

#### Company Announcement (Juchao, SEC)

``` python
class company_announcement_Downloader:

    def __init__(self, args = {}):
        pass

    def download_date_range_all(self, start_date, end_date):
        pass
    
    def download_date_range_stock(self, start_date, end_date, stock = "AAPL"):
        pass
    
    def download_streaming_all(self, rounds = 3):
        pass
    
    def download_streaming_stock(self, stock = None, rounds = 3):
        pass

    def clean_data(self):
        pass
```