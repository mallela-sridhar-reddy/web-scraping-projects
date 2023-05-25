import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

names = soup.find_all("a", class_="title")
# print(names)
product_name = []

for i in names:
    product_name.append(i.text)

prices = soup.find_all("h4", class_="pull-right price")
# print(prices)
price_list = []

for i in prices:
    price_list.append(i.text)


desc = soup.find_all("p", class_="description")
# print(desc)
desc_list = []

for i in desc:
    desc_list.append(i.text)


reviews = soup.find_all("p", class_="pull-right")
# print(reviews)
reviews_list = []

for i in reviews:
    reviews_list.append(i.text)

df = pd.DataFrame({"Product Name":product_name, "Prices":price_list, "Description": desc_list, "Reviews": reviews_list})
# print(df)
df.to_csv("product_details.csv")