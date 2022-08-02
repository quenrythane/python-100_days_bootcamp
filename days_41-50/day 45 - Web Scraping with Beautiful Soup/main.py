from bs4 import BeautifulSoup
import lxml

with open('website.html', encoding="utf8") as html_file:
    contents = html_file.read()

soup = BeautifulSoup(contents, 'lxml')  # instead of lxml i could use html.parser

print(soup.title)
print(soup.title.name)
print(soup.title.string)
