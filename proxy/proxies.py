import requests

# Библиотека Requests позволяет отправлять запросы скрывая свой настоящий IP адрес. Очень часто можно получить бан за
# высокочастотные запросы.
url = 'http://httpbin.org/ip'
proxy = {
    'http': 'http://103.177.45.3:80',
    'https': 'http://103.177.45.3:80',

}

response = requests.get(url=url, proxies=proxy)
print(response.json())


# --------------------------------------
# Для socks4
proxy_socks4 = {
    'http':'socks4://103.177.45.3:80',
    'https':'socks4://103.177.45.3:80',

}
# --------------------------------------
# Для socks5
proxy_socks5 = {
    'http':'socks5://103.177.45.3:80',
    'https':'socks5://103.177.45.3:80',
}


# --------------------------------------
# Для всех, с авторизацией
proxy_all_auth = {
    'http':'socks5://login:password@103.177.45.3:80',
    'https':'socks5://login:password@103.177.45.3:80',
}