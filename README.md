# ETH-GBP
Ultra simple python script to get the lastest Ethereum/GBP change rate.

It is getting the latest rate for ETH/GBP from https://fr.cryptonator.com/rates/ETH-GBP
The api documentation is  https://fr.cryptonator.com/api

It is logging the ETH's rate to a *local* Redis db, with the request's timestamp as a key. 

The script is not flexible. You can't change the coin or the currency. 

To-Do: 
- add market-cap too
- add capability to switch coin
- store past 10 values
