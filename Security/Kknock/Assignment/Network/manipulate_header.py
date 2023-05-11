import requests

# HTTP GET 요청 보내기
url = 'http://20.200.213.238:3737'
headers = {'User-Agent': 'admin','Cookie':'Choi Jeong Won'}
response = requests.get(url, headers=headers)


#url = 'http://127.0.0.1:8888'
#response = requests.get(url)

# 응답 확인
print(response.text)