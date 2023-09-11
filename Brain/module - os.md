운영체제에서 제공되는 여러 기능을 파이썬에서 수행하게 해줌

```python
import os

##운영체제 이름 출력 윈도우는 nt
print(os.name)
```

# 파일 용량 접근

```python
size=os.path.getsize("os_print_os_name.py")

#1000byte=1kb
#1000kb=1mb
def byte_to_mb(size):
return size//1000000

print("용량: {}MB".format(byte_to_mb	mb(size)))
```

# 파일 속성 접근
```python
import datetime

path = 'os_print_os_name.py'

# 타임스탬프 형식의 생성 시간
# 예시: 1594616754.1851065
creation_time = os.path.getctime(path)
modify_time = os.path.getmtime(path)
access_time = os.path.getatime(path)

# datetime 모듈을 사용해서 보기 좋게 변경하기
# 예시: 2020-06-19 14:26:52.981000
format_creation_time = datetime.datetime.fromtimestamp(creation_time)
format_modify_time = datetime.datetime.fromtimestamp(modify_time)
format_access_time = datetime.datetime.fromtimestamp(access_time)

# 문자열과 함께 출력하고 싶다면 format을 사용
print("{} 생성 시각: {}".format(path,format_creation_time))
print("{} 수정 시각: {}".format(path,format_modify_time))
print("{} 참조 시각: {}".format(path,format_access_time))
```

# 파일 내용 접근
```python
file=open("os_check_file_5mb.py",encoding='UTF-8')
#파이썬은 기본적으로 인코딩을 ANSI로 함
#파일을 ANSI로 인코딩해주거나
#위에처럼 인코딩을 따로 지정해줘야함

print(file.readline())
print(file.readline())

file.seek(0)    #파일 커서 처음으로 옮기기
print(file.read())

file.seek(0)    #파일 커서 처음으로 옮기기
print(file.readlines())

file.close()
```

# 파일 생성, 삭제, 수정, 이름변경
```python

with open("data/generatedfile1",'w',encoding='UTF-8') as file:
pass

with open("data/generatedfile2",'w',encoding='UTF-8') as file:
pass

with open("data/generatedfile3",'w',encoding='UTF-8') as file:
pass

import os

os.rename("data/generatedfile1","data/dummyfile")
os.remove("data/generatedfile2")

#파일 내용 편집
with open("data/text1.txt",'a',encoding='UTF-8') as file:
file.write("helpme")
```


# r,w,a 모드 동시에 사용
위에 방법대로 한다면 rwa모드를 동시에 사용하려면 파일을 다른 파일 디스크립터로
여러 번 열어야 한다는 불편함이 있을 수 있다.
이를 위해, r+,w+,a+ 등으로 여러 모드를 동시에 사용 가능하다.

with open("data/text1.txt",'w+',encoding='UTF-8') as file:
file.write("fku")
file.read()

r,w,a,+모드 차이 정리
![[r,w,a,+모드 차이 정리.png]]

# 파일 확장자 분리
```python
import os

file = 'codeit.report.pdf'
filename, extension = os.path.splitext(file)
```
