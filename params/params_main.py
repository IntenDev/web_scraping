import requests
from icecream import ic
param= {'active': 1}
r = requests.get('https://api.salon-love-forever.ru/styles/', params=param)
arr = r.json()
for i in range(len(arr)):
    print(arr[i]['id'], arr[i]['name'])

