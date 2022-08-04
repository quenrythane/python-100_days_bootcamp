from bs4 import BeautifulSoup
import lxml
import requests as req


# period = input("what year you would like to travel to (YYY-MM-DD format): ")
# URL = f"https://www.billboard.com/charts/hot-100/{period}/"
URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"

response = req.get(URL)
soup = BeautifulSoup(response.text, 'lxml')
print(soup.prettify())


