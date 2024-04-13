# Requests
- HTTP 요청을 보내기 위한 라이브러리
- 세션, HTTP메소드, 콘텐츠 디코딩 등등을 처리할 수 있음

---
# 사용 예시
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

- 리다이렉션 비허용
```python
response = requests.get('http://example.com', allow_redirects=False)
```

- 자동 URL 인코딩 제한
```python
url = 'https://example.com/api?' + urlencode(params, safe='/:')
response = requests.get(url)
```