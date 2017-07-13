#!/usr/bin/python
import requests, json, redis

rdb=redis.StrictRedis(host="localhost", port=6379, db=0)
#url = "https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=GBP"
url = "https://api.cryptonator.com/api/full/eth-gbp"
Resp = requests.get(url)

# For successful API call, response code will be 200 (OK)
if(Resp.ok):
    ticker = json.loads(Resp.content)
    print "timestamp: ",ticker["timestamp"]
    timestamp = ticker["timestamp"]
    print "ETH/GBP: ",ticker["ticker"]["price"]
    price = ticker["ticker"]["price"]
    rdb.set(timestamp,price)
else:
    Resp.raise_for_status()

print rdb.keys()
