import requests

url = 'https://api.salon-love-forever.ru/items/category/wedding?active=true&_limit=10'
response = requests.get(url=url).json()
lines = []
for item in response:
    lines.append([item['id'], item['name'], 'api.salon-love-forever.ru' + item['photo_main']['url']])
with open("item.txt", "w") as write_file:
    for line in lines:
        print(line)
        write_file.write(str(line) + '\n')
def get_data():
    myfile = open('item.txt', 'r')
    data = myfile.read()
    return data

# TODO Переделать цикл на for
while True:
    line = get_data().readline()
    if not line:
        break
    r = requests.get(line.strip())
    if r.status_code !=200:
        print(line, r.status_code)

