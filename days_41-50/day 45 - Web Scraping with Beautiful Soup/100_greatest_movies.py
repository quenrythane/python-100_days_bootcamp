from bs4 import BeautifulSoup
import requests as req
import re

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = req.get(URL)

soup = BeautifulSoup(response.text, 'lxml')
print(soup)

site_data = str(soup.find(id="__NEXT_DATA__").contents[0])
start_indexes = [occurrence.start() + 13 for occurrence in re.finditer('"titleText":"', site_data)]

for start_index in start_indexes[::-1][1:-1]:
    end_index = site_data.find('"', start_index)
    title = site_data[start_index:end_index]

    try:
        file = open('movies.txt', 'a')
    except FileNotFoundError:
        file = open('movies.txt', 'w')
    finally:
        file.write(f"{title}\n")
        file.close()