import requests
import openpyxl
from bs4 import BeautifulSoup


excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = "Top Rated Movies"
sheet.append(["Movie Name", "Movie Rank", "Year Of Release", "Imdb Rating"])
try:
    url = requests.get("https://www.imdb.com/chart/top")
    # To raise errors
    url.raise_for_status()

    soup = BeautifulSoup(url.text, "html.parser")
    movies = soup.find("tbody", class_="lister-list").find_all("tr")
    # print(movies)
    for movie in movies:
        name = movie.find("td", class_="titleColumn").find("a").text
        rank = movie.find("td", class_="titleColumn").get_text(strip=True).split(".")[0]
        year = movie.find("td", class_="titleColumn").find("span").text.strip("()")
        rating = movie.find("td", class_="ratingColumn imdbRating").strong.text
        print(name, rank, year, rating)
        sheet.append([name, rank, year, rating])
except Exception as e:
    print(e)

excel.save("IMDB Movie Ratings.xlsx")



