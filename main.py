"""
Author: Logan Cook

Cryptocurrency Databases

Utilizes the CoinMarketCap API, along with imports from requests, json, and os. 

The goal of the code is to provide the user an easy and effecient way to be provided will all of the data they need on their favorite cryptos. 

"""

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os

if __name__ == "__main__":
  os.system("clear")

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