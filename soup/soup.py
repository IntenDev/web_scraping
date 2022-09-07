from bs4 import BeautifulSoup
import requests


# Пример 3. Передача объекта response прямо из запроса
file = open('index.html', encoding='utf-8')
soup = BeautifulSoup(file, 'lxml')

print(soup)
