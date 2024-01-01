[[Python Package]]
[[virtualenv]]
[[OOP - Python]]
[[Algorithm - Python]]

# print()
1. 형식지정자 이용
(1) 소수점 표현
	print('%.nf' %number) number의 소수점 n+1번째 자릿수에서 반올림해서 소수점 n번째 자릿수까지 출력
	ex) print('%.2f' %0.256)

(2) 일반 변수
	print("현재 위치는 %d 입니다."%(cur))

(3)string.format()
	print("hello {}!".format(some_user.name))

2. 매개변수 end
기본적으로 print() 줄바꿈이 들어있다.

	print("줄바꿈은 싫어!", end='')


# 다차원 리스트 정렬
1. 기본적인 정렬

	list.sort()
	list=list.sorted()

2. 비교하는 키함수를 만들어서 정렬

```python
from functools import cmp_to_key

def cmp(a,b):
	if a[0] == b[0]:
		return a[1] < b[1]
	else:
		return a[0] < b[0]

list=[[1,2][2,3][3,5][1,4]]

list=sorted(list,key=cmp_to_key(cmp))
```


3. lambda함수 사용

	list=sorted(list,key=lambda x: (x[0], x[1]))
	list=sorted(list,key=lambda x: (x[0], -x[1]))	

이러면 내림차순인데 -연산자가 안되는 자료형이면 불가능



# defualtdict
주어지는 키가 없다면 오류를 일으키는 기존 딕셔너리와는 달리 자동으로 생성하고
지정한 비어있는 자료형을 바로 할당한다.

```python
from collections import defaultdict
graph = defaultdict(list)
for i in range(n):
	s, e = map(int, input().split())
	graph[s].append(e)
	graph[e].append(s)
```


# lambda 함수
런타임 중 사용하다 버리는 익명함수
리턴문x
변수에 할당할 필요x

1. 형태
	g=lambda x:x**2
	g=lambda x,y:x**2+y
	def inc(n):
		return lambda x:x+n

2. 응용
	map(func,iterable,...)
	filter(func,iterable)
	reduce()



# iterator,iterable,generator
### 요약
기본자료형들은 iterable를 상속받고 있다
iter(iterable)을 통해서 iterator들을 얻을 수 있다.
이러한 iterator들은 각각의 독립적인 상태를 얻고
next(iterator)는 순회할때마다 상태에 맞는 값을 반환해준다
iterable은 무한한 자판기, iterator는 거기서 나오는 음료와 같아서
iterator는 한 번 순회하면 버려짐
그러나 이러한 iterable과 iterator의 분리는 모듈화를 의미하지만
용도의 비해 과한 코드량을 요한다
이때 사용하는게 yeild를 사용하는 generator
generator의 장점은 미리 반환할 값들을 만들어 메모리에 적재하는게 아닌
그저 생성자이기 때문에 적은 양의 데이터를 다룰 땐 손해보지만
매우 큰 데이터를 다루는데는 매우 유리하기 때문에 사용한다.
	
### ABC(abstract base class)
기본자료형(list,tuple,set,dict) 모두 iterator
collections.abc 에 Container,Collection,Sequence 이렇게 3개가 뼈대
기본자료형은 모두 추상 클래스 Collection을 상속받음
기본자료형은 또한 iterable을 상속받고 iterator,generator를 받지 않음

### iterable
iterable은 기본자료형,파일,문자열 등 순회할 수 있는 모든 객체를 말함

```python
assert issubclass(str,iterable)
assert issubclass(io.TextIOWrapper,iterable)
```

즉, for에 넣을 수 있는 모든 객체 range()도 iterable이다.

조건은_iter_추상 메소드가 구현되어 있어야하고, 
호출될 때 마다 새로운 iterator가 반환되어야함

```python
print(iterable._abstractmethods_)
>>>frozenset({'_iter_'})
```

### iterator
iterator는 상태를 유지하며 반환할 수 있는 마지막까지 
원소를 하나씩 반환하는 객체를 말한다.
각 iterator는 서로 다른 상태를 유지한다.
	
```python
	assert iter(i)!=iter(i)
```
	
조건은 _iter_를 구현하되, 자기 자신을 반환해야하고(왜 있어야하는지 모르겠음)
_next_를 구현해서 next(iterator)에 대한 다음 값을 정의해야함

```python
print(iterator._abstractmethods_)
>>>frozenset({'_next_'})
```

### iterable, iterator 만들기

```python
from random import randint
	
class RandomIntIterable:
	def _init_(self,n):
		self.n=n
	
	def _iter_(self):
		return RandomIntIterator(self.n)

class RandomIntIterator:
	def _init_(self,n):
		self.count=0
		self.n=n
		
	def _iter_(self):
		return self
		
	def _next_(self):
		if self.count<self.n:
			self.count+=1
			return randint(1,100)
		else:
			raise StopIteration
```
	

### iterable과 iterator의 상속관계
iterator는 iterable을 상속받는다(자식 클래스이다)

```python	
print(issubclass(iterator,iterable))
>>True
```

역은 성립안함

### generator
iterator와 iterable의 기능을 합쳐 놓은 것
사실상 generator를 사용하는 빈도가 높음(복잡한 구현에선 아님)
앞선 두 클래스와 마찬가지로 collections.abc에 저장되어있음

##### yield를 사용한 생성
```python
from random import randint

def random_number_generator(n):
	count=0
	while count<n:
		yield randint(1,100)
		count+=1
```

		
generator는 클래스가 아닌 함수로 정의한다
return문 x
확실히 한 요소에 담아서 코드량이 현저히 줄어들었다

##### Generator comprehension을 통한 생성
[]를 이용한 comprehension은 list를 생성
()를 이용한 comprehension은 generator를 생성한다

```python
from random import randint
g=(randint(1,100) for _ in range(5))
```

매우 간단하게 만들 수 있지만 구체적은 구현을 힘들거나 불가능하다.
		
### 3가지 클래스의 상속관계
iterable>iterator>Generator
	
### 실전응용
```python
print(sum([n**2 for n in range(1,11)]))보단
print(sum((n**2 for n in range(1,11)))이 성능이 좋고
print(n**2 for n in range(1,11))
```
어떤 함수의 유일한 인자라면 expression의 ()를 생략해도 된다.
	


# 객체 분석하기
1. dir(object)
dir()는 해당 객체에서 선언된 매직메소드나 일반 메소드를 보여주는 함수이다
dir(list)

2. object.mro()
mro()는 상속의 구조를 확인할 수 있다

3. object.\_\_class\_\_()

# 파이썬에서의 언더스코어(\_)
1. 인터프리터에서 사용
파이썬에서 마지막에 실행된 결과값이 _라는 변수에 저장됨

\>> 10
10
\>> _
10
\>> _ * 3
30
\>> _ * 20
600

2. 값을 무시

```python
# 언패킹시 특정값을 무시
x, _, y = (1, 2, 3) # x = 1, y = 3

# 여러개의 값 무시
x, *_, y = (1, 2, 3, 4, 5) # x = 1, y = 5

# 인덱스 무시
for _ in range(10):
	do_something()

```

3. private한 클래스,함수,변수,메서드를 선언
_single_leading_underscore
이런식으로 앞에 언더스코어를 사용하면 외부에서

	from module import *

로 임포트 시 _로 시작되는 것들은 임포트에서 무시된다.
그러나 완전한 private는 아니기에 무시하고 호출하면 되긴된다.
	
4. 파이썬 키워드(c에서의 예약어)와의 충돌을 회피
single_trailing_underscore_
마지막에 \_를 붙여 키워드와의 충돌을 피한다.

5. 클래스간 속성명의 충돌을 방지
\__double_leading_underscores
앞에 언더스코어를 두 번 사용한다.
더블 언더스코어는 클래스 속성명을 맹글링하여 
클래스간 속성명의 충돌을 방지하기 위한 용도로 사용된다.
맹글링이란, 컴파일러나 인터프리터가 변수/함수명을 그대로 사용하지 않고
일정한 규칙에 의해 변형시키는 것을 말한다.
여기선 속성명 앞에 _클래스이름 을 결합하는 방식이다.
즉, ClassName이라는 클래스에서 \__method라는 메서드를 선언했다면 
_ClassName__method로 맹글링

6. 스페셜 변수, 매직 메서드
\__double_leading_and_trailing_underscores__
앞뒤로 언더스코어를 두 번씩 사용한다.
\__init__, \__len__와 같은 메서드가 있다.
이런 형태의 메서드들은 특정한 문법적 기능을 하거나 특정한 일을 한다.
	
7. 국제화(i18n)/지역화(l10n) 함수로 사용되는 경우
음.. 잘모르겠다.. 패스..



# ternary expression
간단한 if문을 한줄로 표현가능
condition_string = "nice" if condition else "not nice"



# list comprehension
for문을 한 줄로 표현 가능

```python
int_list = [1, 2, 3, 4, 5, 6]
	squares = [x**2 for x in int_list]

print(squares)               # [1, 4, 9, 16, 25, 36]

```

# zfill
문자열을 최소 몇 자리 이상을 가진 문자열로 변환시켜줌
이때 만약 모자란 부분은 왼쪽에 “0”을 채워줌
설정된 자릿수보다 이미 더 긴 문자열이라면 그 문자열을 그대로 출력함

```python
print("1".zfill(6))
print("333".zfill(2))
print("a".zfill(8))
print("ab".zfill(8))
print("abc".zfill(8))

000001
333
0000000a
000000ab
00000abc
```


# 모듈
모듈(module)이란 변수, 함수, 클래스 등을 모아놓은 파일
모듈은 다른 곳에서 가져다 쓸 수 있음

	from 모듈의 이름 import 불러올 변수/함수/클래스 이름

모듈의 이름에는 파일명에서 확장자명(.py)을 뺀 이름
모듈에 정의된 모든 것들을 사용하려면 *

### 모듈 별명 지어주기(aliasing)
as 는 조사가 아닌 aliasing의 준말임

	import numpy as np
	array=np.full(6,0)

### 모듈안에 모듈..
모듈안에 모듈이 있을 수 있다. 온점으로 구분하면 됨

	from numpy.random import random
	from matpolotlib.pyplot as plt



# randint, uniform
모두 random 모듈에 있다.

```python
	from random import randint
		x = randint(1, 20)
		# 1 <= N <= 20를 만족하는 랜덤한 정수(난수) N을 리턴
		
	from random import uniform
		x = uniform(0, 1)
		# 0 <= N <= 1을 만족하는 랜덤한 소수(난수) N을 리턴
```


# 가변타입 불변타입
인스턴스의 속성 변경 가능, 변경 불가 차이
가변타입	list dict + 직접 작성하는 클래스
불변타입	bool int float str tuple
불변타입의 원소를 바꾸려면 원소 하나씩 바꾸는게 아니라 인스턴스 자체를 바꿔야함



# 문자열이 숫자인지 문자인지 판별하기
string.isdigit()은 string이 숫자인지를 불린으로 리턴하는 함수
유니코드는 true 음수는 false를 리턴한다.



# 문자열 메소드
STRING.strip()
    문자열 양쪽 공백 제거

STRING.split(SPLITER)
구분자로 구분된 문자열을 iterator로 반환

	phone_number.split("-")[2]
	name,extension=file_name.split(".")

SPLITER.join(LIST)
여러 문자열 합치기

	phone_number_segments = ["010", "0000", "1111"]
	print("-".join(phone_number_segments))

STRING.replace(BEFORE_STRING,AFTER_STRING)
문자열의 일부분을 다른 문자열로 바꾸기

	message.replace("Codeit", "코드잇")

STRING.lower,upper,capitalize
소문자화,대문화,앞글자만 대문자

STRING.find(SUBSTRING)
문자열에서 부분문자열 찾기
-1 나오면 없음

STRING.count(SUBSTRING)
문자열에서 부분문자열 몇 번 나오는지 카운트

SUBSTRING IN STRING
부분문자열이 분자열에 있는지 불린 형식으로 리턴

STRING.endswith(SUBSTRING), startswith(SUBSTRING)
문자열이 부분문자열로 끝나는지 불린 형식으로 리턴

STRING.isalpha(SUBSTRING), isalnum(SUBSTRING), isdigit(SUBSTRING)

isalpha()
	특수문자나 숫자 공백이 문자열에 들어가 있으면 FALSE 아님 TRUE

isalnum()
	alpha+num

isdigit()
	모두 숫자로 이뤄져 있는지 불린 형식으로 리턴



# datetime 모듈
파이썬에서 날짜와 시간 데이터를 다룰 때는 datetime 모듈을 많이 사용
datetime 객체 자체로 날짜와 시간을 더하고 빼는 등의 연산 가능
원하는 포맷으로 출력 가능

```python
import datetime

birth_day=datetime.datetime(2020,11,22)
print(birth_day)

now=datetime.datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

print(now.date())
print(now.time())

#대소문자 구분 잘할 것
now_date=now.strftime("%Y/%m/%d")
print(now_date)

now_time=now.strftime('%H시 %M분 %S초')
print(now_time)
```

포멧코드표
	포맷코드	설명	예
	%a	요일 줄임말	Sun, Mon, ... Sat
	%A	요일	Sunday, Monday, ..., Saturday
	%w	요일을 숫자로 표시, 월요일~일요일, 0~6	0, 1, ..., 6
	%d	일	01, 02, ..., 31
	%b	월 줄임말	Jan, Feb, ..., Dec
	%B	월	January, February, …, December
	%m	숫자 월	01, 02, ..., 12
	%y	두 자릿수 연도	01, 02, ..., 99
	%Y	네 자릿수 연도	0001, 0002, ..., 2017, 2018, 9999
	%H	시간(24시간)	00, 01, ..., 23
	%I	시간(12시간)	01, 02, ..., 12
	%p	AM, PM	AM, PM
	%M	분	00, 01, ..., 59
	%S	초	00, 01, ..., 59
	%Z	시간대	대한민국 표준시
	%j	1월 1일부터 경과한 일수	001, 002, ..., 366
	%U	1년중 주차, 월요일이 한 주의 시작으로	00, 01, ..., 53
	%W	1년중 주차, 월요일이 한 주의 시작으로	00, 01, ..., 53
	%c	날짜, 요일, 시간을 출력, 현재 시간대 기준	Sat May 19 11:14:27 2018
	%x	날짜를 출력, 현재 시간대 기준	05/19/18
	%X	시간을 출력, 현재 시간대 기준	'11:44:22'



# 인터프리터 명시적으로 정하기
스크립트 파일의 첫 줄에 주석으로 작성되는 특별한 구문
shebang이라고 함

#!/usr/bin/env python3

스크립트를 실행할 때 사용할 인터프리터를 지정
다음과 같이 일반 elf 실행하듯 사용할 수 있다.

$ chmod +x script.py
$ ./script.py


# 파일 입출력



# deque


# global
파이썬에서는 기본적으로 함수 내부에서 선언된 변수는 지역 변수(local variable)로 취급되며 해당 함수 내에서만 사용할 수 있음
반대로 함수 외부에서 선언된 변수는 전역 변수(global variable)로 취급되며 프로그램 어디서든 사용할 수 있음
그런데 함수 내부에서 전역 변수를 수정하려고 할 때는 'global' 키워드를 사용하여 해당 변수가 전역 변수임을 명시해야 합니다. 그렇지 않으면 파이썬은 해당 변수를 새로운 지역 변수로 취급하게 됨

중요한 점은, 가변타입, 불변타입 여부에 따라 객체가 참조에 의한 전달을 하기 때문에, 함수 내부에서 리스트를 변경할 때는 그 변경 사항이 원본 객체 적용되지만 반대는 숫자는 불변 타입이므로 함수 내부에서 수정을 하려면 반드시 global을 사용해야 함

한 가지 더 생각해볼 것은, 이는 **변경**할 때 문제가 생기는 것이기 때문에  단순 참조는 `global`을 필요로 하지 않음


# 오류

코드 내에 한글이 있다면 인코딩 오류남
```python
#-*- coding: utf-8 -*-
```


