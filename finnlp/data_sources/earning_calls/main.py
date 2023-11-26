from datetime import datetime
from typing import List

try:
    from finnlp.data_sources.earning_calls.utils import get_earning_transcripts
except ImportError:
    from utils import get_earning_transcripts


class EarningCallTranscripts():
    def __init__(self, year: int, ticker: str, quarter: str):
        """Get the earning call transcripts for a given company, in a given year and quarter

        Args:
            year (int): Year of the transcript
            ticker (str): ticker symbol of the stock
            quarter (str): quarter
        """
        curr_year = datetime.now().year
        assert year <= curr_year, "The year should be less than current year"

        assert quarter in [
            "Q1",
            "Q2",
            "Q3",
            "Q4",
        ], 'The quarter should from the list ["Q1","Q2","Q3","Q4"]'
        self.year = year
        self.ticker = ticker
        self.quarter = quarter

    def load_data(self):
        resp_dict, speakers_list = get_earning_transcripts(
            self.quarter, self.ticker, self.year
        )
        return {
            "text":resp_dict["content"],
            "metadata":{
                "ticker": resp_dict["symbol"],
                "quarter": "Q" + str(resp_dict["quarter"]),
                "date_time": resp_dict["date"],
                "speakers_list": speakers_list,
            },
        }
        
