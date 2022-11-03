from bs4 import BeautifulSoup
# import lxml
import requests

response = requests.get(url='https://parsinger.ru/html/index1_page_1.html')
soup=BeautifulSoup(response.text, 'xml')
print(soup)
