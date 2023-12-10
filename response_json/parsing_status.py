import requests
import time
file1 = open("item", "r", encoding='utf_8')

while True:
    line = file1.readline()
    if not line:
        break
    r = requests.get(line.strip())
    if r.status_code !=200:
        print(line, r.status_code)