"""
SPECS FOR BTC BOT TRADING:
*goes on investing.com
*fetch the candlestick datas of the previous days
*buy/sell on Kraken in function of the model: hammer/hanging man
*spotlimits have to be implemented to avoid losing all"""

import re
import requests
from bs4 import BeautifulSoup
import time
import os

#URL = "https://www.google.com/search?q=btc%20cours"
#URL = "https://courscryptomonnaies.com/bitcoin"
URL = "https://markets.businessinsider.com/currencies/btc-eur"

while True:
    try:
        r = requests.get(URL)

        soup=BeautifulSoup(r.content,'html.parser')
        span=str(soup.find('span', {'class' : 'push-data'}))

        value_BTC=re.findall(r'[0-9],[0-9]{3}\.[0-9]{2}', span)
        print(value_BTC)

        time.sleep(10)
    except KeyboardInterrupt:
        break

    """next steps:
        -the fetching will occur every minute - 100%
        -code a trading_bot that can decide to buy/sell
        -then save the value in a text file - 0%
        -build a function that can decide to buy/sell - 0% """



