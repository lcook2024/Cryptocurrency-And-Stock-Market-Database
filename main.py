"""
Author: Logan Cook

Cryptocurrency Applications 

"""

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

id = input("What Crypto ID do you want data on? ")

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'id':str(id)
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
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

