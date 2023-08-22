import datasets
import pandas as pd
from tqdm.notebook import tqdm
import json
import os

def load_dataset(dataset_name, **kwargs):
    if dataset_name == "Stocknet":
        root_path = r"../../../stocknet-dataset/tweet/raw"
        stock_lists = os.listdir(root_path)
        all = pd.DataFrame()
        for stock in tqdm(stock_lists, desc="Loading Stocknet dataset..."):
            stock_path = os.path.join(root_path, stock)
            date_files = os.listdir(stock_path)
            for date in date_files:
                with open(os.path.join(stock_path, date_files[0])) as f:
                    json_list = f.readlines()
                tmp_json = []
                for json_str in json_list:
                    tmp_json.append(json.loads(json_str))
                tmp_json = pd.DataFrame(tmp_json)
                all = pd.concat([all, tmp_json], axis=0)
        all = all.reset_index(drop=True)
        all = datasets.Dataset.from_pandas(all)
        return all

    else:
        raise NotImplementedError("Only support Stocknet dataset for now")

