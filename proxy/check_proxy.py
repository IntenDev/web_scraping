from random import choice
import requests

url = 'http://httpbin.org/ip'

with open('proxy/proxy.txt') as file:
    proxy_file = file.read().split('\n')
    for _ in range(10):
        try:
            ip = choice(proxy_file).strip()
            proxy = {
                'http': f'http://{ip}',
                'https': f'https://{ip}'
            }
            response = requests.get(url=url, proxies=proxy)
            print(response.json(), 'Success connection')
        except Exception as _ex:
            print()
            print(_ex)
            continue