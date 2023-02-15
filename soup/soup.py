from bs4 import BeautifulSoup
#<<<<<<< HEAD
# import lxml
#import requests

#response = requests.get(url='https://parsinger.ru/html/index1_page_1.html')
#soup=BeautifulSoup(response.text, 'xml')
#=======
import requests
#import lxml

# Пример 3. Передача объекта response прямо из запроса
file = open('index.html', encoding='utf-8')
soup = BeautifulSoup(file, 'xml')

#>>>>>>> soup
print(soup)
