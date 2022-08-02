from bs4 import BeautifulSoup
import requests as req

ycombi_url = "https://news.ycombinator.com/"
response = req.get(ycombi_url)

soup = BeautifulSoup(response.text, 'lxml')

for link in soup.find_all('a', class_="titlelink"):
    article_title = link.text
    article_url = link['href']
    print(f"{article_title}: {article_url}")
    print()

articles_title = [article.text for article in soup.find_all('a', class_="titlelink")]
articles_url = [article['href'] for article in soup.find_all('a', class_="titlelink")]
articles_upvotes = [article.text.split()[0] for article in soup.find_all('span', class_="score")]
print(len(articles_title), articles_title)
print(len(articles_url), articles_url)
print(len(articles_upvotes), articles_upvotes)  # have a problem because not every article has upvotes
# for now i dont want to spend time on this, instead go forward

# data = [(articles_title[i], articles_url[i], articles_upvotes[i]) for i in range(len(articles_title))]
# print(data)