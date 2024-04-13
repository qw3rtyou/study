# BeautifulSoup
[[CSS Selector]]
request로 얻은 데이터에서 필요한 정보만 산출하는 라이브러리

---
# 원하는 태그 선택하기

soup.select는 해당 되는 태그가 하나라도 리스트를 반환한다.
만약 리스트가 아니라 그 값만 얻고 싶다면 soup.select_one메소드를 사용하면 된다.

```python
from bs4 import BeautifulSoup as bs
import requests            

#티비랭킹닷컴: https://workey.codeit.kr/ratings
page=requests.get("https://workey.codeit.kr/ratings").text
soup=bs(page,'html.parser')    #파서로 데이터를 분석,정리하고 그 결과를 soup에 담음
print(soup.prettyify())    #tap문자 같은걸 추가해서 전체 코드를 이쁘게 보여줌
print(soup.select('tagname'))    #해당 태그를 출력함
print(soup.select('table'))

program_title_tags=soup.select('td.program')

program_titles=[]

for tag in program_title_tags:
	program_titles.append(tag.get_text())    #태그의 텍스트를 추출함

print(program_titles)
```



# 슬라이싱, 인덱싱
슬라이싱, 인덱싱도 가능하다 또한 soup가 아닌 일반 태그에서도 가능하다.

```python
td_tags=soup.select('td')[:4]
tr_tag=soup.select('tr')[1]
td_tags=tr_tag.select('td')
```


# find 와 find_all
find()는 select_one()과 비슷하고, find_all()은 select()와 비슷

```python
soup.find_all('tagname')
soup.find_all(['tagname1', 'tagname2'])
tag.find_all(True)    #모든 태그 찾기
soup.find_all('p', id="some-id", class_="some-class")
#class는 예약어여서 _class로 사용해야됨
soup.find_all('p', id=True, class_=False)
```


# 태그에서 텍스트 빼오기
기본적으로 사용하는 get_text() 말고
strings, stripped_strings가 있음

```python
print(list(tag.strings))
print(list(tag.stripped_strings))
```


# 태그에서 속성 빼오기
태그의 속성 안에는 웹사이트 주소나 이미지 주소같은 유의미한 데이터가 많음
태그의 모든 속성은 사전 형태로 저장되어있음

```python
soup.select_one('img')['src']

>>/images/img.png

soup.select_one('img').attrs

>>{'src':'/images/img.png','id':'qwertyou'}
```


# Beautiful Soup 간결하게 쓰기

#### .tagname 문법
```python
soup.tagname # soup.select_one('tagname')과 동일
tag.tagname # tag.select_one('tagname')과 동일
```


#### 메소드 체이닝
메소드 체이닝은 메소드의 리턴값을 변수에 저장하지 않고, 
리턴값에 바로 또 다른 메소드를 호출하는 것을 뜻함

```python
div_tag = soup.select_one('div.data')
keyword = div_tag.div.p.b.get_text()    #메소드 체이닝
print(keyword)
```


# 데이터를 액셀 파일로

```python
import requests
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook

wb=Workbook(write_only=True)    #워크북 생성
ws=wb.create_sheet('TV Ratings')    #워크시트 생성
ws.append(['순위','채널','프로그램','시청률'])    #인덱스row추가

page=requests.get("https://workey.codeit.kr/ratings/index").text

soup=bs(page,'html.parser')
for tr_tag in soup.select('tr')[1:]:    #보통 table의 첫 tr태그는 th일 확률이 있음 이런 경우 슬라이싱해야댐
	td_tags=tr_tag.select('td')
	row=[
		td_tags[0].get_text(),
		td_tags[1].get_text(),
		td_tags[2].get_text(),
		td_tags[3].get_text()
	]

wb.save('시청률.xlsx')    #워크북 저장, 확장자 xlsx 잊지말기
```



# 데이터를 csv 파일로
```python
import csv
csv_file = open('file_name.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow([data1, data2, ...])    # CSV 파일에 행 추가
```
