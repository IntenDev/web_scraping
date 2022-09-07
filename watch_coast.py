from bs4 import BeautifulSoup
import requests
import lxml
url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = [i.text for i in soup.find_all('p', 'price')]
result = 0
for i in div:
    result += int(i.partition(' ')[0])
print(result)