'''
script to download stock information prior to running the app
'''

import json

import pandas as pd
import FinanceDataReader as fdr
from tqdm import tqdm

from utils.utils import read_json
from utils.utils_fdr import get_comp_info


if __name__ == "__main__":
	stock_market_info = read_json("resource/stock_market.json")
	result = get_comp_info(stock_market_info['market'])

	with open('./resource/stock_list.json','w') as f:
		json.dump(result, f)
