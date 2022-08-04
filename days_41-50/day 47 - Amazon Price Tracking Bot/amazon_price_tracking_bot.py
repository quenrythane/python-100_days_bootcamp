from bs4 import BeautifulSoup
import requests as req
import lxml

PRODUCT_URL = "https://www.amazon.de/-/en/Marvel-Heroes-Guardians-Avengers-Spaceship/dp/B098425PT1/ref=sr_1_3?crid=1DNXDPGYT6HC8&keywords=guardians+of+the+galaxy+lego&qid=1659636947&sprefix=guardians+of+the+galaxy+leg%2Caps%2C146&sr=8-3"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7"
}

response = req.get(PRODUCT_URL, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
print(price)

