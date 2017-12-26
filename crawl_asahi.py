import requests
from bs4 import BeautifulSoup


html = requests.get('https://news.google.com/news/headlines/section/topic/NATION?ned=jp&hl=ja&gl=JP')

soup = BeautifulSoup(html.text, 'html.parser')
news = soup.find_all('c-wiz', class_="PaqQNc")

link_holder = []


for article in news:
    a = article.find('a')

    link = a.get('href')

    link_holder.append(link)

with open("./data.txt", 'w') as f:
    for idx in link_holder:
        f.write(idx + '\n')

f.close()
