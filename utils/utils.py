import json
from io import BytesIO
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

def read_json(file_path: str) -> dict:
    '''
    function to read json file
    '''
    with open(file_path, 'r', encoding='utf-8') as f:
        data: dict = json.load(f)
    return data


def convert_df_excel_binary(df):
    '''
    fucntion to convert pandas dataframe into binary file
    '''
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.save()
    value = output.getvalue()
    return value


def download_df(dataframe, filename):
    '''
    function to create streamlit download button customized for excel file
    '''
    data = convert_df_excel_binary(dataframe)
    st.download_button(label = 'Download data (Excel)',
                       data=data,
                       file_name = '{}.xlsx'.format(filename),
                       mime = 'application/octet-stream')


def plot_candle(df):
    '''
    function to create Plotly based candle chart.
    '''
    candle_data = go.Candlestick(
                x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close']
                )
    data = [candle_data]
    fig = go.Figure(data)
    fig.update_layout(
        margin=dict(
                l=5,
                r=5,
                b=5,
                t=5,
                pad=4
            ),
        )
    st.plotly_chart(fig, use_container_width=True)
