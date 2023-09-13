service mysql start		mysql 서비스 실행



# CSV 파일로 테이블 생성하기
CSV는 Comma Separated Values의 약자
추가바람..



# WHERE을 이용한 다양한 조건 표현

```sql
SELECT * FROM TABLE WHERE INT_COLUMN BETWEEN 20 AND 30;
SELECT * FROM TABLE WHERE INT_COLUMN IN (20, 30);
SELECT * FROM TABLE WHERE DATE_COLUMN > '2019-01-01';
SELECT * FROM TABLE WHERE address LIKE '서울%';
SELECT * FROM TABLE WHERE address LIKE '__시 __구 %';
SELECT * FROM TABLE WHERE YEAR(DATE_COLUMN) = '2019';
SELECT * FROM TABLE WHERE MONTH(DATE_COLUMN) IN (6,7,8);
SELECT * FROM TABLE WHERE DAYOFONTH(DATE_COLUMN) BETWEEN 15 AND 31;
SELECT email, day, DATEDIFF(day, ’2018-01-03’) FROM TABLE;
SELECT email, day, DATEDIFF(day, CURDATE()) FROM TABLE;
SELECT email, day, DATEDIFF(day, birthday)/365 FROM TABLE;
SELECT email, sign_up_day, DATE_ADD(sign_up_day, INTERVAL 300 DAY) from TABLE;
SELECT email, sign_up_day, DATE_SUB(sign_up_day, INTERVAL 200 DAY) from TABLE;
```

### UNIX Timestamp 값
1970년 1월 1일을 기준으로 몇 초가 지난 것인지 나타냄
UNIX_TIMESTAMP() 위의 기준보다 몇초 지났는지를 반환함
FROM_UNIXTIME() 위의 반환된 값을 보기 좋게 바꿈

### NOT 대체쿼리
NOT 사용가능 !=,<>으로도 사용가능

### 문자열 패턴 조건에서 주의할 점
LIKE : 문자열 패턴 매칭 조건을 걸기 위해 사용되는 키워드
% : 임의의 길의를 가진 문자열(0자도 포함)
_ : 한 자리의 문자

### 이스케이핑, 문자 그대로 사용하기
원래 특정 의미를 나타내던 문자(%)를 그 특정 의미가 아니라, 
일반적인 문자처럼 취급하는 행위를 이스케이핑(escaping)이라고 함
그래서 '중간에 특수문자%가 들어간 문자열'을 표현하고 싶으면

	WHERE id LIKE '%\%%'

### 대소문자 구분하기

	WHERE id LIKE 'g%;

이런식으로 표현하면 대소문자 구분없이 모든 G,g가 나옴
구분하려면

	WHERE id LIKE BINARY 'g%;



# 이쁘게 SQL문 쓰는법(들여쓰기,엔터위치 등등)

절마다 끊기
AND나 OR 전에 들여쓰기
비슷한 내용 들여쓰기

```sql
SELECT COUNT(*),
	ROUND(AVG(star)) 
FROM review
WHERE CONDITION1
	OR CONDITION2
	AND CONDITION3
ORDER BY flag;
```

AND가 OR보다 우선순위가 높지만 괄호로 우선순위 표기해주기



# ORDER BY를 이용한 데이터 정렬
ORDER BY가 WHERE보다 뒤임

```sql
SELECT * FROM DATABASE
WHERE CONDITION
ORDER BY id DESC;
```

오름차순 ASC 내림차순 DESC

### 다중기준정렬
앞에 기준이 더 우선순위가 높음

	SELECT * FROM DATABASE
	ORDER BY id DESC, email ASC;

이러면 id 먼저 정렬 후 email 정렬

### 문자열 형 데이터 정렬
숫자형은 크기 비교 후 정렬하지만 문자형는 앞에서부터 한 글자씩 비교
예를 들어 숫자형은 12>3이지만  문자형은 12<3임

이걸 해결하려면 문자형을 임시적으로 숫자형으로 CAST()로 변경 후 사용하면됨

	ORDER BY CAST(class AS signed) ASC
	
signed는 양수와 음수를 포함한 모든 정수를 나타낼 수 있는 데이터 타입
만약 소수점이 포함되어 있다면 signed 대신 decimal을 사용하면 됨



# LIMIT을 이용한 데이터 추리기
정렬한 후에 앞에서부터 10개만 보고싶다면

	SELECT * FROM TABLE
	ORDER BY id DESC, email ASC
	LIMIT 10;

9번째 10번째를 보고 싶다면

	LIMIT 8,2

왜냐하면 보통 배열의 인덱스가 0부터 시작하는 것 처럼 ROW도 0번째부터 시작함



# 데이터의 특성 구하기
### 집계함수
집계 함수는 특정 컬럼의 여러 row의 값들을 동시에 고려해서 실행되는 함수
SELECT COUNT(id) FROM TABLE;	id 개수 파악
근데 이러면 COUNT가 NULL을 제외하고 세기때문에 ROW 개수를 정확히 파악하기 힘듦
SELECT COUNT(*) FROM TABLE	ROW 개수 파악
SELECT MAX(height) FROM TABLE;	AVG,MIN,SUM 등등도 가능
STD()는 표준편차구해주는 함수

### 집계함수
산술함수
산술 함수는 특정 컬럼의 각 row의 값마다 실행되는 함수

ABS			절대값

SQRT		제곱근

CEIL		올림

FLOOR		내림

ROUND		반올림

CONCAT		문자열 합치기
	
	SELECT CONCAT(height,'cm') FROM TABLE;
	
DISTINCT	고유값 확인

	SELECT DISTINCT(GENGER) FROM TABLE;
	
SUBSTRING	문자열 자르기

	SELECT DISTINCT(SUBSTRING(address,1,8)) FROM member;
	
LENGTH		문자열 길이

UPPER,LOWER	대문자화 소문자화

LPAD,RPAD	 문자열의 왼쪽 또는 오른쪽을 특정 문자열로 채움

	SELECT email, LPAD(age,10,'0') FROM TABLE;
	
TRIM,LTRIM,RTRIM	문자열 속 공백 제거



# 컬럼에 alias 붙이기

```sql
SELECT
email,
weight AS 키,
height AS 몸무게,
weight/((height/100)*(height/100)) AS BMI
FROM TABLE;
```

AS는 생략해도 상관없음 그래도 가시성을 위해 쓰는게 좋음


# CASE END를 이용한 컬럼값 변환해서 보기


```sql
SELECT 
(CASE 
WHEN age =29 THEN '29살'
ELSE '타겟 아님'
END) AS check_29
FROM member
```


# NULL 다루기
기본적으로 SELECT * FROM DATABASE.TABLE WHERE address IS NOT NULL
이런 식으로 다루면 된다.

### COALESCE(COL,STRING)
합치다라는 뜻
COL에 있는 컬럼에서 NULL이 나오면 NULL대신에 STRING으로 대체해줌

```sql
SELECT
	COALESCE(height,'asdf')
FROM DATABASE.TABLE
```

### IS NULL VS =NULL
NULL은 아무 값도 아니기 때문에 뭐랑 비교하든 FALSE임
때문에 =NULL은 항상 FALSE
만약 NULL값이 들어 있다면 TRUE를 얻고 싶다면 IS NULL을 사용하면 됨
같은 맥락으로 !=NULL <>NULL 모두 사용 불가

NULL은 어떤 연산을 해도 결국 NULL


# GROUP BY 그리고 HAVING을 이용한 그루핑해서 보기
GROUP BY를 이용해 그룹을 나누고 각각에 집계합수를 통해 집계된 값을 산출할 
수 있음

	SELECT AVG(height) FROM member GROUP BY gender;

여러 개의 기준으로 그루핑할 수도 있음

```sql
SELECT 
	SUBSTRING(address,1,2) AS region,
	COUNT(*)
FROM copan_main.member
GROUP BY
	SUBSTIRNG(address,1,2),
	gender;
```

HAVING을 이용해 특정 그룹만을 필터링해서 출력할 수 있음

```sql
SELECT 
	SUBSTRING(address,1,2) AS region,
	COUNT(*)
FROM copan_main.member
GROUP BY
	SUBSTIRNG(address,1,2),
	gender;
HAVING
	region='서울'
```

위 예시에서 HAVING 대신에 WHERE을 쓰고 싶을 수도 있는데
WHERE은 테이블의 로우들을 필터링하는 용도고
HAVING은 로우들을 그룹핑한 그룹을 필터링하는 용도로 엄연히 다른 개념이다.

### GROUP BY를 쓸 때 지켜야하는 규칙
SELECT절에는 
	1. GROUP BY뒤에서 사용한 컬럼들 또는
	2. 집계함수만
사용할 수 있다.

다시말해 GROUP BY 뒤에 쓰지 않은 컬럼 이름을 SELECT 뒤에 쓸 수는 없다
왜냐하면 각 그룹에는 여러가지 ROW들이 포함되어 있는데
만약 GROUP BY로 그루핑 되지 않은 컬럼명을 조회하려하면
어느 ROW에 있는 데이터를 가져와야 하는지 결정할 수가 없다.

그러나 COUNT(), MAX()와 같은 집계함수는 여러 ROW에 대한
함수이므로 사용 할 수 있다. 심지어 그루핑 기준으로 사용되지 않은
컬럼이어도 가능하다!

### WITH ROLLUP을 이용해 부분 합계 혹은 전체 합계 구하기
WITH ROLLUP은 말다 소매를 걷어올리다라는 뜻이다.
SQL에서는 세부 그룹들을 좀 더 큰 단위의 그룹으로 중간중간 합쳐준다는 의미

WITH ROLLUP은 2가지 이상의 기준으로 조희가 되었을 때
특정 기준을 무시하고 나머지 기준으로 조회했을 때 결과를 보여준다.

```sql
SELECT SUBSTRING(address, 1, 2) as region,
	   gender,
	   COUNT(*)
FROM member
GROUP BY SUBSTRING(address, 1, 2), gender WITH ROLLUP
HAVING region IS NOT NULL
ORDER BY region ASC, gender DESC;
```

이러면 성별을 무시하고 사는 지역으로만 그루핑을 했을 때 COUNT를 보여준다.
무시 기준은 나중에 그루핑된 기준을 사용한다.

### WITH ROLLUP으로 생긴 NULL 과 그냥 NULL
	WITH ROLLUP으로 생긴 로우는 무시된 커럼을 NULL이라고 표시하게된다.
	그런데 만약 HAVING절에서 region IS NOT NULL과 같은 문장을 사용하면
	WITH ROLLUP으로 생긴 NULL 또한 필터링 된다.
	이를 피하려면 WHERE절로 미리 NULL값을 빼두는 식으로 사용하면 된다.



# SELECT문의 나와야하는 순서와 실행순서
1. 먼저 나와야하는 순서
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
LIMIT

2. 실행 순서
FROM
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
LIMIT

FROM: 어느 테이블을 대상으로 할 것인지를 먼저 결정
WHERE: 해당 테이블에서 특정 조건(들)을 만족하는 row들만 선별
GROUP BY: row들을 그루핑 기준대로 그루핑함
HAVING: 여러 그룹들 중에서, 특정 조건(들)을 만족하는 그룹들만 선별
SELECT: 모든 컬럼 또는 특정 컬럼들을 조회

SELECT 절에서 컬럼 이름에 alias를 붙인 게 있다면,
이 이후 단계(ORDER BY, LIMIT)부터는 해당 alias를 사용할 수 있음

ORDER BY: 각 row를 특정 기준에 따라서 정렬
LIMIT: 이전 단계까지 조회된 row들 중 일부 row들만을 추림



# Foreign key
외래키는 다른 테이블의 특정 row를 식별할 수 있게 해주는 컬럼
이런 관계에서
참조를 하는 테이블인 stock 테이블을 자식 테이블
참조를 당하는 테이블인 item 테이블을 부모 테이블
이라고 함
Foreign Key는 다른 테이블의 특정 row를 식별할 수 있어야 하기 때문에 
주로 다른 테이블의 Primary Key를 참조할 때가 많음
forenign key를 설정하지 않으면 참조할 때 사용하는 키가 이상한 키로 들어가는 것을 막기위함이다.



# JOIN을 이용한 테이블 조인
JOIN은 서로 다른 테이블을 합칠 때 사용하는 키워드이다.
JOIN은 크게 결합 연산과 집합 연산이 있다.

### 결합연산
결합연산은 테이블을 가로 방향으로 합치는 것에 관한 연산이다.
다시말해 컬럼을 변화시키는 JOIN이다.

1) OUTER JOIN
OUTER JOIN은 차집합같은 개념, 두 테이블을 서로 뺏을 때 나오는 ROW만 산출

```sql
SELECT 
	item.id,
	item.name,
	stock.item_id,
	stock.inventory_count
FROM item LEFT OUTER JOIN stock
on item.id=stock.item_id;
```

LEFT OUTER JOIN을 하게되면 왼쪽을 기준으로 ON 뒤에 기준을 만족하는 로우를 연결한 것이다
RIGHT는 반대

```sql
SELECT 
	i.id,
	i.name,
	s.item_id,
	s.inventory_count
FROM item AS i LEFT OUTER JOIN stock AS s
on i.id=s.item_id;
```

2) INNER JOIN
INNER JOIN은 합집합 같은 개념, 두 테이블에 공통인 ROW만 산출

```sql
SELECT
	item.id,
	item.name,
	stock.item_id,
	stock.inventory_count
FROM item INNER JOIN stock
on item.id=stock.item_id;
```

### 집합연산
집합 연산은 테이블을 세로 방향으로 합치는 것에 관한 연산이다.
다시말해 ROW를 변화시키는 JOIN연산이다.

A ∩ B (INTERSECT 연산자 사용)
```sql
SELECT * FROM member_A
	INTERSECT 
SELECT * FROM member_B
```

A - B (MINUS 연산자 또는 EXCEPT 연산자 사용)
```sql
SELECT * FROM member_A 
	MINUS
SELECT * FROM member_B
```

B - A (MINUS 연산자 또는 EXCEPT 연산자 사용)
```sql
SELECT * FROM member_B
	MINUS
SELECT * FROM member_A
```

A U B (UNION 연산자 사용)
```sql
SELECT * FROM member_A
	UNION
SELECT * FROM member_B	
```

UNION 연산자는 중복제거해서 표시됨
중복을 제거하지 않고 표시하려면
UNION ALL 연산자를 사용하면 된다.

두 컬럼 이름이 같다면 ON 대신에 USING(컬럼 이름) 을 사용해도 괜찮다.
서로 다른 종류의 테이블도, 조회하는 컬럼을 일치시키면 집합 연산이 가능하다.
정확히는 서로 다른 테이블의 총 컬럼의 수와, 각 컬럼의 데이터 타입만 일치하면 UNION 연산이 가능
집합 연산 중 INTERSECT, MINUS 연산자는 MySQL에서 지원하지 않아서, 조인을 통해 간접적으로 사용 가능


### 추가적인 조인
##### NATURAL JOIN
NATURAL JOIN은 ON 절 없이 그냥 알아서 조인 조건을 설정해주는 조인이다.
편하긴한데 어떤 컬럼들을 어떤 기준으로 조인할지 알 수가 없기 때문에
사용하지 않는 편이 좋다.

	SELECT COLUMN FROM player NATURAL JOIN team;

##### CROSS JOIN
CROSS JOIN은 각각의 테이블에서 매칭할 수 있는 모든 경우를
매칭한 JOIN이다.
예를 들어 상의 정보가 담긴 테이블, 하의 정보가 담긴 테이블이 있다면
상의 하의 도합을 한눈에 보고 싶을 때 사용하면된다.

##### SELF JOIN
SELF JOIN은 특별한 문법이 있는게 아니라 그냥 자기 자신을 JOIN한
방법이다.
나이 컬럼을 조인하면 자신과 같은 나이인 사람들을 확인할 수도 있고
직원의 직속상관을 담은 테이블이라면 이 회사의 계층 구조를 확인
할 수도 있다.

##### FULL OUTER JOIN
LEFT OUTER JOIN+RIGTH OUTER JOIN 이다.
그런데 UNION ALL로 조인하면 중복나오니까
UNOIN으로 조인하면 된다.
다시말하면 

	SELECT *
	FROM A테이블과 B테이블을 LEFT OUTER JOIN한 결과
	UNION
	SELECT *
	FROM A테이블과 B테이블을 RIGHT OUTER JOIN한 결과

##### Non-Equi JOIN
ON 뒤에 등호가 있는 조건식이 아니라 부등호나 다른 표현식이
들어가있는 조인 방법
경험이 많이 필요해보인다..



# 서브쿼리
말 그대로 한 쿼리 내부에 작은 쿼리를 사용하여 여러 쿼리 창을 사용하지 않고
한 눈에 보기 위함이다.
괄호 안에 서브 쿼리를 넣어주면 그 결과 값이 사용된다.
한편 결과값은 하나만 있을 수도 있지만 여러 컬럼, 여러 로우를 동반할 수도 있다.
즉 여러 값이나 테이블 자체를 리턴할 수 있다.
맨 마지막에 세미콜론은 사용하지 않아도 되는 것 같다.

### SELECT 절에서 사용하는 서브쿼리

```sql
SELECT 
	id,
	name,
	price,
	(SELECT AVG(price) FROM item) AS avg_price
FROM copang_main.item
```

### WHERE 절에서 사용하는 서브쿼리

```sql
SELECT 
	id,
	name,
	price
FROM item
WHERE price=(SELECT MIN(price) FROM item);
```

### 여러값을 담은 서브쿼리
위에서도 언급했듯 서브쿼리는 하나의 값이 아닌 여러 값이 될 수도 있다.	
아래는 리뷰수가 3개 이상인 item을 조희하는 쿼리이다.

```sql
select item.name
from item left outer join review
on item.id=review.item_id
group by item.id
having count(*)>=3
```

이를 서브쿼리로 아래와 같이 작성할 수도 있다.

```sql
select * from item
where id in
(
select item_id
from review
group by item_id having count(*) >= 3)
```

### IN, ANY(SOME), ALL
IN은 서브쿼리에 있는 모든 값 중 하나만이라도 같으면 TRUE
ANY(SOME)는 서브쿼리에 있는 값중 하나라도 만족하면 TRUE
ALL은 서브쿼리에 있는 모든 값을 만족하면 TRUE

```sql
SELECT * FROM MOVIE
	WHERE view_count>ALL(SELECT veiw_count FROM MOVIE
	WHERE category='ACTION')
		AND category != 'ACTION'
```

### FROM 절에서 사용하는 서브쿼리
FROM 절에서 사용된다는 의미는 서브쿼리의 결과가 테이블이라는 의미다.
이러한 테이블을 derived table이라고 하고
꼭 ALIASING을 해줘야한다.

### EXISTS,NOT EXISTS 와 서브쿼리
outer query는 서브쿼리 외부 쿼리, 그러니까 더 상위 쿼리를 말한다.
지금까지 기록한 모든 서브쿼리는 비상관 쿼리이다.
한편, 지금부터는 모두 상관 쿼리에 대한 내용이다.
위에서 서브쿼리의 결과에 따라 분류하는 것과는 다르게
서브쿼리와 outer query와의 관계 유무에 따라 구분할 수 있다.
서브 쿼리와 outer query를 관계짓는 에시는 아래와 같다.

```sql
SELECT * FROM item
	WHERE EXISTS(SELECT * FROM review 
		WHERE review.item_id=item.id);
```

위에서 서브쿼리 FROM 절에서 review테이블만을 썼음에도
WHERE절에서는 item 테이블 또한 사용한 모습을 확인할 수 있다.
이게 가능한 이유는 SQL에서 가장 먼저 읽히는 부분이 FROM절이기 때문인 것 같다.
만약 위에 예시에서 같은 id가 존재하지 않는 경우를 찾고 싶다면
NOT EXISTS 키워드를 사용하면 된다.



# 뷰
조인등의 작업을 해서 만든 결과 테이블이 가상으로 저장된 형태
지금까지 기록한 내용들을 이용하여 테이블을 만들고 이를
중첩하다가 쿼리가 너무 길어지고 가독성이 떨어지는
문제가 발생할 수도 있다.
이를 해결하기 위해 가상으로 테이블을 저장할 수 있는데

	CREATE VIEW FANCY_VIEW_NAME AS
	SELECT ...

이런식으로 작성하면 VIEW에 저장이 된다.
뷰에 또다른 장점은 데이터 보안을 제공한다.
민감한 정보를 제외하고 필요한 정보만을 담게 할 수 있기 대문에 중요하게 작용한다.



# 데이터베이스를 넓은 관점에서 살펴보기
1. 존재하는 데이터베이스들 파악

	SHOW DATABASES;

2. 한 데이터베이스 안의 테이블(뷰도 포함)들 파악
SHOW FULL TABLES IN database_name;
테이블들은 BASE TABLE이라고 표시, 뷰는 VIEW라고 표시

3. 한 테이블의 컬럼 구조 파악

	DESCRIBE table_name;
	DESC table_name;



# 데이터베이스와 테이블 구축하기

### 데이터베이스 만들기
백틱(\`)을 사용해야 객체들을 표현할 수 있음 '"는 문자열 표현할 때만 사용

```sql
CREATE DATABASE DATABASENAME;		데이터베이스 생성
CREATE DATABASE IF NOT EXISTS DATABASENAME;	
중복하지 않게 데이터베이스 생성

CREATE TABLE `DATABASENAME`.`테이블이름`(
	`컬럼이름` `데이터타입` `속성`,
	`컬럼이름` `데이터타입` `속성`,
	`컬럼이름` `데이터타입` `속성`
);
```


### 데이터베이스 지정하기

실무에서는 여러 개의 데이터베이스를 사용하는 경우가 많음

    USE course_rating;

이렇게 사용하려고 하는 데이터베이스를 지정해두면
DBMS가 작업중인 데이터베이스를 인식하게 되고
SQL문에서 따로 데이터 베이스 이름을 적어주지 않아도됨

    SELECT * FROM A.animal;
대신에
    SELECT * FROM animal;
    
이렇게 사용하면 됨


### 테이블 생성하기

아래 두 개의 테이블 생성 코드는 같음

    CREATE TABLE `course_rating`.`student`(
        `id` INT NOT NULL AUTO_INCREMENT,
        `name` VARCHAR(20) NULL,
        PRIMARY KEY(`id`));

    CREATE TABLE `course_rating`.`student`(
        `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        `name` VARCHAR(20) NULL);

테이블을 생성하면서 FOREIGN KEY도 생성하고 싶으면 다음과 같이 작성하면 된다.

	CREATE TABLE `topic` (
	  `id` int NOT NULL AUTO_INCREMENT,
	  `stNUM` int DEFAULT NULL,
	  `name` varchar(30) DEFAULT NULL,
	  `temperature` decimal(7,2) DEFAULT NULL,
	  `created` datetime NOT NULL,
	  PRIMARY KEY (`id`),
	  KEY `foreign_key_text_idx` (`stNUM`),
	  CONSTRAINT `foreign_key_text` FOREIGN KEY (`stNUM`) REFERENCES `topic` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
	) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


### MYSQL 시간대 변경
SET time_zone='UTC 기준 +-값';			



### 컬럼의 속성
    PK(primary key)
    NN(not null)    null 금지
    AL(auto increment)    row가 추가될 때 마다 1씩 증가
    
    NULL    null 값이 있어도 괜찮다


### 컬럼의 데이터 타입
1. Numeric types
    1) 정수형
        TINYINT (SIGNED/UNSIGNED)
        SMALLINT
        MEDIUMINT
        INT
        BIGINT
    2) 실수형
        DECIMAL(M,D)	M은 전체 자리수 D는 소수점 뒤에 있는 자리수
        DECIMAL 대신에 DEC,NUMERIC,FIXED 사용가능
        FLOAT
        DOUBLE

2. Date and Time types
    1) DATE		날짜를 저장 		2020-03-26
    2) DATETIME		날짜와 시간을 저장		2020-03-26-09:30:27
    3) TIMESTAMP	날짜와 시간을 저장		2020-03-26-09:30:27
    DATETIME과는 다르게 타임 존 정보도 담고있음
    4) TIME		시간을 저장 		09:27:31

3. Stirng types
    1) CHAR(N)		N은 글자수		고정 길이 타입->고정적으로 용량을 먹음 대신 그 외의 추가 비용 X
    2) VARCHAR(N)	N은 글자수		 가변 길이 타입->입력한 값에 따라 유동적으로 용량을 최적화함
    3) TEXT			길이가 긴 문자를 저장
    4) MEDIUMTEXT
    5) LONGTEXT


### 백틱(\`)과 따옴표(')
DBMS에서 데이터베이스 테이블 컬럼 등 구성요소를 보통 객체라고 표현
이러한 객체들에게 주어진 이름을 식별자(identifier)라고함
백틱은 이러한 identifier을 나타내는 기호임

백틱 사용의 장점
    백틱을 쓰면 어느 단어가 사용자가 직접 이름을 지은 부분인지를 
    확실하게 알 수 있음
    이미 SQL 문법에 정해진 키워드로 이름을 짓고 싶을 때는 백틱을 쓰는 것이 필수

비슷하게 생긴 따옴표는 온전하게 문자열임을 나타낼 때 사용함


### 테이블에 row 추가하기

테이블에 row를 추가하려면 다음과 같이 하면 된다.
    
    INSERT INTO student
        (id,name,major)
        VALUES(1,'강정훈','컴공');
        
그런데, 만약 모든 컬럼에 데이터가 들어갔다면 다음과 같이
컬럼 이름들을 생략해도 된다.

    INSERT INTO student
        VALUES(2,'박태경','컴공');

만약 모든 컬럼 이름은 명시 했는데 중간에 빈 데이터가 들어갔다면
당연히 오류가 나오고

데이터의 개수 만큼 모든 컬럼 이름을 명시 했다면,
그리고 올바른 데이터 타입이라면 제대로 들어간다.

    INSERT INTO student
        (id,name)
        VALUES(3,'정장우');
        
다만 이런식으로 했을 땐, AI같은 설정이 안되어 있으면
자동으로 누락된 데이터에는 NULL이 들어간다.


### 테이블의 row 갱신하기

테이블의 row를 갱신하려면 다음과 같은 sql문을 사용하면된다.
    
    UPDATE student SET major='멀티미디어학과' WHERE id=2;

만약 WHERE절을 사용하지 않았다면
모든 row의 major 컬럼은 '멀티미디어학과가 되어버린다.
    
    UPDATE student SET major='멀티미디어학과'
    
2개 이상의 column의 값이 바뀔 수도 있다.
    
    UPDATE student 
        SET major='멀티미디어학과',name='조현진' 
        WHERE id=2;

또, 기존의 값을 기준으로 갱신하고 싶을 수도 있다.
    
    UPDATE student SET score=score+3

### 테이블의 row 삭제하기

테이블의 row를 삭제하려면 다음과 같은 sql문을 사용하면 된다.
    
    DELETE FROM student WHERE id=4;
    
마찬가지로 where절을 안 적으면 모든 row가 지워진다.

    DELETE FROM student;

모든 로우를 지우는 쿼리로 다음과 같은 쿼리도 있다.

	TRUNCATE final_exam_result;

    
### 물리삭제&논리삭제
DELETE문을 사용해서 지우면 물리삭제,
논리 삭제는 삭제해야할 row를 삭제하지 않고, 
삭제 여부를 나타내는 별도의 컬럼을 두고, 
거기에 삭제되었음을 나타내는 값을 넣는 것

    DELETE FROM order WHERE id = 2; 
    UPDATE order SET is_cancelled = ‘Y’;
    
    
# 테이블 다루기

### DESCRIBE
테이블의 구조, 정보를 한눈에 확인할 수 있는 명령어

    DESCRIBE 테이블이름;


## 컬럼 다루기

### 컬럼 추가 (ALTER ADD)
테이블 이름, 컬럼이름, 컬럼타입, 속성

	ALTER TABLE student ADD gender CHAR(1) NULL;


### 컬럼 이름변경 (ALTER RENAME)
테이블 이름, 이전컬럼이름, 변경컬럼이름

	ALTER TABLE student RENAME COLUMN student_num TO regist_num

    
### 컬럼 삭제 (ALTER DROP)
테이블 이름, 컬럼이름

	ALTER TABLE student DROP COLUMN admission_date;


### 컬럼 데이터 타입 변경 (ALTER MODIFY)
테이블 이름, 컬럼이름, 타입

	ALTER TABLE student MODIFY major INT;


### 컬럼에 NOT NULL 속성 주기 (ALTER MODIFY)
테이블 이름, 컬럼이름, 타입, 속성
데이터타입이랑 동시에 바꿔도됨

	ALTER TABLE student MODIFY name VARCHAR(35) NOT NULL;
	ALTER TABLE student MODIFY registration_num INT NOT NULL;
	ALTER TABLE student MODIFY major INT NOT NULL;


### 컬럼에 DEFAULT 속성 주기 (ALTER MODIFY)
테이블 이름, 컬럼이름, 타입, 속성, DEFAULT

	ALTER TABLE student MODIFY major INT NOT NULL DEFAULT 10;


### 컬럼에 시간 관련 타입을 넣기 (INSERT INTO VALUE)
여기서 말하는 타입은 DATETIME,TIMESTAMP타입이다.

##### NOW() 함수
데이터를 넣는 위치에 NOW() 함수를 넣으면 된다
.
INSERT INTO post(title,content,upload_time,recent_time)
VALUES ('제목','ㄱㄷㅊㅋ',NOW(),NOW())

##### DEFAULT CURRENT_TIMESTAMP 속성
테이블에 새 row를 추가할 때 따로 그 컬럼에 값을 주지 않아도 
현재 시간이 설정되도록 하는 속성

##### ON UPDATE CURRENT_TIMESTAMP 속성
기존 row에서 단 하나의 컬럼이라도 갱신되면 
갱신될 때의 시간이 설정되도록 하는 속성

```sql
ALTER TABLE post
	MODIFY upload_time DATETIME DEFAULT CURRENT_TIMESTAMP,
	MODIFY recent_modified_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
```

### 컬럼에 UNIQUE 속성 주기 (ALTER MODIFY)
테이블 이름, 컬럼이름, 타입, 속성, UNIQUE

	ALTER TABLE student MODIFY id INT NOT NULL UNIQUE;

##### Primary Key와 Unique 속성의 차이
	Primary Key는 테이블당 오직 하나만 존재
	Unique 속성은 각각의 컬럼들이 가질 수 있는 속성이기 때문에 
	한 테이블에 여러 개의 Unique 속성들이 존재
	Primary Key는 NULL을 가질 수 없지만, Unique는 NULL을 허용한다.
   
   
### 테이블에 CONSTAINT 걸기 (ALTER ADD CONSTRAINT)
##### CONSTRAINT 걸기
테이블 이름, 조건이름, 조건

	ALTER TABLE student
		ADD CONSTRAINT str_rule CHECK (regi_num<30000000);

##### CONSTRAINT 삭제
테이블 이름, 조건이름

	ALTER TABLE student DROP CONSTRAINT st_rule;

##### CONSTRAINT 걸기2
	ALTER TABLE student
		ADD CONSTRAINT str_rule 
		CHECK (email LIKE '%@%' AND gender IN ('m','f'));
            

### 컬럼 가장 앞으로 당기기 (ALTER MODIFY)

    ALTER TABLE playe_info
        MODIFY id INT NOT NULL AUTO_INCREMENT FIRST;
        

### 컬럼 간의 순서 바꾸기 (ALTER MODIFY)

    ALTER TABLE player_info 
    	MODIFY role CHAR(5) NULL AFTER name;


### 컬럼 이름,컬럼의 데이터 타입 속성 동시에 수정하기 ALTER CHANGE
테이블 이름, 기존컬럼이름, 변경컬럼이름, 타입, 속성

	ALTER TABLE player_info
		CHANGE role postion VARCHAR(2) NOT NULL;



컬럼 관련 여러 작업 동시 수행하기
	위에서 나온 컬럼 관련 작업은 모두 같이 사용할 수 있다.

	ALTER TABLE player_info
	MODIFY role CHAR(5) NULL AFTER name,
	DROP CONSTRAINT st_rule;


## 테이블 자체를 다루기
### 이름변경
컬럼을 명시하고 컬럼 이름을 적으면 컬럼이름 바꾸기
아니면 테이블 이름 변경

	RENAME TABLE student TO undergraduate;


### 복사본 만들기(테이블 컬럼 구조 + ROW까지)

	CREATE TABLE copy_undergraduate AS SELECT * FROM undergraduate;


### 삭제
	DROP TABLE copy_undergraduate;


### 복사본 만들기(테이블 컬럼 구조)
위에서 복사본 만드는 거에서 ROW는 추가 안함

	CREATE TABLE copy_undergraduate LIKE undergraduate;

이 상태에서 ROW를 추가하고 싶다면 다음과 같이 하면 된다.

	INSERT INTO copy_undergraduate SELECT * FROM undergraduate;

당연히 두 테이블의 구조가 같을 때만 가능하다.


복사본 만들때나 새 값을 넣을 때 사용했던 쿼리문을 보면 서브쿼리가
사용된 걸 확인할 수 있다. 당연히 서브쿼리니까 where절 같은 문을
추가할 수 있다.



# Foreign Key 사용하기
foreign key 란 한 테이블의 컬럼 중에서 다른 테이블의 특정 컬럼으로 식별할
수 있는 컬럼을 말함 우리나라 말로 외래키라고 함

한 테이블의 컬럼에 있는 key가 다른 테이블에서 primary key라면foreign key일 
것이다. 이렇게 다른 테이블에서 찾는것 을 참조(reference) 라고 한다.

Foreign Key가 존재할 때 Foreign Key가 있는 테이블을 자식 테이블(child table)이나 참조하는 테이블(referencing table)이라고 하고 
Foreign Key에 의해 참조당하는 테이블을 부모 테이블(parent table),
참조당하는 테이블(referenced table)이라고 한다.

DBMS 상에서 한 테이블의 컬럼을, '이것이 다른 테이블의 컬럼을 참조하는 Foreign Key다'라고 설정해놓으면 참조 무결성(Referential Integrity)이라는 것을 지킬 수 있다.

참조 무결성은 참조 관계가 있을 때 각 데이터 간에 유지되어야 하는 정확성과 일관성을 의미
예를들면 참조했더니 참조 결과가 없을 수도 있다 이러한 경우 무결성이 깨진 것이다.


### Foreign Key 설정 쿼리
FOREIGN KEY는 DBMS에서는 일종의 제약으로 CONSTRAINT 추가하듯이 이름을 지어주고
조건을 걸어주고 추가하면 된다.
그리고 아래는 FOREIGN KEY를 student 테이블에 stNUM이라는 컬럼에 걸고
topic 테이블에 id 컬럼을 참조하는 것을 알 수 있다. 

```sql
ALTER TABLE `capston`.`student` 
ADD CONSTRAINT `foreign_key_text`
	FOREIGN KEY (`stNUM`)
	REFERENCES `capston`.`topic` (`id`)
	ON DELETE RESTRICT
	ON UPDATE RESTRICT;
```


지금 바로 현재 테이블을 만드는 쿼리문 알아내기
다음 쿼리문은 review 테이블을 만드는 데 사용한 쿼리문을 알아낼 수 있다.

	SHOW CREATE TABLE review;

row를 확인해보면 결과가 잘 나온 것을 확인할 수 있다.

```sql
CREATE TABLE `review` (
  `id` int NOT NULL AUTO_INCREMENT,
  `stNUM` int DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `temperature` decimal(7,2) DEFAULT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `foreign_key_text_idx` (`stNUM`),
  CONSTRAINT `foreign_key_text` FOREIGN KEY (`stNUM`) REFERENCES `topic` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

굳이 다른 점을 찾자면 FOREIGN KEY를 설정하는 부분인데
CREATE문을 통해 테이블을 만들 때 바로 FOREIGN KEY를 설정하려면
이런 식으로도 사용할 수 있다.


FOREIGN KEY로 보장되는 참조 무결성(자식테이블 관점, ROW 추가)
FOREIGN KEY를 설청한 테이블에 대해서 다음과 같은 ROW 추가 쿼리문을 실행했다.

	INSERT INTO review (course_id, star, comment)
	    VALUES (10, 5 , '정말 좋은 수업이에요!');

그런데 course_id 를 확인해보니 10이라는 값을 가지고 있는 수업이 없다면 
DBMS는 다음과 같은 오류를 반환한다.

	ERROR 1216 (23000) at line 16: Cannot add or update a child row: a foreign key constraint fails

FOREIGN KEY를 설정하면 참조 무결성을 깨는 ROW를 막는 것이다.
다음과 같은 INSERT문은 참조 무결성을 깨지 않으므로 오류없이 잘 실행될 것이다.

	INSERT INTO review (course_id, star, comment)
	    VALUES (8, 5 , '정말 좋은 수업이에요!');


FOREIGN KEY로 보장되는 참조 무결성(부모테이블 관점, ROW 삭제)
부모 테이블의 ROW를 삭제하면 그 ROW를 참조하는 자식 테이블은 참조할 ROW를
잃게 되고 참조 무결성이 깨지게 된다. 
이를 해결해주는게 FOREIGN KEY 설정 쿼리에서 다음과 같은 부분이다.

	ON DELETE RESTRICT
	ON UPDATE RESTRICT;

현재 RESTRICT 부분을 설정하면 참조 무결성이 깨졌을 때 어떻게 대처할 것인지를
설정할 수 있는 정책(옵션)이다. 정책은 총 4가지가 있다.

RESTRICT
	해당 ROW를 참조하고 있는 ROW가 있다면 애초에 삭제를 못하게 함

CASCADE
	'폭포수처럼 떨어지다, 연쇄작용을 일으키다' 라는 뜻
	부모 테이블의 ROW를 지우려고하면 그 ROW를 참조하고 있는
	자식 테이블의 ROW도 삭제됨

SET NULL
	CASCADE에서 같이 삭제되는 ROW를 삭제하는 대신에 NULL로 설정함
	필요없어졌지만 그 자체 데이터를 남기고 싶을 때 사용하면 유용함

NO ACTION
	사실상 RESTRICT와 같은 역할을 함


### 논리적(Logical) Foreign Key 와 물리적(Physical) Foreign Key
실무에서 데이터베이스의 테이블을 살펴보다보면 
어떤 테이블의 특정 컬럼이 Foreign Key로 설정되어야할 것 같은데 
Foreign Key로 설정되지 않은 경우를 보게될 수도 있다.

어떤 테이블의 한 컬럼이 논리적으로 다른 테이블의 컬럼을 참조(reference)
해야 해서 개념 상 Foreign Key에 해당하는 것과, 실제로 해당 컬럼을 
Foreign Key로 설정해서 두 테이블 간의 참조 무결성을 지킬 수 있게 되는 
것은 별개의 개념이다.

논리적으로 성립하는 Foreign Key를 논리적(Logical) Foreign Key라고 하고, 
DBMS 상에서 실제로 특정 컬럼을 Foreign Key로 설정해서 두 테이블 간의 
참조 무결성을 보장할 수 있게 됐을 때, 
그 컬럼을 물리적(Physical) Foreign Key라고 한다.

모든 설정을 물리적 Foreign Key로 설정한다면 참조 무결성이 보장되니까 
좋을 것 같지만 다음과 같은 문제를 만들 수 있다.

성능 문제
	실제 서비스에 의해 사용되고 있는 데이터베이스의 테이블들은 
	단 1초 내에도 수많은 작업이 일어나고 있을 수 있다.

	물리적 Foreign Key가 있는 자식 테이블의 경우에는 
	INSERT, UPDATE 문 등이 실행될 때 
	참조 무결성을 깨뜨리는 변화가 발생하지 않을지 검증해야 하기 때문에
	약간의 속도 저하가 발생할 가능성이 있다.

레거시(Legacy) 
	데이터의 참조 무결성이 이미 깨진 상태
	레거시 데이터는 DBMS같은 시스템이 들어오기 전에
	기존의 코드, 데이터 등을 말하는 용어이다.

	이러한 레거시 데이터가 애초에 무결성을 어기고
	이러한 데이터가 중요해서 삭제할 수 없다면 
	무결성을 포기하게 되는 것이다.


### FOREIGN KEY 삭제
먼저 CREATE TABLE을 사용하여 FOREIGN KEY의 이름을 알아내고
다음의 쿼리문을 작성해주면 된다.

	ALTER TABLE review 
		DROP FOREIGN KEY fk_review_table;
		


# information_schema / mysql / performance_schema / sys