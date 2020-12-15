"""
Author: Logan Cook

Cryptocurrency Applications 

"""

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

print("Some popular Cryptocurrencies and their tickers are: \n Bitcoin, BTC \n Ethereum, ETH \n Dogecoin, DOGE \n")
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

