
---

### 웹 기초 주제

- 네트워크, 웹 개념
- IP주소
    - IP 주소 구조, 특징
- MAC주소
    - IP주소와 MAC주소를 같이 사용하는 이유
    - IP 주소만 알아도 접속이 가능한 이유
- URI, URN, URL
    - 각각 차이점
- 도메인, DNS, DNS 질의 과정
    - DNS의 필요성
- 프로토콜
    - 대표적인 프로토콜
- port
    - well known port
    - 포트 번호의 필요성
- HTTP 프로토콜
    - HTTP header, body
    - Request, Response
    - Method
    - status code
- HTTP/HTTPS
    - SSL/TLS
- 프록시 서버, VPN
- TCP/UDP
- OSI 7계층
- TCP/IP 3, 4 Way Handshaking
- IP 구분
    - 고정 IP, 유동 IP
    - 공인 IP, 사설 IP
- 데이터 전송 방식
    - 유니 캐스트
    - 멀티 캐스트
    - 브로드 캐스트
    - 애니 캐스트
- 네트워크 장비
    - 라우터
    - 스위치
    - 허브
    - 게이트웨이
    - 등등..
- Loopback IP
- 포트포워딩
- 각종 프로토콜 - FTP, Telnet, ARP, ICMP, DHCP, SSH, SSL, …
- 파일 디스크립터
- 패킷
- Fiddler, Wireshark
    - 유명한 프로토콜 구조 분석
    - HTTPS 패킷 뜯어보기
- 소켓 프로그래밍
    - 관련 함수
    - 구조체
    - 통신과정
- Redirect
    - ARP
    - ICMP
    - ARP Spoofing, Sniffing
- 서비스 거부 공격
    - Dos
    - DDos
    - DRDos
- 엔디안
- 절대, 상대 경로
    - 필요성
    - 절대 경로의 기준?
- GET, POST 방식
    - GET 보다 POST가 안전하다고 알려졌었던 이유?
- Server Side Script와 Client Side Script
- HTML
- CSS
- JS
- MySQL
- VMWare
- Linux
    - 절대경로/상대경로
    - 루트 디렉토리, 디렉토리 구조
    - 주요 파일
    - ls, find, cd 등등 기본 명령어
    - 패키지 관리
    - 권한
    - VIM
    - 방화벽
    - SSH, NC
    - Symbolic Link
- APM
- 게시판 제작

---

### 취약점 주제

공통

- SQLi
- XSS
- OS Command Injection
- Path Traversal
- Webshell?, Reverseshell?
- LFI
- RFI
- SSTI
- SOP, CORS?
- CSRF
- SSRF

PHP관련

- PHP Type Juggling
- PHP Serialization
- PHP Eval
- 고급으로 간다면 PHP filter gadget chain도 괜찮습니다 e.g. [dreamhack - secret document stroage: REVENGED](https://dreamhack.io/wargame/challenges/1044)

---

### 그 외 해볼만한 주제

- Curl
    
- Python Request
    
- Flask, Node.js 혹은 요즘 사용하는 간단한 프레임워크 아무거나..
    
- Prototype Pollution
    
- DOM Clobbering
    
- Race Condition
    
- 각 취약점 보호기법(CSP, Prepared Statement 등등)
    
- JWT 토큰
    
- serialize / deserialize
    
- Docker
    
- 다른 DB 익스
    
- 파이썬 자체 배우기? → 근데 이걸 웹에서 해야하나..
    
- DNS data exfiltration
    
- gopher + MySQL DB Leak
    
- DNS Rebinding
    
- Request Smuggling
    
- CSS Injection + XSS (가끔 frontend에 따라서 keylogger로서 작동시켜 admin privilege 탈취까지 가능하긴 합니다)
    
- Directory Brute force e.g. [hspace space war (web) - web101](https://chall.hspace.io/challenges#web101-64)
    

---

# 공통 트랙

### 보여줄만한거..?

- union select sqli 이런거 시연 해서 db 전체 털린 모습 시각적으 보여주기
- xss로 다른 사람 계정으로 로그인하기
- 웹쉘 올려서 메인페이지 디페이스?

### 커리큘럼

1. 만약 공방전이 저번처럼 방학쯤 진행한다고 하면)

- 게시판 만드는 법 간단하게 + 주차별로 과제
- sqli나 xss 등 기법 간단하게 (공방전에서 사용할 수 있을 정도로) -> 딥하게는 심화에서 진행
- 앞서 배운 취약점 공격에 대응하는 방법 / 해시 솔트 암호화 등 시큐어 코딩 ---> 스터디는 이런식으로 공방전 대비로 가고 추가 조사 과제로 네트워크 진행

1. 공방전을 좀 늦게 진행한다고 하면)

- 웹 커리에 흥미를 가질 수 있도록 웹 해킹 실습들을 많이 넣어서 구성

실습 넣으시면 워드프레스에 각종 취약점들 많아서 워드프레스 이용하시는 것도 추천입니다 ㅎ

가장 많이 사용되는 cms다 보니 실습하는 입장에서도 해킹하는 맛 좀 날거에요

넹

### 일정

- 1회차
    
    - 공격 시연 짧게?
    - 환경세팅 도와주기(dockerfile, 깃헙 코드 제공)
- 2회차
    
    - 게시판 만들기 - 코드 제공, 설명만 해주기
    - 게시판 메인 페이지 제작 - 실습
    - sqli 이론 공부
- 3회차
    
    - 케녹서버에 sqli 실습
    - sqli 공격 기법 시연 및 설명
    - xss 이론 공부
- 4회차
    
    - 케녹서버에 xss 실습
    - xss 공격 기법 시연 및 설명

---

# 웹 심화 트랙 일정

- 총 60회 정도




### 16회차 @


### 17회차


### 18회차


---

### 취약점 주제

공통

- SQLi
- XSS
- OS Command Injection
- Path Traversal
- Webshell?
- LFI
- RFI
- SSTI
- SOP, CORS?
- CSRF
- SSRF

PHP관련

- PHP Type Juggling
- PHP Serialization
- PHP Eval

### 1회차

### 2회차

### 3회차

### 4회차

### 5회차

### 6회차

### 7회차

### 8회차

### 9회차

### 10회차

### 11회차

### 12회차

### 13회차

### 14회차

### 15회차

### 16회차

### 17회차

### 18회차

### …

### 60회차..?