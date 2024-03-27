키-값(Key-Value)의 쌍을 가진 데이터를 저장
다른 데이터베이스와 다르게 메모리 기반의 DBMS
메모리를 사용하기 때문에 읽고 쓰는 작업을 다른 DBMS보다 훨씬 빠르게 수행

Redis에서 데이터를 작성하고 조회하는 명령어를 입력한 모습

```bash
$ redis-cli
127.0.0.1:6379> SET test 1234 # SET key value
OK
127.0.0.1:6379> GET test # GET key
"1234"
```

데이터 조회 및 조작 명령어

```
GET key
데이터 조회

MGET key [key ...]
여러 데이터를 조회

SET key value
새로운 데이터 추가

MSET key value [key value ...]
여러 데이터를 추가

DEL key [key ...]
데이터 삭제

EXISTS key [key ...]
데이터 유무 확인

INCR key
데이터 값에 1 더함

DECR key
데이터 값에 1 뺌
```

관리 명령어

```
INFO [section]
DBMS 정보 조회

CONFIG GET parameter
설정 조회

CONFIG SET parameter value
새로운 설정을 입력
```


서버 명령어

```
save : 파일 저장 주기 설정

dbfilename : 파일 저장 위치 설정

dir : 현재 디렉토리
```