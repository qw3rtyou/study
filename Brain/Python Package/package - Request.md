웹사이트의 패킷 내용을 가져올 수 있는 라이브러리

```python
import requests

response=requests.get("https://fancyurl.com")
print(response.text)

rating_pages=[]
#https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0
for i in range(5):
	url="https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex={}".format(i)
	rating_page=requests.get(url).text
	rating_pages.append(rating_page)

print(rating_pages)
```
