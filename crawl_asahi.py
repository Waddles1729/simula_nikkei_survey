import requests
from bs4 import BeautifulSoup


html = requests.get('http://webronza.asahi.com/free/list.html')

soup = BeautifulSoup(html.text, 'html.parser')
news = soup.find('ul', class_="list")
new = news.find_all('li')

link_holder = []


for article in new:
    link = "http://webronza.asahi.com" + str(article.a.get('href'))

    link_holder.append(link)

with open("./data.txt", 'w') as f:
    for idx in link_holder:
        f.write(idx + '\n')

f.close()
