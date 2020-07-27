"""this script has been built:
-to fetch in real-time the value of the BTC
-then save the value in a text file
-the fetching will occur every minute
libraries to use:
-beautifulsoup
-requests
-time"""

import re
import requests
from bs4 import BeautifulSoup

#URL = "https://www.google.com/search?q=btc%20cours"
URL = "https://courscryptomonnaies.com/bitcoin"
r = requests.get(URL)

soup=BeautifulSoup(r.content,'html.parser')
str=soup.find("div",text="price")
print(str)




