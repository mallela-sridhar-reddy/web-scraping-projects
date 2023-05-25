import requests
from bs4 import BeautifulSoup
import pandas as pd

name_list = []
price_list = []
desc_list = []
reviews_list = []
url = "https://www.flipkart.com/search?q=mobile+phones+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
r = requests.get(url)
# print(r)

soup = BeautifulSoup(r.text, "html.parser")
box = soup.find("div", class_="_1YokD2 _3Mn1Gg")
names = box.find_all("div", class_="_4rR01T")
# print(names)
for i in names:
    name = i.text
    name_list.append(name)
# print(name_list)
print(len(name_list))


prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
for i in prices:
    price = i.text
    price_list.append(price)
# print(price_list)
print(len(price_list))

desc = box.find_all("ul", class_="_1xgFaf")
for i in desc:
    descr = i.text
    desc_list.append(descr)
# print(desc_list)
print(len(desc_list))

reviews = box.find_all("div", class_="_3LWZlK")
for i in reviews:
    review = i.text
    reviews_list.append(review)
# print(reviews_list)
print(len(reviews_list))

df = pd.DataFrame({"Product name":name_list, "Product price":price_list, "Product Description":desc_list, "Product review":reviews_list})
df.to_csv("mobiles.csv")
