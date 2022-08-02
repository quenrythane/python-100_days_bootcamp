from bs4 import BeautifulSoup
import lxml

with open('website.html', encoding="utf8") as html_file:
    contents = html_file.read()

soup = BeautifulSoup(contents, 'lxml')  # instead of lxml i could use html.parser

print(soup.title)  # <title>The HTML5 Herald</title>
print(soup.title.name)  # title (tag name)
print(soup.title.string)  # The HTML5 Herald
print()

# .find <- find fisrt atribute with name
# .find_all <- find all atributes match the query
all_links = soup.find_all('a')
print(all_links)
for link in all_links:
    print(f"{link.string} - {link['href']}")
    # print(f"{link.getText()} - {link.get('href')}")
print()

heading = soup.find(name='h1', id='name')
print(heading, heading.string)
print()

find_class = soup.find_all(class_='heading')
print(find_class)
print(find_class[0].get('class'))
print()


