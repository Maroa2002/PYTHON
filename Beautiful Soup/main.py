from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
articles_text = []
article_links = []
for article in articles:
    text = article.getText()
    articles_text.append(text)
    link = article.get("href")
    article_links.append(link)
article_upvote = [int(soup.getText().split()[0]) for soup in soup.find_all(name="span", class_="score")]
max_index = max(article_upvote)
print(articles_text)
print(article_links)
print(article_upvote)
print(max_index)























# with open("website.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.a)
