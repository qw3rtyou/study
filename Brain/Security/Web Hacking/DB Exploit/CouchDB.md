MongoDB와 같이 JSON 형태인 도큐먼트(Document)를 저장
웹 기반의 DBMS로, REST API 형식으로 요청을 처리

다음은 CouchDB 기반 레코드 업데이트 및 조회 예시

```bash
$ curl -X PUT http://{username}:{password}@localhost:5984/users/guest -d '{"upw":"guest"}'
{"ok":true,"id":"guest","rev":"1-22a458e50cf189b17d50eeb295231896"}
$ curl http://{username}:{password}@localhost:5984/users/guest
{"_id":"guest","_rev":"1-22a458e50cf189b17d50eeb295231896","upw":"guest"}
```

# 특수 구성 요소
_ 문자로 시작하는 URL, 필드는 특수 구성 요소를 나타냄

SERVER

	/
	인스턴스에 대한 메타 정보를 반환

	/_all_dbs
	인스턴스의 데이터베이스 목록을 반환

	/_utils
	관리자페이지로 이동

Database

	/db
	지정된 데이터베이스에 대한 정보를 반환
	
	/{db}/_all_docs
	지정된 데이터베이스에 포함된 모든 도큐먼트를 반환

	/{db}/_find
	지정된 데이터베이스에서 JSON 쿼리에 해당하는 모든 도큐먼트를 반환