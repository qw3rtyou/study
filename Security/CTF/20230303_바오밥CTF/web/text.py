import requests

url="http://43.201.15.137/api/message"
response=requests.post(url)

print(response)