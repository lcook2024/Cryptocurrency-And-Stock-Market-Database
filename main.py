"""
Author: Logan Cook

Cryptocurrency Databases

Utilizes the CoinMarketCap API, along with imports from requests, json, and os, pandas data reader. PDR pulls from Yahoo finance.

The goal of the code is to provide the user an easy and effecient way to be provided will all of the data they need on their favorite cryptos and stocks. 

"""
import pandas_datareader
import pandas_datareader as pdr
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os

def stock():
  """
  This functions utilizes the Pandas Data Reader to pull stock data from Yahoo finance 
  
  No parameters or returns.
  """
  print("Hello, and welcome to your friendly neighborhood stock market database! \nThis data base can provide you information on thousands of stocks. \nIt'll display you data from 5 years ago, and current day. \nThe name of the data is on top and it's value is below! \nThe date the data is from is displayed on the left. \nI hope you can find this useful!\n")
  print("Some popular stocks and their tickers: \n Amazon, AMZN \n Apple, APPL \n Coca-Cola, KO \n Tesla, TSLA \nRemember you can put in any stock ticker! \n")
  ticker = input("What stock would you like data on (Please input ticker)? ")
  data = pdr.get_data_yahoo(ticker)
  print(str(data))

def crypto():
  """
  This functions utilizes the Coin Market Cap API to provide the user with crytpocurrency data based off their user input
  
  No parameters or returns.
  """
  print("Hello, and welcome to your friendly neighborhood Cyrptocurrency database! \nThis data base can provide you information on thousands of cryptos. \nIt'll display you the information in a format you're not used to, but it's simple! \nThe name of the infomation is on the left, and the value is on the right. \nI hope you can find this useful!\n")

  print("Some popular Cryptocurrencies and their tickers are: \n Bitcoin, BTC \n Ethereum, ETH \n Dogecoin, DOGE \n Monero, XMR \n Ripple, XRP \n Litecoin, LTC \n Bitcoin Cash, BCH \n ")

  id = input("What Crypto do you want data on (Please input ticker)? ")

  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
  parameters = {
    'symbol':str(id)
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'f8f7c3ae-8f2d-496d-a6bf-b595d4b7f63b',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    PrettyJson = json.dumps(data, indent=4, separators=(',', ': '), sort_keys=True)
    print(str(PrettyJson))
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

  print("\nPlease note that the console will clear when you run the program again!")

#Below clears the terminal each time the code runs
if __name__ == "__main__":
  os.system("clear")

choice = input("What would you like data on, stocks or Cyrptocurrency? ")

#Uses the choice variable to determine which function to use
if choice == "Stocks" or choice == "stocks" or choice == "Stock market" or choice == "stock market" or choice == "Stock Market" or choice == "Stock" or choice == "stock":
  print("\n")
  stock()
elif choice == "Cryptocurrency" or choice == "cryptocurrency" or choice == "Crypto" or choice == "crypto":
  print("\n")
  crypto()