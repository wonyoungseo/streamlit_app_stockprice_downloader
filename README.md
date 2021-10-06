# Streamlit App: Stock price info downloader

[Try it out !](https://share.streamlit.io/lucaseo/streamlit_app_stockprice_downloader/main/app.py)

>Hosted via Streamlit Share

Streamlit app providing stock price information and download data in Excel format.

## Currently available stock market

- USA
	- NASDAQ
	- SP500
	- NYSE
	- AMEX
- South Korea
	- KOSPI
	- KRX
	- KOSDAQ
	- KONEX


## Requirements

The app is developed and tested in Python3.7+

```bash
pip install -r requirements.txt
```


## How to run app

### 1. Download stock information data

- Collecting list of all stocks tasks about 1 ~ min, which makes inefficient user experience. 
- Therefore, storing all stock list is required prior to running or deploying the app.
- The following script will store the listed stock information into `./resource` directory
	```bash
	python prepare_data.py
	```


### 2. Run app

```bash
streamlit run app.py
```

