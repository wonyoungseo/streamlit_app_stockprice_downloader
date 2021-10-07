from datetime import datetime
from dateutil.relativedelta import relativedelta
import time

import FinanceDataReader as fdr

def get_comp_info(stock_market_info: dict) -> dict:
    '''

    Parameters
    ----------
    stock_market_info: dict

    Returns
    -------
    result: dict
    '''


    time_st = time.time()
    result = {}
    for country in stock_market_info.keys():

        result[country] = {}

        for market in stock_market_info[country]:
            listed_comp_df = fdr.StockListing(market)
            listed_comp_df['comp_id'] = listed_comp_df['Symbol'] + ' : ' + listed_comp_df['Name']
            listed_comp_df.sort_values(by='comp_id', ascending=True, inplace=True)
            listed_comp_df.reset_index(drop=True, inplace=True)
            listed_comp_df.set_index(keys='comp_id', inplace=True)
            if 'ListingDate' in listed_comp_df.columns:
                listed_comp_df['ListingDate'] = listed_comp_df['ListingDate'].apply(lambda x: str(x)[:10])
            result[country][market] = listed_comp_df.to_dict(orient='index')

    print("Loading time: `{}` sec".format(time.time() - time_st))

    return result


def get_stock_data(comp_info:dict, days=30):
    '''

    Parameters
    ----------
    comp_info : dict
    days : int

    Returns
    -------
    data : pandas dataframe
    '''
    code = comp_info['Symbol']

    date_st = str(datetime.now() - relativedelta(days=days))[:10]
    date_ed = str(datetime.now())[:10]

    data = fdr.DataReader(code, date_st, date_ed)
    data = data.reset_index(drop=False)
    data['Date'] = data['Date'].apply(lambda x: str(x)[:10])
    return data
