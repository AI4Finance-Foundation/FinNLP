from finnlp.data_sources._base import FinNLP_Downloader

class Company_Announcement_Downloader(FinNLP_Downloader):

    def __init__(self, args = {}):
        super().__init__(args)
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