import requests
from bs4 import BeautifulSoup

url = "https://www.webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
# print(r.status_code) if the output is 200 then we can scrape that web page's data
# print(r.text) HTML output is in unstructured form
soup = BeautifulSoup(r.text, "html.parser")
# print(soup.div)

# To obtain attributes use the below code
# tag = soup.header
# atb = tag.attrs
# print(atb["class"])

# To get a navigable string use the below code
tag = soup.div.p
print(tag.string)

# To obtain HTML comments




