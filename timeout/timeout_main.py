from icecream import ic
import requests
import time

url = 'http://httpbin.org/get'

proxies = {
    'http': 'http://91.227.47.243:8081',
    'https': 'http://91.227.47.243:8081'
}
start = time.perf_counter()
ic(start)
try:
    requests.get(url=url, proxies=proxies, timeout=1)
except Exception as _ex:
    print(time.perf_counter() - start)
    ic(_ex)