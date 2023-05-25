import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://ticker.finology.in/"
r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table", class_="table table-sm table-hover screenertable")
headers = table.find_all("th")
# print(headers)
titles = []
for i in headers:
    title = i.text
    titles.append(title)
# print(titles)
df = pd.DataFrame(columns=titles)
rows = table.find_all("tr")
for i in rows[1:]:
    data = i.find_all("td")
    row = [elm.text for elm in data]
    print(row)
    l = len(df)
    # print(l)
    df.loc[l] = row
# df.to_csv("stock_market_data.csv")
