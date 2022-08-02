from bs4 import BeautifulSoup
import requests as req

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = req.get(URL)

soup = BeautifulSoup(response.text, 'lxml')
print(soup.prettify())

