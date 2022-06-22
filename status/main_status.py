import requests
import time


for i in range(1, 501):
    url = f'https://parsinger.ru/task/1/{i}.html'
    r = requests.get(url)
    if r.status_code != 200:
        time.sleep(1)
        print(url, r.status_code)

    else:
        print(url)