from bs4 import BeautifulSoup as bs
import requests

url = 'https://parsinger.ru/html/hdd/4/4_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = bs(response.text, 'lxml')
div = []
div.append(soup.find('span', id='price').text)
div.append(soup.find('span', id='old_price').text)
for i in range(len(div)):
    div[i] = int(div[i].partition(' ')[0])
result = (div[1] - div[0]) * 100 / div[1]
print(result)
