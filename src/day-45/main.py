#web scraping

from bs4 import BeautifulSoup
import requests

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup)
# # print(soup.title)
# # print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))


response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_texts = []
article_links = []
article_tag = soup.find_all(name="span", class_="titleline")
for article in article_tag:
    text = article.find(name="a").getText()
    article_texts.append(text)
    link = article.find(name="a").get("href")
    article_links.append(link)

article_upvotes = [ int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)

largest_number = max(article_upvotes)
largest_num_index = article_upvotes.index(largest_number)

print(article_texts[largest_num_index])
print(article_links[largest_num_index])