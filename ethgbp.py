#!/usr/bin/python
import requests, json

#url = "https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=GBP"
url = "https://api.cryptonator.com/api/full/eth-gbp"
Resp = requests.get(url)

# For successful API call, response code will be 200 (OK)
if(Resp.ok):
    ticker = json.loads(Resp.content)
    print "ETH/GBP: ",ticker["ticker"]["price"]
else:
    Resp.raise_for_status()
