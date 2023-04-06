from finnlp.data_sources._base import FinNLP_Downloader

class Social_Media_Downloader(FinNLP_Downloader):

    def __init__(self, args = {}):
        super().__init__(args)
        pass

    def download(self, start_date, end_date, stock = "all"):
        pass

    def clean_data(self):
        pass

    def gather_one_day_news(self,date,stock = "all",delay = 0.1):
        pass

    def transfer_standard_date_to_nonstandard(self,date):
        pass