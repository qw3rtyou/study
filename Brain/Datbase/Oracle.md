# 기본문법
주석은  `--`

# DDL
- Data Definition Language
- 데이터 정의어
- 테이블 생성, 변경, 제거
- CREATE, ALTER, DROP

## CREATE TABLE

- 데이터 타입
![[Pasted image 20231204212520.png|400]]

```SQL
CREATE TABLE empl ( id NUMBER(5), name VARCHAR2(10) );
```

널값의 허용 여부 : NULL, NOT NULL
```SQL
CREATE TABLE empl_1 ( id NUMBER(5) NOT NULL, name VARCHAR2(10) NULL );
```

## ALTER TABLE
- 생성된 테이블의 속성과 제약조건을 변경
- 테이블에 이미 데이터가 있는 상태에서, 새로운 속성이 추가될 때는 추가된 속성의 값은 NULL 값이 됨

- 구조
```SQL
ALTER TABLE 테이블이름
	[ ADD 속성이름 데이터타입]
	[ DROP COLUMN 속성이름]
	[ MODIFY 속성이름 데이터타입]
	[ ADD [ CONSTRAINT 제약조건이름] 제약조건 (속성이름)]
	[ DROP CONSTRAINT 제약조건이름]
```


- 새로운 속성 추가
```SQL
ALTER TABLE empl_1 ADD address VARCHAR2(10) NULL;
```

- 속성 변경
- 속성의 데이터타입을 바꿀 때는 데이터타입 변환이 가능해야 함
```SQL
ALTER TABLE empl_1 MODIFY address VARCHAR2(20); --NULL은 유지
```

- 속성 삭제
```SQL
ALTER TABLE empl_1 DROP COLUMN address;
```

- 제약 조건 추가
```SQL
ALTER TABLE 테이블명 ADD [CONSTRAINT 제약조건이름] 제약조건 (컬럼명)
```

- 제약 조건 삭제
```SQL
ALTER TABLE 테이블명 DROP CONSTRAINT 제약조건이름
```


## DROP TABLE
- 테이블을 삭제
```SQL
DROP TABLE empl_1;
```


## 무결성 제약 조건
- 데이터 무결성
>데이터를 결함이 없는 상태, 즉 정확하고 유효하게 유지하는 것

- 무결성 제약조건 
>데이터의 무결성을 보장하고 일관된 상태로 유지하기 위한 규칙
>DBMS 가 자동적으로 무결성 제약조건을 검사하므로 응용 프 로그램들은 이러한 제약조건을 검사할 필요가 없음

![[Pasted image 20231205054055.png|400]]

- 컬럼 레벨 제약 조건
- NOT NULL은 컬럼 레벨에서만 가능
```SQL
CREATE TABLE test_tbl2 ( id number(3), jumin char(14) NOT NULL );
```

- 테이블 레벨 제약 조건
- 하나 이상의 컬럼을 참조할 때 사용
```SQL
CREATE TABLE test_tbl5 (
	pk2 number(3),
	fk2 number(3),
	PRIMARY KEY(pk2, fk2)
);
```


### NULL / NOT NULL
명시 안하면 NULL값 허용


### CHECK
- 데이터를 삽입하거나 수정할 때 열의 값이 정의된 규 칙에 부합되는지를 검사
- select문의 where에 들어가는 조건을 쓰면 됨
- 서브 쿼리 불가
```SQL
CREATE TABLE test_tbl2 (
	id number(3),
	jumin char(14) NOT NULL,
	zip char(7) NOT NULL
	CHECK (zip LIKE '%-%')
);

INSERT INTO test_tbl2 (id, jumin, zip) VALUES (2, '840101-1234567', '112=341');
>>ORA-02290: check constraint (SQL_HGHJGSHXJZFBHFXSMRSQVVHVD.SYS_C00142001879) violated ORA-06512: at "SYS.DBMS_SQL", line 1721 

INSERT INTO test_tbl2 (id, jumin, zip) VALUES (2, '840101-1234567', '112-341');
>>1 row(s) inserted.
```


### PRIMARY KEY
- 테이블당 최대 하나의 기본키 제약조건만 설정
- 기본 키의 값은 유일해야 하며, NULL을 허용하지 않음
```sql
CREATE TABLE test_tbl4 (
	pk1 number(3) PRIMARY KEY, -- 기본 키 지정
	uq1 number(3) NULL
);

INSERT INTO test_tbl4 (pk1) VALUES (1);
>>1 row(s) inserted.

CREATE TABLE test_tbl5 (
	pk2 number(3) NOT NULL,
	fk2 number(3) NOT NULL,
	CONSTRAINT tbl5_pk PRIMARY KEY(pk2, fk2)
);

INSERT INTO test_tbl5 (pk2) VALUES (1);
>>ORA-01400: cannot insert NULL into ("SQL_HGHJGSHXJZFBHFXSMRSQVVHVD"."TEST_TBL5"."FK2") ORA-06512: at "SYS.DBMS_SQL", line 1721

```


### UNIQUE
- PRIMARY KEY와 유사하지만, NULL 을 허용
- 한 테이블에 여러 개의 유일성 제약 조건 가능
- uq1 에 uq_test_tbl4 이름의 유일성 제약 조건 생성
```SQL
ALTER TABLE test_tbl4 
	ADD CONSTRAINT uq_test_tbl4 UNIQUE (uq1);

INSERT INTO test_tbl4 VALUES (2, 10);
INSERT INTO test_tbl4 VALUES (3, 20);
INSERT INTO test_tbl4 VALUES (4, 20);
>>1 row(s) inserted. 
>>1 row(s) inserted. 
>>ORA-00001: unique constraint (SQL_HGHJGSHXJZFBHFXSMRSQVVHVD.UQ_TEST_TBL4) violated ORA-06512: at "SYS.DBMS_SQL", line 1721
```


### FOREIGN KEY
- 외래 키: 릴레이션의 기본키를 참조하는 속성 (또는 속성 집합)
- 부모 릴레이션의 어떤 투플의 기본 키 값 혹은 널 값
- 기본키와 외래키 속성의 이름은 달라도 되지만 도메인은 같아야 함
- 하나의 릴레이션에는 외래키가 여러 개 존재할 수도 있고, 외래키를 기본키로 사용할 수도 있음

```SQL
컬럼명 데이터형 [CONSTRAINT 제약조건이름] 
REFERENCES 테이블명(컬럼명1 [, 컬럼명 2, ….] [ON DELETE CASCADE])

컬럼명 데이터형,
…….,
[CONSTRAINT 제약조건이름]
FOREIGN KEY (컬럼명 1 [, 컬럼명 2, ….])
REFERENCES 테이블명(컬럼명 1 [, 컬럼명 2, ….] [ON
DELETE CASCADE])
```

test_tbl6 테이블의 fk2를 test_tbl4의 pk1을 참조할 수 있도록 외래 키 지정
```SQL
CREATE TABLE test_tbl4 (
	pk1 number(3) PRIMARY KEY,
	uq1 number(3) NULL
); -- 이전에 만들어둔 테이블

CREATE TABLE test_tbl6 (
	pk2 number(3) NOT NULL,
	fk2 number(3) NOT NULL,
	CONSTRAINT fk_test_tbl6
	FOREIGN KEY (fk2)
	REFERENCES test_tbl4(pk1)
);

INSERT INTO test_tbl6 VALUES (100, 1); 
INSERT INTO test_tbl6 VALUES (200, 2); 
INSERT INTO test_tbl6 VALUES (400, 4);

>>ORA-02291: integrity constraint (SQL_HGHJGSHXJZFBHFXSMRSQVVHVD.FK_TEST_TBL6) violated - parent key not found ORA-06512: at "SYS.DBMS_SQL", line 1721 
>>1 row(s) inserted. 
>>ORA-02291: integrity constraint (SQL_HGHJGSHXJZFBHFXSMRSQVVHVD.FK_TEST_TBL6) violated - parent key not found ORA-06512: at "SYS.DBMS_SQL", line 1721
```



### FOREIGN KEY : CASCADE
- 연속 변동 설정
- CASCADE - 도미노, 폭포, 연쇄 작용 
- 참조되는 테이블(부모 테이블)의 데이터가 변동되었 을 때 이를 참조하는 쪽(자식 테이블)에서도 자동으로 변동되도록 설정

![[Pasted image 20231204211849.png]]

부모테이블인 test_tbl7에 데이터를 삭제했더니 test_tbl8도 삭제된 모
```SQL
CREATE TABLE test_tbl7 (
	pk4 number(3) PRIMARY KEY
);

CREATE TABLE test_tbl8 (
	pk5 number(3) PRIMARY KEY,
	fk5 number(3),
	CONSTRAINT test_tbl8_fk5
	FOREIGN KEY (fk5)
	REFERENCES test_tbl7 (pk4)
	ON DELETE CASCADE
);

INSERT INTO test_tbl7 (pk4) VALUES(1);
INSERT INTO test_tbl8 (pk5,fk5) VALUES (1,1);
INSERT INTO test_tbl8 (pk5,fk5) VALUES (2,1);

SELECT * FROM test_tbl7;
|PK4|
|---|
|1|

SELECT * FROM test_tbl8;
|PK5|FK5|
|---|---|
|1|1|
|2|1|

DELETE FROM test_tbl7;
>>1 row(s) deleted.

SELECT * FROM test_tbl8;
>>no data found
```


# DML
- Data Manipulation Language
- 데이터 조작어
- 테이블에 데이터를 검색, 삽입, 수정, 삭제
- SELECT, INSERT, DELETE, UPDATE 문 

## SELECT 
- 행과 열의 일부를 추출

### 기본형태
```SQL
SELECT [DISTINCT] 속성이름
FROM 테이블이름
[WHERE 검색조건]
[GROUP BY 속성이름]
[HAVING 검색조건]
[ORDER BY 속성이름 [ASC┃DESC]]
```

### SELECT, FROM
`*` - 모든 속성을 나타냄
```SQL
SELECT * FROM EMP;
```

```SQL
SELECT EMPNO, ENAME, JOB FROM EMP;
```

- 결과에 중복된 투플들을 하나씩만 나타나게 하려면 열 목록에 DISTINCT를 사용하면 됨
```SQL
select DISTINCT job from emp
```


### WHERE
![[Pasted image 20231204195536.png |400]]

```SQL
SELECT * FROM EMP WHERE EMPNO=7499;
```

```SQL
select empno,job,sal from emp WHERE sal >= 1500
```

```SQL
select empno,job,sal from emp WHERE sal >= 1500 AND job = 'SALESMAN'
```

```SQL
SELECT empno, ename, sal, sal*12 FROM emp
```

```SQL
select ename,job,sal from emp WHERE sal BETWEEN 3000 AND 6000
```

- IN 키워드에서 사용되는 리스트는 서브쿼리도 가능
```SQL
select ename,job from emp WHERE job IN ('MANAGER','PRESIDENT')

SELECT ename
FROM emp
WHERE deptno IN
(SELECT deptno FROM dept
WHERE dname='ACCOUNTING' or dname='RESEARCH');
```

- `%` 문자가 0개 이상인 문자열
- `_` 단일 문자
```SQL
select ename,job from emp WHERE ename LIKE 'A%'
select ename,job from empWHERE ename LIKE '%M%'
select ename,job from emp WHERE ename LIKE '‘_L%'
```

- NULL에 대한 연산을 하기 위해서는 특수한 연산자 IS 또는 IS NOT만 사용해야 함
```SQL
select ename,mgr,comm from emp WHERE comm = NULL
select ename,mgr,comm from emp WHERE comm <> NULL -- !=랑 같은 의미
select ename,mgr,comm from emp WHERE comm IS NULL
select ename,mgr,comm from emp WHERE comm IS NOT NULL
```


### ORDER BY
- 행들을 특정 속성(들)을 기준으로 정렬하고자 할 때 사용
- ASC는 오름차순 정렬, DESC는 내림차순 정렬
- 기본적으로 오름차순이므로 ASC는 생략 가능
- 속성명이 여러 개일 때는 첫 번째 것이 1차 정렬 키, 두 번째 것이 2차 정렬 키 등과 같이 적용

```SQL
select job, ename, sal from emp ORDER BY job DESC, ename
select job, ename, sal from emp ORDER BY 1 DESC, 2 -- 같은 결
```



### GROUP BY
- 어떤 속성을 기준으로 집계 함수값(합계, 평균 등) 을 그 컬럼의 값별로 보고자 할 때 사용

- 집계 함수
여러 투플들의 집단에 적용되는 함수
속성에 적용되어 단일 값을 반환함

![[Pasted image 20231205055824.png|400]]

```SQL
SELECT COUNT(*) as 총인원, COUNT(COMM) as 총갯수 
FROM emp --NULL 제외

SELECT COUNT(COMM) as 총갯수, SUM(COMM) as 총합 
FROM emp

SELECT COUNT(COMM) as 총갯수, SUM(COMM) as 합, AVG(COMM) as 평균 
FROM EMP

SELECT MAX(sal) as 최고급여, MIN(sal) as 최저급여 
FROM EMP
```

```SQL
SELECT deptno, AVG(sal) as 평균급여 
FROM emp 
GROUP BY deptno
```

- 표현식에 집계함수는 사용하지 못함
```SQL
SELECT deptno, sum(sal) FROM emp GROUP BY sum(sal) --오류
```

- SELECT 문의 속성 목록에 나타난 속성 중, 집계함수가 아닌 모든 속성은 표현식에 반드시 나와야 함
```SQL
SELECT deptno,job,sum(sal) FROM emp GROUP BY deptno --오류
```

- SELECT절에 집계함수가 포함되어 있고, GROUP BY절이 없는 경우에는 SELECT절에 집계함수가 아닌 속성은 나타날 수 없음
```SQL
SELECT deptno, sum(sal) FROM emp --오류
```

- GROUP BY절에 사용된 속성이라도 SELECT절에 사용되지 않아도 됨
```SQL
SELECT sum(sal) FROM emp GROUP BY deptno --올바름
```

- GROUP BY절에는 속성 별칭을 사용하지 못함
```SQL
SELECT deptno as 부서번호, sum(sal) FROM emp GROUP BY 부서번호 -- 오류
```


### GROUP BY…HAVING
- GROUP BY 절을 적용해서 나온 결과값 중에서 원하는 조건 에 부합하는 자료만 산출하고 싶을 때 사용
```SQL
SELECT deptno, SUM(sal) as 급여합계 
	FROM emp 
	GROUP BY deptno 
	HAVING SUM(sal) >= 9000
	
SELECT deptno, SUM(sal) as 급여합계 
	FROM emp 
	WHERE SAL > 1000
	GROUP BY deptno 
	HAVING SUM(sal) >= 9000

SELECT deptno, SUM(sal) as 급여합계 
	FROM emp 
	WHERE SAL > 1000
	GROUP BY deptno 
	HAVING SUM(sal) >= 9000
	ORDER BY 2
```

- 반드시 GROUP BY 절과 함께 작성해야 함
- WHERE절보다 뒤에 나타나야 함
- HAVING 뒤에는 반드시 집계 함수가 와야 함


### 조인
- 1개 이상의 릴레이션으로부터 연관된 튜플을 결 합하는 것
- 속성들간 공통된 값(기본 키와 외래 키)을 사용하 여 조인 실행
- 조인 속성의 이름은 달라도 되지만 도메인은 같아야 함

-INNER JOIN
```SQL
SELECT table.column1 [, table.column2, ….] 
FROM table1 [INNER] JOIN table2 
ON table1.column1 = table2.column1 
[WHERE <검색조건>]

SELECT table.column1 [, table.column2, ….]
FROM table1, table2
WHERE table1.column1 = table2.column1 [and <검색조건>]
```

```SQL
SELECT empno,ename, job, dname, loc
FROM emp, dept
WHERE emp.deptno = dept.deptno and sal>=2000;

SELECT empno, ename, job, dname, loc
FROM emp INNER JOIN dept
ON emp.deptno = dept.deptno
WHERE sal >= 2000;
```

- alias
- 테이블 별칭을 이용하여 긴 테이블 이름을 간단하게 사용
- FROM 절에 테이블 별칭이 사용되면 SELECT 문 전체에서 사용 가능

```sql
SELECT e.empno,ename, job, d.dname, loc
	FROM emp e INNER JOIN dept d
	ON e.deptno = d.deptno
	WHERE sal>=2000;
```

- 카티션 프로덕트
- 필요없음. 대부분 조건 명시 안해서 생김

- OUTER JOIN
- 내부 조인은 조인하는 테이블의 두 개의 속성에서 공통된 값이 없다면 테이블로부터 행을 반환하지 않음
- 정상적으로 조인 조건을 만족하지 못하는 행들을 보기 위해 외부 조인 사용

```SQL
SELECT table.column1 [, table.column2, ….]
	FROM table1, table2
	WHERE table1.column1 = table2.column1(+) -- 왼쪽 외부 조인

SELECT table.column1 [, table.column2, ….]
	FROM table1 LEFT OUTER JOIN table2
	ON table1.column1 = table2.column1 -- 왼쪽 외부 조인

SELECT a.deptno, b.deptno
	FROM emp a FULL OUTER JOIN dept b
	ON a.deptno = b.deptno -- 완전 외부 조인
```



### 서브쿼리
- 부속 질의, 하위 질
- 하나의 SQL 문(주 질의 : main query)에 중첩된 SELECT 문
- 부속 질의는 주 질의 이전에 한번 실행
- 부속 질의의 결과는 주 질의에 의해 사용됨

select 절에서 사용 : 스칼라 부속질의
from 절에서 사용 : 인라인 뷰
where절에서 사용 : 중첩질의
단일 행 (Single Row) 부속질의
다중 행 (Multiple Rows) 부속질의
다중 열 (Multiple Columns) 부속질의

- SELECT 절에서 사용
```SQL
SELECT empno, sal, sal/(select max(sal) from emp) 
FROM emp
```

- 부속 질의의 결과 값은 1개의 행, 1개 의 열 값만 가능함

- FROM 절에서 사용
```SQL
SELECT emp2000.deptno, COUNT(*)
	FROM (SELECT deptno, ename, deptno FROM emp WHERE sal>2000)emp2000
	GROUP BY emp2000.deptno
 --급여가 2000 보다 많은 사원들에 대한 부서번호 별 사원수를 구하라.
```

- WHERE 절에서 사용 - 단일 행 부속질의
- 오직 하나의 행을 반환
- 단일 행 연산자(=,>, >=, <, <=, <>, !=) 만 사용 가능
```SQL
SELECT ename, empno, job
	FROM emp
	WHERE job = (SELECT job
	FROM emp
	WHERE empno=7369)

--사원번호가 7369인 사원과 같은 업무를 하는 사원의 이름과 사원 번호, 업무를 출력하시오.
```

- WHERE 절에서 사용 - 다중 행 부속질의
- 1개 이상의 행을 반환하는 부속질의
- 복수 행 연산자(IN, NOT IN) 사용 가능
```SQL
SELECT ename
	FROM emp
	WHERE deptno IN
	(SELECT deptno FROM dept
	WHERE dname='ACCOUNTING' or dname='RESEARCH');

-- ‘ACCOUNTING’ 부서나 ‘RESEARCH’ 부서에서 근무하는 사원들의 이름을 검색하라.
```

- WHERE 절에서 사용 - 다중 열 부속질의
- 부속질의의 결과값이 2개 이상의 열을 반환하는 부속질의
```SQL
SELECT empno, ename, sal, deptno
	FROM emp
	WHERE (job, sal) IN ( SELECT job, MIN(sal)
	FROM emp
	GROUP BY job);
	
-- 업무별 최소 급여를 받는 사원의 사원 번호, 사원 이름, 급여, 부서 번호를 출력
```


### 집합연산
- 둘 이상의 SELECT 문들의 결과 집합을 합성해서 하나의 결과 집합으로 만들어주는 연산자
- 집합 연산자로 합성된 SELECT 문은 전체적으로 하나의 문장이 됨

- UNION : 합집합
- SELECT문장의 열들은 개수가 일치해야 하고, 대응되 는 열들의 데이터형은 서로 호환성이 있어야 함
- 최종적인 결과집합의 열 이름은 SELECT문장1 의 것 을 따름
- 기본적으로 중복된 행은 제거
- 기본적으로 결과 집합은 첫번째 열 값으로 정렬
- 이 순서를 바꾸려면 ORDER BY 절을 사용
```SQL
SELECT deptno FROM emp 
UNION 
SELECT deptno FROM dept
```


- INTERSECT : 교집합
```SQL
SELECT deptno FROM emp
INTERSECT
SELECT deptno FROM dept
```


- MINUS : 차집합
```SQL
SELECT deptno FROM emp
MINUS
SELECT deptno FROM dept
```



## INSERT
- 테이블에 새로운 튜플을 삽입

```SQL
INSERT INTO 테이블이름 [(속성리스트)] VALUES ( 값리스트 )
```

```SQL
INSERT INTO emp VALUES (9001, '디비야', 'SE', 7698, NULL, NULL, NULL, NULL)
```

- 속성과 값의 순서는 반드시 서로 일치해야 함
```SQL
INSERT INTO emp(job, ename, empno) VALUES ('SE', '김열공', 9002)
```

- 필드 조건이 NOT NULL 이 아니라면 일부 레코드만 명시할 수 있음
```SQL
INSERT INTO empl VALUES (10, '김철수'); 
INSERT INTO empl (id) VALUES (11); 
INSERT INTO empl (name) VALUES ('강명주');
```


## UPDATE
- 특정 속성값을 수정

```SQL
UPDATE 테이블이름
SET 속성명1 = 값1 [ , 속성명2 = 값2, ... ]
[ WHERE 조건문 ] 
```
- WHERE 절 생략 시 모든 행을 일괄적으로 수정

```SQL
SELECT * FROM emp WHERE empno = 9001; 
UPDATE emp SET job = ‘CIO’ WHERE empno = 9001; 
SELECT * FROM emp WHERE empno = 9001;
```


## DELETE
- 테이블에 있는 기존 튜플 삭제
```SQL
DELETE [FROM] 테이블이름 [ WHERE 조건문 ]
```
- FROM 은 조건없이 생략가능
- WHERE 절은 생략가능 하지만, 모든 행을 일괄 삭제

```SQL
DELETE FROM emp WHERE empno = 9002
```


# DCL
- Data Control Language
- 데이터 제어어
- 사용자 접근 제어. 백업과 회복, 동시성 제어 등
- GRANT, REVOKE


# Normalization

