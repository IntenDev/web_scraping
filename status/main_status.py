import requests
import time
file1 = open("result.csv", "r", encoding='utf_8')

while True:
    line = file1.readline()
    if not line:
        break
    r = requests.get(line.strip())
    if r.status_code !=200:
        print(line, r.status_code)


















    # time.sleep(1)
    # if r.status_code != 200:
    #     time.sleep(1)
    #     print(line, r.status_code)
    #
    # else:
    #     print(line)

# for i in range(1, 501):
#     url = f'https://parsinger.ru/task/1/{i}.html'
#     r = requests.get(url)
#     if r.status_code != 200:
#         time.sleep(1)
#         print(url, r.status_code)
#
#     else:
#         print(url)