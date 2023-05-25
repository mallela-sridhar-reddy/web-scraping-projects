
import requests
from bs4 import BeautifulSoup

url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

# # Using find function to  find the price of a specific product
# price = soup.find("h4", {"class":"pull-right price"})
# # or
# # price = soup.find("h4", class_ ="pull-right price")
# print(price)
# print(price.text)
# # or
# # print(price.string)

# # Using find_all function to  find the price of a specific product
# price = soup.find_all("h4", {"class":"pull-right price"})
# # print(len(price))
# for i in price:
#     print(i.string)

# # Using find_all function with regular expressions
#
# # without regular expressions
# data = soup.find_all(string=re.compile("Galaxy"))
# print(data)
#
# # without regular expressions
# data = soup.find_all(string="Galaxy")
# print(data)

# Using regex along with pandas

