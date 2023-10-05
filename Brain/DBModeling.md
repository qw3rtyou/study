
데이터 모델이란, 다양한 데이터 요소들을 이해하고 사용하기 편한 형태로 정리해놓은 모형

저장하고자 하는 데이터에서 Entity, Attribute, Relationship, Constraint 파악
우리가 데이터를 저장하려고 하는 대상: Entity(개체)
Entity에 대해서 저장하려고 하는 특징: Attribute(속성)
Entity들 사이 생기는 연결점: Relationship(관계)
여러 데이터 요소들에 있는 규칙: Constraint(제약 조건)

이 네 가지 요소들을 파악한 후, 이 내용들을 발전시켜 데이터 모델들을 만드는 과정을 데이터 모델링

# 릴레이셔널 모델
릴레이션은 데이터를 로우와 컬럼으로 정리한 테이블, 또는 표를 의미
Entity는 테이블, attribute은 컬럼, relationship은 foreign key를 사용해서 정리해놓은 모형
릴레이셔널 모델을 모델링한다는 건, 정확히 어떤 테이블을 만들고, 
이 테이블들을 또 어떤 컬럼들로 나누고,foreign key를 어떻게 만들지를 정해나가는 것
    
    
# ERM(Entity-Relationship 모델)
모델링을 할 때는 로우에 대해서 신경을 쓰지 않기 때문에 
데이터를 조금 다른 형태로 표현하는 모델을 같이 사용
ERM에서는 로우를 매번 표현해주지 않아도 되고
선과 선의 끝점들을 통해서 Entity들 사이 관계를 조금 더 자세하게 표현할 수 있음

Entity를 하나의 네모
attribute을 네모 안에 문자열
relationship을 선으로 표현
선들의 끝을 어떻게 표현하는지에 따라 관계의 특징을 표현
    
    
# 데이터 모델 스펙트럼
데이터 모델은 얼마나 자세하게 표현됐는지에 따라 세 가지로 분류

### 개념 모델
가장 추상적인 내용을 담고 있는 모델을 개념 모델
대략적으로 Entity들과 Entity들 사이에 있는 관계 정도만 표현

### 논리 모델
개념 모델보다는 조금 더 자세한 내용을 담고있음

	Entity들이 갖는 Attribute들과 primary key, 
	Entity들 사이 관계를 표현해줄 foreign key

이런 내용까지 표현

### 물리 모델
물리 모델은 실제로 데이터베이스를 구축할 때 필요한 내용에 
최대한 가까운 내용을 담고 있는 모델

	각 컬럼의 데이터 타입, 요소들의 이름, 
	나중에 배울 인덱스라는 걸 어디에 만들어줄 건지...

이런 내용까지 표현
            
            
            
# 논리적 모델링    
### 비즈니스 룰
비즈니스 룰은 특정 조직이 운영되기 위해 따라야 하는 정책, 절차, 원칙에 대한 간단 명료한 설명

모든 명사는 Entity 후보
모든 동사는 Relationship 후보
하나의 "값"으로 표현할 수 있는 명사는 attribute의 후보
하나의 값으로 표현할 수 있더라도, 
하나의 entity가 여러 개의 값을 가져야 하는 경우 
새로운 테이블(entity)을 만드는게 좋음
    

### 카디널리티
카디널리티는 두 entity type 사이 관계에서 한 종류의 entity가 
다른 종류의 entity 몇 개에 대해서 관계를 맺을 수 있는지를 나타내는 개념

1:1 관계
1:N 관계
N:N 관계

최대 카디널리티
최소 카디널리티

![[관계설명1.png]]

![[관계설명2.png]]

![[관계설명3.png]]

![[관계설명4.png]]

### ERD
ERM을 가끔씩 Entity Relationship Diagram, 줄여서 ERD라고 표현하기도 함
    
    
# 관계모델링
### 1:1 관계 모델링
두 Entity 사이에 1:1 관계가 있을 때는 둘 중 하나, 
또는 둘 다에 foreign key를 추가해서 모델링
	
### 1:N 관계 모델링
Entity와 Entity 사이에 1:N 관계가 있을 때는 항상 다, 
즉 관계에서 다수 쪽에 해당하는 entity에 foreign key를 만들어줌
	
### M:N 관계 모델링
M:N 관계는 두 entity 또는 테이블만 사용해서 자연스럽게 표현할 수 없음
그렇기 때문에 관계를 저장하기 위한 테이블인 
연결 테이블 (junction table)이란 걸 사용
연결 테이블에는 각 테이블의 forign key를 만들어줌
즉, 새로운 테이블에 forign key 2개가 담겨져있음
	
        
ERM은 데이터베이스 구조를 만들어낼 때 뿐만 아니라, 
이미 사용하고 있는 데이터베이스를 파악하는데 사용할 수 있음



# 정규화
### 1NF(제 1정규형)
나눌 수 없는 단일 값
모든 칸에 하나의 데이터만 있어야함

하나의 컬럼을 여러개로 나누거나
같은 속성을 나타내는 컬럼을 분리해서 새로운 테이블을 만들면됨
다시 말해서 쪼개서 새로운 로우를 추가함
당연히 후자가 좋음 왜냐하면 전자로 하게 되면 
NULL이 많이 생길 수 있게 된다
컬럼을 몇 개를 만들어야 되는지 애매해진다
조회가 비효율적이게 된다

핵심만 정리해보면 1NF를 지키지 않는 경우는 크게 두 가지가 있음
한 컬럼에 같은 종류의 값을 여러 개 저장하고 있을 때
이때는 해당 컬럼을 하나의 테이블로 분리해서 모델링
한 컬럼에 서로 다른 종류의 값을 여러 개 저장하고 있을 때
이때는 한 컬럼을 여러 개로 분리해서 모델링
    

### 함수 종속성(Functional Dependency)
x의 값에 따라서의 값이 결정될 때,
y는 x에 함수 종속성이 있다고 한다.
x->y 라고 표현

name, age, gender는 email에 함수 종속성이 있다.
email->{name,age,gender}

brand_country는 brand에 함수 종속성이 있고, product는 brand에 함수 종속성이 있다.
이러한 관계를 이행적 함수 종속성이라고 한다.


### Candidate Key
하나의 로우를 특정 지을 수 있는 attribute들의 최소 집합
컬럼으로 id, user_id, product_id, score, description 이렇게 5개의 컬럼이 있을 때,
user_id, product_id 만으로도 하나의 로우를 특정할 수 있으므로 Candidate Key이다.
당연히 id도 Candidate Key이면서 Primary Key이다.
Candidate Key에 해당되는 모든 컬럼은 prime attribute라고 하고,
그 외의 컬럼은 non-prime attribute라고 한다.


### 2NF(제 2정규형)
1NF에 부합해야함
테이블에 Candidate Key의 일부분에 대해서만 함수 종속성이 있는 non-prime attribute가 없어야 함

id, user_id, product_id, age, price, score, comment
이렇게 7개의 컬럼이 있을 때, Candidate Key는 user_id, product_id 이다.
그런데, age는 user_id에 함수종속성이 있고,
price는 product_id에 함수 종속성이 있다.
따라서 2NF에 부합하지 않는다.

이를 해결하려면, 새로 테이블을 만들어서 
현재의 테이블에는 
id, user_id, product_id, comment만 남게 만들면 된다.


### 3NF(제 3정규형)
2NF에 부합해야함
테이블 안에 있는 모든 attribute들은 오직 primary key에 대해서만 함수 종속성이 있어야 함
(=테이블의 모든 attribute는 직접적으로 테이블 Entity에 대한 내용이어야만 한다.)

id, event, event_num, winner, age
이렇게 5개의 컬럼이 있을 때, 2NF를 어기고 있지 않지만
winner는 id에, age는 winner에 함수 종속성을 가지고 있고,
다시말해 age는 id에 2행적 함수 종속성이 있으므로, 3NF에 부합하지 않는다.
대체로 제 3정규형을 하면 웬만한 이상현상은 모두 대처할 수 있다.


### 비정규화
정규화를 하면 여러개의 테이블로 쪼개지게 되는데
데이터를 구하려면 여러 테이블을 join하게 될 것이다.
이는 성능 저하로 이어지기 때문에 의도적으로 비정규화를 해야할 수도 있다.
그러나 이는 이상현상을 야기함을 인지하고 해야한다.
     


# 인덱스 만들기
### Clustered 인덱스 만들기
MYSQL에서는 자동으로 각 테이블이 primary key에대한 Clustered 인덱스가 만들어 진다.
일반적으로 primary key를 사용한 조회를 많이 하기 때문

만약 primary key가 아닌 다른 컬럼을 clustered 인덱스로 사용하고 싶을 때는
clustered 인덱스는 테이블당 하나씩 밖에 있을 수 없기 때문에, 먼저 기존 인덱스를 삭제한 후
해당 코드를 사용해서 인덱스를 추가

	CREATE CLUSTERED INDEX index_name ON table_name (column_name)


### Non-clustered 인덱스 만들기
Non-clustered 인덱스는 개수 상관없이 여러 개를 만들 수 있기 때문에 이미 있는 인덱스를 지울 필요가 없음

	CREATE INDEX index_name ON table_name (column_name)

    
### Composite 인덱스 만들기
Clustered/Non-clustered 인덱스 모두, 하나의 컬럼이 아니라, 여러 개의 컬럼에 대해서 composite 인덱스를 만들 수 있음
composite 인덱스를 만들고 싶은 컬럼 이름들을 괄호 안에 모두 넣어주면 됨

	CREATE INDEX index_name ON table_name (column_name_1, column_2, ...)


### 인덱스 확인하기
    SHOW INDEX FROM table_name;


### 인덱스 삭제하기
    DROP INDEX index_name ON table_name;


    
# sql 백업파일 생성과 복원
mysqldump -utest_user -p'test123' test_db > test_db_backup.sql
mysql -utest_user -p'test123' dev_db < test_db_backup.sql 


    
# TIP
*(와일드카드)는 모두를 뜻함
WHERE NULL = NULL 은 True를 리턴하지 않음

쿼리 끝에 세미콜론 붙이기
예약어는 항상 대문자로 해주는게 좋음(=안해도됨)

schema랑 database랑 비슷함
entry랑 row랑 비슷함

change 명령을 통해 내가 사용하고자 하는 db를 선택할 순있지만
table은 그렇지 않다. 따라서 

```sql
ALTER TABLE player_info
		CHANGE role postion VARCHAR(2) NOT NULL;
```

이런 명령어를 사용할 때 table 이름을 적어주는 것이다.










