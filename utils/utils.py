import json
from io import BytesIO
import pandas as pd
import streamlit as st


def read_json(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as f:
        data: dict = json.load(f)
    return data


def convert_df_excel_binary(df):
    '''
    Convert pandas dataframe into binary file
    '''
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.save()
    value = output.getvalue()
    return value


def download_df(dataframe, filename):
    data = convert_df_excel_binary(dataframe)
    st.download_button(label = 'Download data (Excel)',
                       data=data,
                       file_name = '{}.xlsx'.format(filename),
                       mime = 'application/octet-stream')