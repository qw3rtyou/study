# input()보다 더 빨리 입력받기
import sys
sys.stdin.readline()


# 최대공약수, 최소공배수 최적화(유클리드 호제법)
1. 최대공약수(GCD)
	while 나머지가 0이 될때까지
		a=a%b
		a,b=b,a

2. 최소공배수
	a*b/(최대공약수)

	xref:백준2981



# 소수 최적화(에라토스테네스의 체 알고리즘)
k 이전까지의 소수 모두 구하기
sieve=[True]*(k+1)

### 에라토스테네스의 체 알고리즘 적용
for i in range(2, int(k**.5)+1):
    if sieve[i]:
        for j in range(i+i, k+1, i):
            sieve[j]=False

### k 이상의 첫 번째 소수 반환
for i in range(k, len(sieve)):
    if sieve[i]:
        return i


# map(),split()
한 번에 여러 값을 입력받을 때 변수에 바로 할당하는 방법으로

a,b=map(int,input().split())

이런 식으로 많이 사용함
입력받은 문자열을 딱히 가공할 필요없이 스플릿만 해야한다면 
굳이 map을 사용할 필요가 없음

1. split(구분자,분할횟수)
	문자열을 입력받은 규칙으로 짤라서 리스트를 반환함

2. map(func,iterable)
	iterable을 한번씩 호출하면서 func을 적용하고 난 값들을 map 객체로 반환함
	(잘은 모르겠지만 for문에 잘들어가는 걸 보니 iterator를 반환하는 것 같다..)
	func는 일반함수 타입함수 람다함수 모두 사용가능


# 재귀제한하기

```python
sys.setrecursionlimit(10**8)
```


# 2차원배열생성

```python
b[["init" for _ in range(n)] for i in range(m)]
b=[["init"]*n]*m
```



# dict.items()
dict에서 사용하는 메소드 items()은 defaultdict에서도 사용가능하다.
그냥 dict을 사용하여 접근하는 것과 dict.items()을 사용해 접근하는 것에는
분명한 차이가 있다
일반 dict로 key,value를 접근하고 싶다면 별도의 함수를 사용해야한다

```python
Dictionary1 = { 'A': 'Geeks', 'B': 4, 'C': 'Geeks' }
Dictionary1.values()
>>>dict_values(['Geeks', 4, 'Geeks'])
```

그러나 dict.items()는 key와 value를 투퓰로 묶인 list를 반환해준다.

```python
Dictionary1.items()
>>>dict_items([('A', 'Geeks'), ('B', 4), ('C', 'Geeks')])
```


# 파이썬 내장함수 시간복잡도
Operation			Average Case	Amortized Worst Case
Copy				O(n)			O(n)
Append[1]			O(1)			O(1)
Pop last			O(1)			O(1)
Pop intermediate[2]	O(n)			O(n)
Insert				O(n)			O(n)
Get Item			O(1)			O(1)
Set Item			O(1)			O(1)
Delete Item			O(n)			O(n)
Iteration			O(n)			O(n)
Get Slice			O(k)			O(k)
Del Slice			O(n)			O(n)
Set Slice			O(k+n)			O(k+n)
Extend[1]			O(k)			O(k)
Sort				O(n log n)		O(n log n)
Multiply			O(nk)			O(nk)
x in s				O(n)	
min(s), max(s)		O(n)	
Get Length			O(1)			O(1)



# 질문 or 생각해볼거리
각 복잡도가 얼마나 큰 수 인지 어떻게 알 수 있는지
예를들어 
0.75초 만에, 256MB 메모리 제한이 있을 때 이 코드가 문제를 해결할 수 있는가?
라는 질문에 답을 할 수 있는 기준이 뭔지.


# 그래프구현
# collections
