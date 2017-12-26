from bs4 import BeautifulSoup
import requests
import pprint
import re

all_p_text = []
f = open('data.txt')

line = f.readline()
all_url = []
while line:
    line = f.readline()
    all_url.append(str(line))

f.close()

correct_all_url = all_url[:len(all_url)-1]
for url in correct_all_url:

    html = requests.get(url.replace('\n', ''))
    soup = BeautifulSoup(html.text, 'html.parser')
    ps = soup.find_all('p')

    for p in ps:
        pre_p_text = re.sub(r'\u3000', '', p.text)
        p_text = re.sub(r'\n', '', pre_p_text)
        if len(p_text) >= 40:
            if '。' in p_text:
                all_p_text.append(p_text)


with open('p_data.txt', 'w') as file:
    for p in all_p_text:
        file.write(p + '\n')

file.close()

# # pp = pprint.PrettyPrinter(indent=1)
# #
# # pp.pprint(all_p_text)
