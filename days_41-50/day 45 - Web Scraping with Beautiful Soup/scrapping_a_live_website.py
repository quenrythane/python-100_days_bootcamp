from bs4 import BeautifulSoup
import requests as req

ycombi_url = "https://news.ycombinator.com/"
response = req.get(ycombi_url)
