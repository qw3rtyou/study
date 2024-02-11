numpy를 이용해 만듬

# Series
Series는 1차원 array를 다루는 pandas 라이브러리의 고유 자료형
numpy array랑 pandas Series랑 비슷한 기능을 한다고 생각하면 됨

```python
pd.Series(['dongwook', 50, 86]
```

Series는 list로 변환 가능

#### 2차원 배열, numpy array가 아닌 pandas를 쓰는 이유
numpy array에서는 row나 column이 숫자여만 했는데
pandas DataFrame에서는 문자열이나 다른 자료형이어도 상관없음
표 안에 데이터도 숫자만 넣을 수 있던 numpy array와는 달리
pandas DataFrame에서는 다른 자료형이어도 상관없음
그 외에도 외부데이터 읽고 쓰기, 데이터분석, 데이터 정리 등등 다양한 기능이 있음


# DataFrame
표 형식의 데이터를 담는 자료형
가로로 나열되어 있는 줄을 행    row/index    레코드
세로로 나열되어 있는 줄을 열    column        데이터의 특징


#### DataFrame 기본적인 사용법
보통 aliasing으로 pd라고 한다.
```python
import pandas as pd
two_dimensional_list=[['asdf',23,42],['fads',14,89],['poui',53,26]]
my_df=pd.DataFrame(two_dimensional_list, columns=['name','score1','score2'],index=['a','b','c',])

my_df    
#기본적으로 columns나 index를 설정하지 않으면 0,1,2,3 이런식으로 
#기본적으로 설정되기 때문에 이름을 짓고 싶다면 데이터프레임 설정할 때 지어줘야함        
>>
name	score1	score2
a	asdf	23	    42
b	fads	14	    89
c	poui	53	    26

type(my_df)

>>pandas.core.frame.DataFrame

my_df.columns    #데이터프레임의 column 출력

>>Index(['name', 'score1', 'score2'], dtype='object')

my_df.index    #데이터프레임의 row 출력

>>Index(['a', 'b', 'c'], dtype='object')

my_df.dtypes    #데이터프레임의 각각의 컬럼들의 자료형 출력

>>
name      object    #object는 pandas에서 문자열 같은 개념
score1     int64
score2     int64
dtype: object

#int64	정수
#float64	소수
#object	텍스트
#bool	불린(참과 거짓)
#datetime64	날짜와 시간
#category	카테고리

#각각의 컬럼은 서로 다른 자료형을 가져도 되지만
#하나의 컬럼은 무조건 같은 자료형이 담겨야하는 것을 알 수 있음
```


#### From list of lists, array of arrays, list of series
2차원 리스트나 2차원 numpy array로 DataFrame을 만들 수 있음 
심지어 pandas Series를 담고 있는 리스트로도 DataFrame 생성 가능

```python
import numpy as np
import pandas as pd

two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]
two_dimensional_array = np.array(two_dimensional_list)
list_of_series = [
pd.Series(['dongwook', 50, 86]), 
pd.Series(['sineui', 89, 31]), 
pd.Series(['ikjoong', 68, 91]), 
pd.Series(['yoonsoo', 88, 75])
]

# 아래 셋은 모두 동일함
df1 = pd.DataFrame(two_dimensional_list)
df2 = pd.DataFrame(two_dimensional_array)
df3 = pd.DataFrame(list_of_series)

print(df1)

>>
0   1   2
0  dongwook  50  86
1    sineui  89  31
2   ikjoong  68  91
3   yoonsoo  88  75
```



#### From dict of lists, dict of arrays, dict of series
파이썬 사전(dictionary)으로도 DataFrame을 만들 수 있음
사전의 key로는 column 이름을 쓰고, 그 column에 해당하는 리스트, 
numpy array, 혹은 pandas Series를 사전의 value로 넣어주면 됨

```python
import numpy as np
import pandas as pd

names = ['dongwook', 'sineui', 'ikjoong', 'yoonsoo']
english_scores = [50, 89, 68, 88]
math_scores = [86, 31, 91, 75]

dict1 = {
'name': names, 
'english_score': english_scores, 
'math_score': math_scores
}

dict2 = {
'name': np.array(names), 
'english_score': np.array(english_scores), 
'math_score': np.array(math_scores)
}

dict3 = {
'name': pd.Series(names), 
'english_score': pd.Series(english_scores), 
'math_score': pd.Series(math_scores)
}


# 아래 셋은 모두 동일함
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
df3 = pd.DataFrame(dict3)

print(df1)

>>
name  english_score  math_score
0  dongwook             50          86
1    sineui             89          31
2   ikjoong             68          91
3   yoonsoo             88          75
```


#### From list of dicts
리스트가 담긴 사전이 아니라, 
사전이 담긴 리스트로도 DataFrame을 만들 수 있음

```python
import numpy as np
import pandas as pd

my_list = [
{'name': 'dongwook', 'english_score': 50, 'math_score': 86},
{'name': 'sineui', 'english_score': 89, 'math_score': 31},
{'name': 'ikjoong', 'english_score': 68, 'math_score': 91},
{'name': 'yoonsoo', 'english_score': 88, 'math_score': 75}
]

df = pd.DataFrame(my_list)
print(df)

>>
english_score  math_score      name
0             50          86  dongwook
1             89          31    sineui
2             68          91   ikjoong
3             88          75   yoonsoo
```


#### csv(comma seperated values)
보통 첫 줄에 컬림이름들이 나와있는 줄이 있는데 헤더라고 함

```python
import pandas as pd
iphone_df=pd.read_csv('data/iphone.csv')
iphone_df

>>
Unnamed: 0	출시일	디스플레이	메모리	출시 버전	Face ID
0	iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No
1	iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No
2	iPhone 8	2017-09-22	4.7	2GB	iOS 11.0	No
3	iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No
4	iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
5	iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
6	iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes
```


csv 파일의 처음을 자동으로 header로 인식해서 사용함 
그러나 header 없이 바로 데이터가 나오는 경우도 있을 것이다.
그러면 다음과 같이 header가 없음을 설정하면 된다.

```python
iphone_df=pd.read_csv('data/iphone.csv',header=None)
```


또 지금과 같이 가장 왼쪽 부분이 어색한데 가장 왼쪽 컬럼을 row 이름으로
설정하면 된다.

```python
iphone_df=pd.read_csv('data/iphone.csv',index_col=0)
```



#### DataFrame 인덱싱
이전 버전에서는 

```python
iphone_df.loc[:,[True,False,True,True,False]]
```


이런 식으로 문법을 사용하였는데 DataFrame의 row의 값이 10개라면
다시말해 조건으로 건 인덱싱의 개수랑 row의 개수가 다르다면
모자른 개수는 모두 false로 처리하고 초과한 건 무시했는데
현재는 정확히 개수가 맞아야 한다고 함

```python
import pandas as pd
iphone_df=pd.read_csv('data/iphone.csv',index_col=0)

#특정 데이터 인덱싱
iphone_df.loc['iPhone 8','메모리']

>>'2GB'

#특정 row나 column 인덱싱
iphone_df.loc['iPhone 8']    #iphone_df.loc['iPhone 8',:] 랑 동일함

>>
출시일        2017-09-22
디스플레이             4.7
메모리               2GB
출시 버전        iOS 11.0
Face ID            No
Name: iPhone 8, dtype: object


iphone_df.loc[:,"디스플레이"]        #iphone_df["디스플레이"] 랑 동일함

>>
iPhone 7         4.7
iPhone 7 Plus    5.5
iPhone 8         4.7
iPhone 8 Plus    5.5
iPhone X         5.8
iPhone XS        5.8
iPhone XS Max    6.5
Name: 디스플레이, dtype: float64

type(iphone_df.loc[:,"디스플레이"])

>>pandas.core.series.Series    #한줄은 Series 라고 생각하면 됨

type(iphone_df.loc['iPhone 8','메모리'])   

>>str

#index 목록 및 데이터타입 확인
iphone_df.index    
>>
Index(['iPhone 7', 'iPhone 7 Plus', 'iPhone 8', 'iPhone 8 Plus', 'iPhone X',
'iPhone XS', 'iPhone XS Max'],
dtype='object')

#원하는 row를 리스트로 보내주면 여러개 선택가능
iphone_df.loc[['iPhone 8','iPhone 8 Plus']]


#슬라이싱도 가능
iphone_df.loc[['iPhone 8','iPhone 8 Plus']]

>>>
출시일	디스플레이	메모리	출시 버전	Face ID
iPhone 8	2017-09-22	4.7	2GB	iOS 11.0	No
iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No

iphone_df.loc[:'iPhone 8']

>>>
출시일	디스플레이	메모리	출시 버전	Face ID
iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No
iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No
iPhone 8	2017-09-22	4.7	2GB	iOS 11.0	No

#위에서 loc 안쓰고 인덱싱 하는거 슬라이싱에서는 안됨 
iphone_df.loc[:,'메모리':'Face ID']

>>>
메모리	출시 버전	Face ID
iPhone 7	2GB	iOS 10.0	No
iPhone 7 Plus	3GB	iOS 10.0	No
iPhone 8	2GB	iOS 11.0	No
iPhone 8 Plus	3GB	iOS 11.0	No
iPhone X	3GB	iOS 11.1	Yes
iPhone XS	4GB	iOS 12.0	Yes
iPhone XS Max	4GB	iOS 12.0	Yes

iphone_df.loc['iPhone 7':'iPhone X','메모리':'Face ID']

>>>
메모리	출시 버전	Face ID
iPhone 7	2GB	iOS 10.0	No
iPhone 7 Plus	3GB	iOS 10.0	No
iPhone 8	2GB	iOS 11.0	No
iPhone 8 Plus	3GB	iOS 11.0	No
iPhone X	3GB	iOS 11.1	Yes


#불린타입 series도 인덱싱 가능
iphone_df['디스플레이']>5

iPhone 7         False
iPhone 7 Plus     True
iPhone 8         False
iPhone 8 Plus     True
iPhone X          True
iPhone XS         True
iPhone XS Max     True
Name: 디스플레이, dtype: bool

iphone_df.loc[iphone_df['디스플레이']>5]
#iphone_df.loc[[False,True,False,True,True,True,True]]랑 같음

출시일	디스플레이	메모리	출시 버전	Face ID
iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No
iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes

#컬럼으로도 인덱싱 가능
iphone_df.loc[:,[True,False,True,True,False]]

출시일	메모리	출시 버전
iPhone 7	2016-09-16	2GB	iOS 10.0
iPhone 7 Plus	2016-09-16	3GB	iOS 10.0
iPhone 8	2017-09-22	2GB	iOS 11.0
iPhone 8 Plus	2017-09-22	3GB	iOS 11.0
iPhone X	2017-11-03	3GB	iOS 11.1
iPhone XS	2018-09-21	4GB	iOS 12.0
iPhone XS Max	2018-09-21	4GB	iOS 12.0

iphone_df['Face ID']=='Yes'

iPhone 7         False
iPhone 7 Plus    False
iPhone 8         False
iPhone 8 Plus    False
iPhone X          True
iPhone XS         True
iPhone XS Max     True
Name: Face ID, dtype: bool

#조건연산자 사용가능 or은 | 사용하면 됨
condition=(iphone_df['Face ID']=='Yes')&(iphone_df['디스플레이']>5)
condition

iPhone 7         False
iPhone 7 Plus    False
iPhone 8         False
iPhone 8 Plus    False
iPhone X          True
iPhone XS         True
iPhone XS Max     True
dtype: bool

#조건 응용하기
iphone_df[condition]
iphone_df[condition,'디스플레이']='양호'

#iloc를 사용하면 숫자로 인덱싱할 수 있음
iphone_df.iloc[2,4]
>>
'No'

iphone_df.iloc[[1,3],[1,4]]
>>
디스플레이	Face ID
iPhone 7 Plus	5.5	No
iPhone 8 Plus	5.5	No

iphone_df.iloc[3:,1:4]
>>
디스플레이	메모리	출시 버전
iPhone 8 Plus	5.5	3GB	iOS 11.0
iPhone X	5.8	3GB	iOS 11.1
iPhone XS	5.8	4GB	iOS 12.0
iPhone XS Max	6.5	4GB	iOS 12.0
```



#### DataFrame에 값 쓰기
```python
iphone_df.loc['iPhone 8','출시 버전']

>>
'iOS 11.0'
'iPhone 8'

iphone_df.loc['iPhone 8','출시 버전']='iOS 11.5'
iphone_df.loc['iPhone 8','출시 버전']

>>
'iOS 11.5'

iphone_df.loc['iPhone 8']=['2016-09-25','4.7','4GB','iOS 13.0','No']
iphone_df.loc['iPhone 8']

>>
출시일        2016-09-25
디스플레이             4.7
메모리               4GB
출시 버전        iOS 13.0
Face ID            No
Name: iPhone 8, dtype: object

iphone_df['face ID']='Yes'
iphone_df

>>
출시일	디스플레이	메모리	출시 버전	Face ID	face ID
iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No	Yes
iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No	Yes
iPhone 8	2016-09-25	4.7	4GB	iOS 13.0	No	Yes
iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No	Yes
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes	Yes
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes	Yes
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes	Yes
```



#### DataFrame에 한 줄 단위,column,row 추가 삭제

```python
#row 추가
iphone_df.loc['iPhone XR']=['2016-09-25','4.7','4GB','iOS 13.0','No','No']
iphone_df

>>
출시일	디스플레이	메모리	출시 버전	Face ID	face ID
iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No	Yes
iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No	Yes
iPhone 8	2016-09-25	4.7	4GB	iOS 13.0	No	Yes
iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No	Yes
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes	Yes
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes	Yes
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes	Yes
iPhone XR	2016-09-25	4.7	4GB	iOS 13.0	No	No

#column 삭제(원본 변형)
iphone_df.drop('face ID',axis='columns',inplace=True)
iphone_df

>>
출시일	디스플레이	메모리	출시 버전	Face ID
iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No
iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No
iPhone 8	2016-09-25	4.7	4GB	iOS 13.0	No
iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes
iPhone XR	2016-09-25	4.7	4GB	iOS 13.0	No

#row 삭제(원본 변형 안함)
iphone_df.drop('iPhone XR',axis='index',inplace=False)

>>
출시일	디스플레이	메모리	출시 버전	Face ID
iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No
iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No
iPhone 8	2016-09-25	4.7	4GB	iOS 13.0	No
iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes

iphone_df

>>
출시일	디스플레이	메모리	출시 버전	Face ID
iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No
iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No
iPhone 8	2016-09-25	4.7	4GB	iOS 13.0	No
iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes
iPhone XR	2016-09-25	4.7	4GB	iOS 13.0	No

index/column 설정하기

liverpool_df=pd.read_csv('./data/liverpool.csv',index_col=0)
liverpool_df

>>
position	born	number	nationality
Roberto Firmino	FW	1991	no. 9	Brazil
Sadio Mane	FW	1992	no. 10	Senegal
Mohamed Salah	FW	1992	no. 11	Egypt
Joe Gomez	DF	1997	no. 12	England
Alisson Becker	GK	1992	no. 13	Brazil

liverpool_df.rename(columns={'position':'Position'})

>>
Position	born	number	nationality
Roberto Firmino	FW	1991	no. 9	Brazil
Sadio Mane	FW	1992	no. 10	Senegal
Mohamed Salah	FW	1992	no. 11	Egypt
Joe Gomez	DF	1997	no. 12	England
Alisson Becker	GK	1992	no. 13	Brazil

liverpool_df

>>
position	born	number	nationality
Roberto Firmino	FW	1991	no. 9	Brazil
Sadio Mane	FW	1992	no. 10	Senegal
Mohamed Salah	FW	1992	no. 11	Egypt
Joe Gomez	DF	1997	no. 12	England
Alisson Becker	GK	1992	no. 13	Brazil

#사전형태로 컬럼이름 변경 가능
liverpool_df.rename(columns={'position':'Position','born':'Born'},inplace=True)
liverpool_df

>>
Position	Born	number	nationality
Roberto Firmino	FW	1991	no. 9	Brazil
Sadio Mane	FW	1992	no. 10	Senegal
Mohamed Salah	FW	1992	no. 11	Egypt
Joe Gomez	DF	1997	no. 12	England
Alisson Becker	GK	1992	no. 13	Brazil

#index 이름 변경 및 설정 가능
liverpool_df.index.name='Player Name'
liverpool_df

>>
Position	Born	number	nationality
Player Name				
Roberto Firmino	FW	1991	no. 9	Brazil
Sadio Mane	FW	1992	no. 10	Senegal
Mohamed Salah	FW	1992	no. 11	Egypt
Joe Gomez	DF	1997	no. 12	England
Alisson Becker	GK	1992	no. 13	Brazil

#다른 column으로 index 설정가능 그러나 기존 index는 덮어써짐
liverpool_df.set_index('number')

>>
Position	Born	nationality
number			
no. 9	FW	1991	Brazil
no. 10	FW	1992	Senegal
no. 11	FW	1992	Egypt
no. 12	DF	1997	England
no. 13	GK	1992	Brazil

liverpool_df.index

>>
Index(['Roberto Firmino', 'Sadio Mane', 'Mohamed Salah', 'Joe Gomez',
'Alisson Becker'],
dtype='object', name='Player Name')

#따라서 기존 인덱스를 따로 column을 생성해서 설정해줘야함
liverpool_df['Player Name']=liverpool_df.index
liverpool_df

>>
Position	Born	number	nationality	Player Name
Player Name					
Roberto Firmino	FW	1991	no. 9	Brazil	Roberto Firmino
Sadio Mane	FW	1992	no. 10	Senegal	Sadio Mane
Mohamed Salah	FW	1992	no. 11	Egypt	Mohamed Salah
Joe Gomez	DF	1997	no. 12	England	Joe Gomez
Alisson Becker	GK	1992	no. 13	Brazil	Alisson Becker
number

#number column으로 index 변경
liverpool_df.set_index('number')

>>
Position	Born	nationality	Player Name
number				
no. 9	FW	1991	Brazil	Roberto Firmino
no. 10	FW	1992	Senegal	Sadio Mane
no. 11	FW	1992	Egypt	Mohamed Salah
no. 12	DF	1997	England	Joe Gomez
no. 13	GK	1992	Brazil	Alisson Becker


```
#### 큰 데이터 다루기
```python
laptops_df=pd.read_csv('./data/laptops.csv')

#위에서 3개 데이터만 출력
laptops_df.head(3)

>>
brand	model	ram	hd_type	hd_size	screen_size	price	processor_brand	processor_model	clock_speed	graphic_card_brand	graphic_card_size	os	weight	comments
0	Dell	Inspiron 15-3567	4	hdd	1024	15.6	40000	intel	i5	2.5	intel	NaN	linux	2.50	NaN
1	Apple	MacBook Air	8	ssd	128	13.3	55499	intel	i5	1.8	intel	2.0	mac	1.35	NaN
2	Apple	MacBook Air	8	ssd	256	13.3	71500	intel	i5	1.8	intel	2.0	mac	1.35	NaN

#끝에서 3개 데이터만 출력
laptops_df.tail(5)

>>
brand	model	ram	hd_type	hd_size	screen_size	price	processor_brand	processor_model	clock_speed	graphic_card_brand	graphic_card_size	os	weight	comments
162	Asus	A555LF	8	hdd	1024	15.6	39961	intel	i3 4th gen	1.7	nvidia	2.0	windows	2.3	NaN
163	Asus	X555LA-XX172D	4	hdd	500	15.6	28489	intel	i3 4th gen	1.9	intel	NaN	linux	2.3	NaN
164	Asus	X554LD	2	hdd	500	15.6	29199	intel	i3 4th gen	1.9	intel	1.0	linux	2.3	NaN
165	Asus	X550LAV-XX771D	2	hdd	500	15.6	29990	intel	i3 4th gen	1.7	intel	NaN	linux	2.5	NaN
166	Asus	X540LA-XX538T	4	hdd	1024	15.6	30899	intel	i3 5th gen	2.0	intel	NaN	windows	2.3	NaN

#대략적인 크기 출력
laptops_df.shape

>>
(167, 15)

#컬럼 이름 확인
laptops_df.columns

>>
Index(['brand', 'model', 'ram', 'hd_type', 'hd_size', 'screen_size', 'price',
'processor_brand', 'processor_model', 'clock_speed',
'graphic_card_brand', 'graphic_card_size', 'os', 'weight', 'comments'],
dtype='object')

#컬럼의 기본적인 특징 출력
laptops_df.info()

>>
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 167 entries, 0 to 166
Data columns (total 15 columns):
#   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
0   brand               167 non-null    object 
1   model               167 non-null    object 
2   ram                 167 non-null    int64  
3   hd_type             167 non-null    object 
4   hd_size             167 non-null    int64  
5   screen_size         167 non-null    float64
6   price               167 non-null    int64  
7   processor_brand     167 non-null    object 
8   processor_model     167 non-null    object 
9   clock_speed         166 non-null    float64
10  graphic_card_brand  163 non-null    object 
11  graphic_card_size   81 non-null     float64
12  os                  167 non-null    object 
13  weight              160 non-null    float64
14  comments            55 non-null     object 
dtypes: float64(4), int64(3), object(8)
memory usage: 19.7+ KB

#데이터들의 특징 출력
laptops_df.describe()

>>
ram	hd_size	screen_size	price	clock_speed	graphic_card_size	weight
count	167.000000	167.00000	167.000000	167.000000	166.000000	81.000000	160.000000
mean	6.898204	768.91018	14.775210	64132.898204	2.321084	52.160494	2.250813
std	3.787479	392.99080	1.376526	42797.674010	0.554187	444.134142	0.648446
min	2.000000	32.00000	10.100000	13872.000000	1.100000	1.000000	0.780000
25%	4.000000	500.00000	14.000000	35457.500000	1.900000	2.000000	1.900000
50%	8.000000	1024.00000	15.600000	47990.000000	2.300000	2.000000	2.200000
75%	8.000000	1024.00000	15.600000	77494.500000	2.600000	4.000000	2.600000
max	16.000000	2048.00000	17.600000	226000.000000	3.800000	4000.000000	4.200000

#가격 기준으로 정렬
laptops_df.sort_values(by='price')

>>
brand	model	ram	hd_type	hd_size	screen_size	price	processor_brand	processor_model	clock_speed	graphic_card_brand	graphic_card_size	os	weight	comments
148	Acer	Aspire SW3-016	2	ssd	32	10.1	13872	intel	Atom Z8300	1.44	intel	NaN	windows	1.2	NaN
83	Acer	A315-31CDC UN.GNTSI.001	2	ssd	500	15.6	17990	intel	Celeron	1.10	intel	NaN	windows	2.1	NaN
108	Acer	Aspire ES-15 NX.GKYSI.010	4	hdd	500	15.6	17990	amd	A4-7210	1.80	amd	NaN	windows	2.4	NaN
100	Acer	A315-31-P4CRUN.GNTSI.002	4	hdd	500	15.6	18990	intel	pentium	1.10	intel	NaN	windows	NaN	NaN
73	Acer	Aspire ES1-523	4	hdd	1024	15.6	19465	amd	A4-7210	1.80	amd	NaN	linux	2.4	NaN
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
154	Microsoft	Surface Book CR9-00013	8	ssd	128	13.5	178799	intel	i5	1.80	intel	NaN	windows	1.5	NaN
31	Acer	Predator 17	16	ssd	256	17.3	178912	intel	i7	2.60	nvidia	NaN	windows	4.2	Integrated Graphics
96	Alienware	AW13R3-7000SLV-PUS	8	ssd	256	13.3	190256	intel	i7	3.00	nvidia	6.0	windows	2.6	13.3 inch FHD (1920 x 1080) IPS Anti-Glare 300...
90	Alienware	15 Notebook	16	hdd	1024	15.6	199000	intel	i7	2.60	nvidia	8.0	windows	3.5	Maximum Display Resolution : 1920 x 1080 pixel
5	Apple	MacBook Pro (TouchBar)	16	ssd	512	15.0	226000	intel	i7	2.70	intel	2.0	mac	2.5	NaN
167 rows × 15 columns

#역순으로 정렬
laptops_df.sort_values(by='price',ascending=False)

>>
brand	model	ram	hd_type	hd_size	screen_size	price	processor_brand	processor_model	clock_speed	graphic_card_brand	graphic_card_size	os	weight	comments
5	Apple	MacBook Pro (TouchBar)	16	ssd	512	15.0	226000	intel	i7	2.70	intel	2.0	mac	2.5	NaN
90	Alienware	15 Notebook	16	hdd	1024	15.6	199000	intel	i7	2.60	nvidia	8.0	windows	3.5	Maximum Display Resolution : 1920 x 1080 pixel
96	Alienware	AW13R3-7000SLV-PUS	8	ssd	256	13.3	190256	intel	i7	3.00	nvidia	6.0	windows	2.6	13.3 inch FHD (1920 x 1080) IPS Anti-Glare 300...
31	Acer	Predator 17	16	ssd	256	17.3	178912	intel	i7	2.60	nvidia	NaN	windows	4.2	Integrated Graphics
154	Microsoft	Surface Book CR9-00013	8	ssd	128	13.5	178799	intel	i5	1.80	intel	NaN	windows	1.5	NaN
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
73	Acer	Aspire ES1-523	4	hdd	1024	15.6	19465	amd	A4-7210	1.80	amd	NaN	linux	2.4	NaN
100	Acer	A315-31-P4CRUN.GNTSI.002	4	hdd	500	15.6	18990	intel	pentium	1.10	intel	NaN	windows	NaN	NaN
108	Acer	Aspire ES-15 NX.GKYSI.010	4	hdd	500	15.6	17990	amd	A4-7210	1.80	amd	NaN	windows	2.4	NaN
83	Acer	A315-31CDC UN.GNTSI.001	2	ssd	500	15.6	17990	intel	Celeron	1.10	intel	NaN	windows	2.1	NaN
148	Acer	Aspire SW3-016	2	ssd	32	10.1	13872	intel	Atom Z8300	1.44	intel	NaN	windows	1.2	NaN
167 rows × 15 columns

#정렬한 내용 원본 반영
laptops_df.sort_values(by='price',ascending=False,inplace=True)
```

#### 큰 series 다루기
```python
laptops_df=pd.read_csv('./data/laptops.csv')
laptops_df['brand']

>>
0       Dell
1      Apple
2      Apple
3      Apple
4      Apple
...  
162     Asus
163     Asus
164     Asus
165     Asus
166     Asus
Name: brand, Length: 167, dtype: object

#겹치지는거 없애고 중복없이 출력
laptops_df['brand'].unique()

>>
array(['Dell', 'Apple', 'Acer', 'HP', 'Lenovo', 'Alienware', 'Microsoft',
'Asus'], dtype=object)

#몇번 겹치는지
laptops_df['brand'].value_counts()

>>
HP           55
Acer         35
Dell         31
Lenovo       18
Asus          9
Apple         7
Microsoft     6
Alienware     6
Name: brand, dtype: int64

#대략적인 정보 출력
laptops_df['brand'].describe()

>>
count     167
unique      8
top        HP
freq       55
Name: brand, dtype: object
```




# Tip
- 사용하다보면 생략된 데이터까지 한눈에 보고 싶은 경우가 생
```python
pd.set_option("display.max_rows", None)  # 모든 행 표시
pd.set_option("display.max_columns", None)  # 모든 열 표시
pd.set_option("display.width", None)  # 셀 너비 제한 없애기
pd.set_option("display.max_colwidth", None)  # 열 내용 전체 표시
```