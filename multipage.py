import requests
from bs4 import BeautifulSoup
import pandas as pd

for i in range(2,11):
    url = "https://www.flipkart.com/search?q=mobile+phones+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r = requests.get(url)
    # print(r)

    soup = BeautifulSoup(r.text, "html.parser")
    # print(soup)


