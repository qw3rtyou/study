numerical python의 준말
숫자와 관련된 파이썬 도구
numpy 배열은 일반적인 list와 유사하지만 ds를 다루는데 적합한 자료형임
list와의 차이점은 속도가 훨씬 빠르고, 간단하지만 같은 자료형만 넣어야 하는 단점이 있다.

```python
import numpy
array1=numpy.array([2,3,5,7,11,13,17,19,23,31])
array1
>>array([ 2,  3,  5,  7, 11, 13, 17, 19, 23, 31])

array2=numpy.array([[1,2,3,4,],[5,6,7,8,],[9,10,11,12]])
type(array2)
>>numpy.ndarray
array2
>>array([[ 1,  2,  3,  4],
[ 5,  6,  7,  8],
[ 9, 10, 11, 12]])
array2.shape
>>(3, 4)
array2.size
>>12
```



# numpy array를 만드는 다양한 방법
numpy 모듈의 array 메소드에 파라미터로 리스트를 넘겨주면 됨

```python
array1 = numpy.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])

#numpy 모듈의 fill 메소드를 사용하면 모든 값이 같은 numpy array 생성

array2 = numpy.full(6,7)        #[7 7 7 7 7 7]
array3 = numpy.zeros(6, dtype=int)        #[0 0 0 0 0 0]
array4 = numpy.ones(6, dtype=int)        #[1 1 1 1 1 1]

#램덤한 값들을 생성하고 싶다면 numpy 모듈안에 random 모듈의 random 함수를
사용하면 됨

array5 = numpy.random.random(6)
#[0.42214929 0.45275673 0.57978413 0.61417065 0.39448558 0.03347601]

array6 = numpy.random.random(6)
#[0.42521953 0.65091589 0.94045742 0.18138103 0.27150749 0.8450694 ]

#연속된 값들을 생성하고 싶다면 numpy 모듈의 arange 함수를 이용해 생성
#arange() 함수는 range()와 매우 유사하게 동작함

#파라미터가 1개라면 0~m-1까지의 값들이 담긴 numpy array가 리턴됨
#파라미터가 2개라면 n~m-1까지의 값들이 담긴 numpy array가 리턴됨
#파라미터가 3개라면 n~m-1까지의 값들 중 간격이 s인 numpy array가 리턴됨

array7 = numpy.arange(6)    #[0 1 2 3 4 5]
array8 = numpy.arange(2, 7)    #[2 3 4 5 6]
array9 = numpy.arange(3, 17, 3)    #[ 3  6  9 12 15]
```

# numpy 인덱싱/슬라이싱

```python
import numpy as np

arr=np.array([2,3,5,7,5,9,0,4,2,1,2])

arr[2]        5
arr[1]        3

arr[-1]        2
arr[-2]        1

arr[[1,3,6]]        3,7,0

idx=np.array([3,1,2])        

arr[idx]        7,3,5        #numpy array안에 numpy array 넣을 수 있음

arr[2:5]        5,7,5
arr[:5]        2,3,5,7,5
arr[1:4:2]        3,7
```

# numpy 기본연산

```python
import numpy as np

array1=np.arange(10)    #[0,1,2,3,4,5,6,7,8,9]
array2=np.arange(10,20)

array1*2        #[0,2,4,6,8,10,12,14,16,18]

array1*array2    #[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
```

# numpy 불린연산
numpy array에는 불린 값도 넣어 둘 수 있고 연산도 할 수 있다.

```python
import numpy as np

array1=np.array([2,3,5,7,11,13,17,19,23,29,31])
array1>4      

>>array([False,False,True,True,True,True,True,True,True,True,True])

booleans=array1<4         #불린값들이 담긴 numpy array 생성
filter=np.where(booleans)        #참 값의 인덱스를 담아둔 numpy array 생성
filter   

>>(array([ 2,  3,  4,  5,  6,  7,  8,  9, 10]),)

array1[filter]        #인덱스가 적힌 값 출력

>>array([ 5,  7, 11, 13, 17, 19, 23, 29, 31])
```

# numpy 라이브러리의 기본적인 통계 기능
array1.max()    최대값
array1.min()    최소값
array1.mean()    평균
np.median(array2)    중앙값
array1.std()    표준편차
array1.var()    분산

# tip
#### 자주 발생하는 오류
'Series' objects are mutable, thus they cannot be hashed
->인덱싱 할 때 Dataframe에 .loc 붙였는지 확인

#### 대각선 대칭되게 만들기(column이랑 row랑 바꾸기)
대각행렬을 만들면 됨
DataFrame에 .T붙이면 됨

```python
pd.DataFrame([day,samsong_series,hyundee_series],index=['day', 'samsong', 'hyundee']).T
pd.DataFrame([day,samsong_series,hyundee_series],index=['day', 'samsong', 'hyundee']).transpose()
```

#### 컬럼명 출력하는데 ... 대신 전부 출력하고 싶다면
print(df.columns.values)

Notebook에선
df.columns.values

데이터 타입오류
DataFrame을 처음에 생성할 때 설정할 수 있음

```python
museum = pd.read_csv("data/museum_3.csv", dtype={'지역번호': str})
```

#### 이런것도 가능
df.drop() 할 때 

```python
df.drop(df[df['budget']>q3+5*iqr].index,inplace=True)
```

이런 식으로 인덱스의 리스트뿐만 아니라
.index로 나온 값도 사용할 수 있음