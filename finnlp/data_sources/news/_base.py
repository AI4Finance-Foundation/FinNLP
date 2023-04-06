from finnlp.data_sources._base import FinNLP_Downloader

class News_Downloader(FinNLP_Downloader):
    
    def __init__(self, args = {}):
        super().__init__(args)
        pass

    def download_date_range(self, start_date, end_date, stock = None):
        pass
    
    def download_streaming(self, stock = None):
        pass

    def clean_data(self):
        pass

    def _gather_one_part(self, date, stock = None, delay = 0.1):
        pass
    
    def _gather_content(self):
        pass
