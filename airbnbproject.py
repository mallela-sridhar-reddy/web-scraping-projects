import requests
from bs4 import BeautifulSoup
import pandas as pd

name_list = []
price_list = []
desc_list = []
reviews_list = []

url = "https://www.airbnb.co.in/s/delhi/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-06-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "html.parser")
for i in range(1,15):
    next_page = soup.find("a", class_="l1j9v1wn c1ytbx3a dir dir-ltr").get("href")
    # Complete next page = cnp
    cnp = "https://www.airbnb.co.in" + next_page
    # print(cnp)
    url = cnp
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    names = soup.find_all("div", class_="t1jojoys dir dir-ltr")
    # print(names)
    for i in names:
        name = i.text
        name_list.append(name)
    # print(name_list)
    # print(len(name_list))

    #
    # prices = soup.find_all("span", class_="_tyxjp1")
    # for i in prices:
    #     price = i.text
    #     price_list.append(price)
    # print(price_list)
    # print(len(price_list))

    desc = soup.find_all("span", class_="t6mzqp7 dir dir-ltr")
    for i in desc:
        descr = i.text
        desc_list.append(descr)
    # print(desc_list)
    # print(len(desc_list))

    reviews = soup.find_all("span", class_="r1dxllyb dir dir-ltr")
    for i in reviews:
        review = i.text
        reviews_list.append(review)
    # print(reviews_list)
    # print(len(reviews_list))
df = pd.DataFrame({"Hotel name":name_list, "Hotel Description":desc_list})
df.to_csv("hotels.csv")


