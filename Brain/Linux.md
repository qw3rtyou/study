# 리다이렉션(>)
cat은 일반적으로 cat 명령어 다음 입력한 내용을 모니터로
출력해주는 기능을 한다. 그러나

	cat > tmp.txt

이런 식으로 리다이렉션을 사용하면 입력한 내용을 tmp.txt로
'방향을 바꿔' 출력한다.

추가적으로 리다이렉션 을 두 번 사용하면 append 효과가 난다

	cat  >> tmp.txt
	
&>/dev/null: 모든 출력을 /dev/null로 리다이렉션하여 출력을 무시


# 와일드카드
와일드카드(wildcards)는 리눅스에서 임의의 다른 문자를 나타낼 수 있는 특수 문자
## ?
a-z, 0-9 범위 내 임의의 1개 문자로 대체
## *
a-z, 0-9 범위 내 임의의 0개 이상 문자로 대체.
## []

`[문자1-문자2]` 혹은 `[문자1, 문자2, …]` 형태로 범위를 지정
범위 내 모든 문자로 대체될 수 있음

다음은 `ls test[0-9]` 를 실행하여 파일명이 `test` 로 시작하고 마지막이 숫자인 파일을 모두 출력하는 모습

```bash
user@user-VirtualBox:~/new_dir$ ls -l
total 8
-rw-rw-r-- 1 user user 13 12월  2 13:05 hello
-rw-rw-r-- 1 user user 13 12월  2 13:08 world
user@user-VirtualBox:~/new_dir$ touch test1 test2 test3
user@user-VirtualBox:~/new_dir$ ls -l
total 8
-rw-rw-r-- 1 user user 13 12월  2 13:05 hello
-rw-rw-r-- 1 user user 0 12월  2 13:10 test1
-rw-rw-r-- 1 user user 0 12월  2 13:10 test2
-rw-rw-r-- 1 user user 0 12월  2 13:10 test3
-rw-rw-r-- 1 user user 13 12월  2 13:08 world
user@user-VirtualBox:~/new_dir$ ls test[0-9]
test1 test2 test3
user@user-VirtualBox:~/new_dir$
```


# 리다이렉션
모니터에 나타나는 표준 출력 혹은 키보드로 입력하는 표준 입력을 다른 곳으로 변경하는 작업
주로 어떤 명령어의 결과를 파일로 저장하거나, 다른 명령어의 입력으로 전달하는 형태로 리다이렉션 함

## 명령어 > 파일

명령어 표준 출력을 파일로 변경
파일이 없으면 새로 만들고, 있으면 덮어씀

아래는 `ls test[0-9]` 명령어 결과를 `world` 파일에 쓰는 예시

```sh
user@user-VirtualBox:~/new_dir$ ls test[0-9]
test1 test2 test3
user@user-VirtualBox:~/new_dir$ ls test[0-9] > world
user@user-VirtualBox:~/new_dir$ cat world
test1
test2
test3
user@user-VirtualBox:~/new_dir$
```

## 명령어 >> 파일

명령어 표준 출력을 파일로 변경
파일이 없으면 새로 만들고, 있으면 이어서 씀

아래는 `cat hello` 명령어 결과를 `world` 파일에 쓰는 예시

```sh
user@user-VirtualBox:~/new_dir$ cat hello
hello
user@user-VirtualBox:~/new_dir$ cat hello >> world
user@user-VirtualBox:~/new_dir$ cat world
test1
test2
test3
hello
user@user-VirtualBox:~/new_dir$
```

## 명령어 < 파일

명령어 표준 입력을 파일로 변경
파일로부터 표준 입력을 받아 명령어를 수행

아래는 `world` 파일 내용을 표준 입력으로 받아 `grep test` 명령어를 수행하는 예시

```sh
user@user-VirtualBox:~/new_dir$ cat world
test1
test2
test3
hello
user@user-VirtualBox:~/new_dir$ grep test < world
test1
test2
test3
user@user-VirtualBox:~/new_dir$
```



# 특수 권한
setuid 
일반 사용자가 파일을 실행하면 파일 소유자 권한으로 실행됨
예를 들어, `/bin/passwd` 파일은 소유자가 `root`이지만 setuid가 설정되어 있어
일반 사용자가 `root` 권한으로 실행하고 비밀번호도 변경할 수 있음
setuid는 소유자의 실행 권한에 `x` 대신 `s` 문자로 나타냄
대문자 `S`로 표시되는 경우에는 setuid가 걸려 있으나, 실행 권한이 없는 경우

`/bin/passwd`의 권한 플래그는 아래와 같음
소유자의 실행 권한이 `s`로 설정된 것을 볼 수 있음
```sh
user@user-VirtualBox:/bin$ ls -l passwd
-rwsr-xr-x 1 root root 59976 11월 24 21:05 passwd
```

setgid
일반 사용자가 파일을 실행하면 파일 소유 그룹 권한으로 실행됨
setgid는 소유 그룹의 실행 권한에 `x` 대신 `s` 문자로 나타냄
마찬가지로 실행 권한이 없으나 setgid가 걸려 있는 경우 대문자 `S`로 표시

sticky bit
디렉토리에 sticky bit를 설정하면 파일 및 디렉토리 소유자와 root 사용자 외에 일반 사용자가 파일을 삭제할 수 없음
주로 공용 디렉토리에 사용
일반 사용자의 실행 권한에 `x` 대신 `t` 문자로 나타냄
이 역시 마찬가지로 실행 권한이 없는 경우에는 대문자 `T`로 표시

특수 권한을 지정할 때는 권한 플래그 맨 앞에 숫자를 붙여 나타냄
**setuid**는 **4**, **setgid**는 **2**, **sticky bit**는 **1**

아래는 `chmod 4755 world` 명령어로 `world` 파일에 실행 권한과 setuid를 설정하는 모습
setuid만 설정하는 경우 `chmod u+s world`도 가능

setgid는 `chmod g+s world`, sticky bit는 `chmod o+t world`로 설정할 수 있음

```sh
user@user-VirtualBox:~/new_dir$ ls -l
total 12
drwxrwxr-x 2 user user 4096 12월 2 13:38 dir
-rwxr--r-- 1 root user   13 12월 2 13:05 hello
-rwxrw-r-- 1 user user   13 12월 2 13:08 world
user@user-VirtualBox:~/new_dir$ chmod 4775 world
user@user-VirtualBox:~/new_dir$ ls -l
total 12
drwxrwxr-x 2 user user 4096 12월 2 13:38 dir
-rwxr--r-- 1 root user   13 12월 2 13:05 hello
-rwsrwxr-x 1 user user   13 12월 2 13:08 world
```



# 압축
보통 songs.tar.gz 이런 식으로 되어있는데
먼저 gzip을 풀어서 songs.tar로 만드고
그 tar를 해제해서 songs를 사용하면 된다.

### tar
tar는 그냥 합치기만 그래서 오히려 용량이 늘어남 속도가 빠른편

	tar cvf songs.tar *		압축
	tar xvf songs.tar		해제
### gzip
실제로 압축하는 명령어

	gzip 파일이름		선택된 파일을 압축
	gzip -d 파일이름	선택된 파일을 해제
### 확장자	
tar		
tar 프로그램을 사용하여 압축된 파일,
사실 압축이 아닌 여러 파일들이 하나로 뭉쳐져 있는 파일

gz 
gzip 프로그램을 사용하여 압축된 파일

tar.gz	
tar 프로그램을 사용하여 파일을 합친 후, 또 다시 gzip 을 사용하여 압축을 한 파일

tgz
위의 tar.gz 을 합쳐서 tgz라는 확장자로 만듬

# 주요 리눅스 디렉토리 구조	

## `/bin`
일반 유저가 사용할 수 있는 기본적인 명령어나 프로그램을 담고 있는 디렉토리

## `/boot`
시스템 부팅에 필요한 파일들을 담고 있는 디렉토리

## `/dev`
리눅스에서는 컴퓨터에 부착된 물리적인 장치들을 디바이스 드라이버를 거쳐 파일 형태로 접근 가능 
그러한 장치들을 나타내는 파일들을 담고 있는 디렉토리

## `/etc`
운영체제나 운영체제 위에서 동작하는 서비스의 설정 파일들을 담고 있는 디렉토리

## `/home`
각 일반 유저의 홈 디렉토리를 담고 있는 디렉토리
일반 유저들은 각기 자신만의 홈 디렉토리를 가지고 있음
예를 들어 `dream` 유저의 홈 디렉토리는 `/home/dream`

## `/lib`
시스템에 필요한 라이브러리 파일들을 담고 있는 디렉토리
`/bin` 이나 `/sbin` 에 존재하는 프로그램이 필요로 하는 동적 라이브러리 파일이 `/lib` 디렉토리에 존재

## `/opt`
소프트웨어 패키지들을 담는 디렉토리

## `/proc`
리눅스 커널 자원에 접근할 수 있는 파일과 프로세스를 나타내는 파일을 담고 있음

## `/root`
`root` 유저의 홈 디렉토리

## `/sbin`
`/bin` 디렉토리와 마찬가지로 기본적인 유저 명령어나 프로그램을 가지고 있는 디렉토리
`/sbin`은 `root` 유저가 사용할 수 있는 명령어나 프로그램을 가지고 있음

## `/tmp`
유저나 프로그램이 임시로 파일을 생성해야할 때 사용할 수 있는 디렉토리
본 디렉토리에 오래 존재했던 파일들은 자동으로 삭제되므로 주의하여 사용해야 함

## `/usr`
사용자 바이너리, 문서, 라이브러리, 헤더 파일 등을 담고 있는 디렉토리

## `/var`
프로그램이나 시스템이 실시간으로 가변적인 파일을 사용하고 저장해야 할 때 활용하는 디렉토리
예를 들어 `/var/log`에는 다양한 로그 파일이 저장됨
	

# 리눅스에서 중요한 역할을 하는 것들

/etc/passwd		사용자들에 대한 간단한 정보가 들어있음
/etc/shadow		사용자들의 패스워드
/etc/services	서버가 어떤 서비스를 하는지 확인할 수 있음
/etc/issue.net	처음 접속될 때 나오는 화면
/etc/motd		로그인 후에 나오는 메세지
~/public_html	각 사용자의 홈페이지 파일, 보통 해킹 후 수정함


# 모니터링 명령어

프로세스 확인
	ps 		현재 실행중인 프로세스 목록
	top		시스템 리소스 사용량 모니터링 + 실행 프로세스
	htop 	top보다 더 많은 정보
	pgrep [프로세스 이름]		특정 이름을 가진 프로세스의 PID 검색

네트워크 확인
	lsof -i :7000	해당 포트에 있는 서비스 확인
	kill -9 5710	서비스 죽이기
	netstat -ano	모든 포트에서 사용하는 프로세스 확인	

디스크 확인
	df -h : 디스크 사용량을 확인
	lsblk : 디스크 및 파티션 정보를 확인


# nc
`nc hostname(ip) port`

```sh
$ nc google.com 80
GET / HTTP/1.1  
​HTTP/1.1 200 OK
Date: Thu, 01 Dec 2022 02:30:32 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
Cross-Origin-Opener-Policy-Report-Only: same-origin-allow-popups; report-to="gws"
```


# ssh
SSH (Secure Shell, Secure Socket Shell) 원격 서버(컴퓨터)에 연결할 수 있도록 해 주는 암호화된 네트워크 프로토콜

### 사용법
`ssh user@HOST -p PORT -i [개인 키 파일 경로]`
`ssh chall@host3.dreamhack.games -p 16350`

ssh 접속할 때는 원격 서버에 존재하는 계정으로 접속
`user`에 접속할 계정(사용자 이름)을 작성
`HOST`에는 접속하려는 원격 서버의 ip 또는 도메인을 작성
특정 포트로 접속하고 싶은 경우 `-p` 옵션을 이용

### ssh-keygen
서버에 공개 키를 저장하고, 클라이언트가 사용할 개인 키를 지정하여 알맞은 사용자인지 검증
공개 키-개인 키 쌍은 `ssh-keygen` 명령으로 생성할 수 있음




# scp
파일 전송 명령어

	scp -p 5022 Foo1@211.250.216.249:/root/rv-sh /root/

# tty
리눅스에선 사용자마다 임시 터미널을 받음 
해당 터미널을 식별할 때 사용

	qwertyou@DESKTOP-8HVF2JQ:~$ tty
	/dev/pts/0


# /dev/sda
리눅스 시스템에서 첫 번째 SCSI(Small Computer System Interface) 디스크
SCSI 디스크는 하드 디스크 또는 SSD와 같은 데이터 저장 장치
`/dev/sdb`, `/dev/sdc` 등의 이름은 두 번째, 세 번째 SCSI 디스크를 나타냄
`/dev/sda3`는 `/dev/sda` 디스크의 세 번째 파티션



# 설치 스크립트 모음
한글 폰트

chrome

	wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
	sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
	sudo apt update
	sudo apt install google-chrome-stable

apm

	sudo apt update & sudo apt upgrade -y
	sudo apt install apache2 php php-mysql mysql-server -y
	sudo service apache2 start

docker

	sudo apt update
	sudo apt install apt-transport-https ca-certificates curl software-properties-common
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
	echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	sudo apt install docker-ce
	sudo systemctl start docker
	sudo systemctl enable docker
	sudo usermod -aG docker $USER

docker-compose

	sudo apt update
	sudo apt install docker-compose
	docker-compose --version

네트워크툴

	apt install net-tools

vim

	apt install vim

ssh

	sudo apt-get update
	sudo apt-get install openssh-server


# Troubleshoot
### 공개키 오류

키 다시 받기
	wget -q -O - https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | apt-key add -

키 추가하기
	sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 40976EAF437D05B5