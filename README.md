# web_scraping
Курс Веб скрапинга на Stepik

## Примеры заголовков (headers)

### Вариант 1

Запрос
> import requests
> response = requests.get(url='http://httpbin.org/user-agent')
> print(response.text)

Ответ
> {"user-agent": "python-requests/2.27.1"}

### Вариант 2

Запрос

Для того чтобы замаскировать свой запрос под запрос браузер, будем использовать .get() запрос с именованным атрибутом и передадим словарь headers
> import requests

> response = requests.get(url='http://httpbin.org/user-agent')

> print(response.text)

Ответ
> {"user-agent": "python-requests/2.27.1"}

### Вариант 3

Запрос

Этот код последовательно подставляет user-agent из файла и делает запрос на наш url. Обратите внимание, что в это примере использовался модуль random и его метод choice для случайного выбора user_agent из файла.
> import requests

> from random import choice

> url = 'http://httpbin.org/user-agent'

> while line := open('user_agent.txt').read().split('\n'):
    user_agent = {'user-agent': choice(line)}
    response = requests.get(url=url, headers=user_agent)

>print(response.text)