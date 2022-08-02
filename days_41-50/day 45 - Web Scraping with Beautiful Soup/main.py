from bs4 import BeautifulSoup
import lxml

with open('website.html', encoding="utf8") as html_file:
    contents = html_file.read()

soup = BeautifulSoup(contents, 'lxml')  # instead of lxml i could use html.parser

print("1 titles")
print(soup.title)  # <title>The HTML5 Herald</title>
print(soup.title.name)  # title (tag name)
print(soup.title.string)  # The HTML5 Herald
print()

print("2 links")
# .find <- find fisrt atribute with name
# .find_all <- find all atributes match the query
all_links = soup.find_all('a')
print(all_links)
for link in all_links:
    print(f"{link.string} - {link['href']}")
    # print(f"{link.getText()} - {link.get('href')}")
print()

print("3 specific tag with id")
heading = soup.find(name='h1', id='name')
print(heading, heading.string)
print()

print("4 specific tag with class")
find_class = soup.find_all(class_='heading')
print(find_class)
print(find_class[0].get('class'))
print()

print("5 specific tag with indent attribute")
company_url_one = soup.select_one(selector="p a")  # like .find
# selector is a css selector
# p a means find the first <p> tag with a <a> tag inside
company_url = soup.select(selector="p a")  # like .find_all
print(company_url_one)
print(company_url)
print()

print("6 specific id and class")
id_name_selector = soup.select(selector="#name")
class_heading_selector = soup.select(selector="h1, .heading")  # looks for h1 or .heading
print(id_name_selector)
print(class_heading_selector)


