BoB 12기 필기문제

UseAfterFree 방지를 위해 현재 객체가 참조되는 수를 저장하는 변수의 이름 : Reference Count
Reference Count : 객체 생성 시 참조 카운트를 1로 초기화하며, 다른 객체가 해당 객체를 참조하거나 해제할 때 참조 카운트를 증가 또는 감소.

XSS 및 데이터 삽입 공격 등을 방어하기 위해 페이지에 로드할 수 있는 컨텐츠를 제어하는 보안정책 : CSP(Content Security Policy)
CSP : 특정 도메인에서만 리소스를 로드하거나, 특정 도메인에서만 스크립트 실행을 허용
SOP(Same-Origin Policy) : 스크립트 실행 시, 스크립트가 속한 도메인과 리소스를 가져올 도메인이 일치하는지 검사하는 보안 정책
HSTS(HTTP Strict Transport Security) : 해당 도메인을 HTTPS로만 접속하도록 설정
HttpOnly : 쿠키의 속성. 쿠키를 JavaScript를 통해 접근할 수 없도록 설정.

웹 브라우저에서 불러오는 리소스가 자신의 origin과 다를 때 추가 http 헤더를 사용하여 다른 orign의 자원에 접근하는 기술 : CORS
CORS(Cross-Origin Resource Sharing) : 웹 브라우저에서 Same-Origin Policy를 우회하여 다른 origin의 리소스에 접근할 수 있도록 허용
위 기술을 사용하기 위해 HTTP 추가 헤더인 Orgin과 Access-Control-Request-Method 등을 사용

웹 브라우저 프로그램의 보안성을 향상시키기 위한 mitigation 기법 : JIT hardening, sandbox, site isolation
site isolation : 웹 사이트를 별도의 프로세스로 격리시켜 하나의 웹 페이지가 다른 웹 페이지에 영향을 미치지 못하도록 하는 기법
JIT hardening : Just-In-Time 컴파일러의 취약성을 줄이기 위한 보안 기법. 악성 스크립에 의해 JIT 컴파일러가 악용되는 것을 방지하여 코드 실행의 안정성을 향상시킨다.
Sandbox : 웹 브라우저를 격리된 환경으로 실행하여 악성 코드의 영향을 제한하는 기법

kaslr : 커널 주소 공간의 ASLR

cpu 해킹 방법론에서 spectre 공격에 사용되었던 cpu 최적화 기법은? : Branch Prediction을 악용.
분기 예측은 CPU 성능 향상을 위한 기법으로, 분기 명령문을 실행하기 전에 해당 분기가 어느 쪽으로 가는지를 예측하는 방식.
Specture 공격은 분기 예측 기법을 이용하여 메모리 상의 기밀 정보를 탈취하는 기법. CPU의 분기 예측을 잘못된 분기를 예측하게 하여, 메모리 접근에 대한 비밀 정보 추출

LFIO 데이터 구조를 가지고 있는 메모리 영역 : 스택

윈도우 커널 오브젝트 생성 번호를 뜻하는 용어 : Handle
커널 오브젝트 : Windows 운영체제에서 리소스(Resource : 프로세스, 쓰레드, 파일)들을 관리하기 위한 데이터를 저장하는 메모리 블록
커널 오브젝트가 생성되면 관리를 위한 핸들이 생긴다. 핸들에는 hProcess, hTread, dwProcessId, dwThreadId 등의 구조체를 가진다.

안드로이드에서 프로시저들의 주소가 담겨있는 테이블 : IAT
IAT(Import Address Table) : 실행 파일이나 공유 라이브러리의 다른 모듈로부터 가져온 외부 함수 및 변수의 주소를 포함하는 테이블
PLT(Procedure Likage Table) : ELF 바이너리 형식에서 사용되며, 함수 호출 시 실제 함수 주소를 검색하고 해당 주소로 점프하기 위해 사용
GOT(eef

 Offset Table) : ELF 바이너리 형식에서 사용되는 다른 모듈로부터 가져온 전역 변수의 주소를 포함하는 테이블
EAT(Export Address Table) : 윈도우 운영체제에서 사용하는 테이블

서버와 클라이언트에서 모두 가능한 공격은?
Cross Site Scripting : 스크립트 구문을 웹페이지에 넣어 의도치 않게 실행되게 하는 공격
SQL Injection : 악의적인 SQL 쿼리 실행
HTTP request smuggling : HTTP 요청을 조작하는 공격으로 프록시 서버를 사용할 때 발생할 수 있는 취약점이며, 공격자가 웹 페이지 요청 시 추가적인 데이터를 전송하게 하여 다음 요청자가 데이터 요구시 공격자의 추가적인 데이터를 헤더로 사용하게 되는 취약점.
+ HTTP 1.0 이하 버전 : TCP/IP 연결 하나당 하나의 세션.
+ HTTP 1.1 이후 버전 : Keep-Alive를 사용하여, TCP/IP 연결 하나당 여러개의 세션 관리.
+ HTTP pipelining : Proxy서버를 사용. (중간자가 생기게 됨)
 
 
+ 정상적인 경우에는 순차적으로 일을 처리한다.
 
+ 프록시 서버를 사용하게 되면서, 첫번째 요청에서 두번째 요청쪽으로 추가 데이터를 전송하게 됨. 이 취약점을 사용하여 Paypal 패스워드 탈취를 한 사례가 있다.

HTTP Request Smuggling & HTTP Desync Attack | Core-Research-Team
Prototype Pollution : Javascript의 프로토타입 체인에 악의적인 데이터를 주입하여 웹 애플리케이션의 동작을 변경하거나 제어하는 공격

CSRF의 완화방법.
SameSite : 쿠키의 전송 방식을 제어하는 데 사용. 동일한 출처에서만 쿠키가 전송될 수 있도록 제한 - strict 설정 시 쿠키가 외부로 전송되지 않음.
HTTPOnly : 쿠키가 Javasciprt에서 사용될 수 없도록 설정.
Referer 검증 : HTTP 요청 헤더의 Refer 값을 검증하여 요청이 유효한지 확인
+ Captcha : 사람인지 컴퓨터인지 확인하는 방식. 

서버의 데이터를 유출할 수 있는 공격.
SSRF(Server Side Request Forgery) : 공격자가 악의적인 요청을 서버로 전송하여 서버의 신뢰할 수 있는 내부 리소스에 대한 요청을 강제로 발생
XML 외부 엔티티 삽입 : XML 파싱을 할 때 외부 엔티티를 로딩하는데, 이를 이용하여 시스템에 액세스하거나, 네트워크 상의 임의 소스에 접근
Java 역직렬화 : 직렬화는 객체를 전송하거나 저장하기 위해 사용되는데, 악의적인 객체를 전달하고, 객체를 역직렬화 할 때 악의적인 행위를 발생
+ ClickJacking : 사용자가 의도되지 않은 클릭을 하도록 유도 하는 것.

IOS 환경에서 실행되는 프로세스가 다른 프로세스에 접근하기 위해 선언되어야 할 entitlements값은? task_for_pid-allow
task_for_pid-allow : 이 entitilements를 가지고 있다면, 다른 프로세스의 PID를 이용하여 해당 프로세스에 접근하고 조작가능.

HeapOverflow 발생 원리 : Memory Region Overrun
Memory Region Overrun : 메모리 영역을 벗어나 읽고 쓰는 오류
+ Memory Leak : 메모리를 해제하지 않아 계속 쌓이는 상황
+ Memory Deallocation Error : 메모리를 올바르지 않게 해제하는 경우.
+ Memory Allocation Error : 메모리 할당 시 오류가 생기는 경우

ROP 공격을 방어하기 위한 기술 : 
Control Flow Integrity : 프로그램의 흐름 검증 기술
+ ROP(Return-Oriented Programming) : 프로그램의 실행 흐름을 조작하여 공격자가 원하는 코드를 실행하는 기법
+ Address Space Layout Randomiza : 메모리 주소를 무작위로 배치
+ Pointer Authentication code : 포인터에 대한 추가적인 정보를 포함시켜 무결성을 검증
+ Memory Tagging Extension : 메모리 액세스의 유효성을 검증

프록시의 계층 : 7계층(응용프로그램)
+ 프록시 : 클라이언트와 서버 사이의 중개자 - 보안, 로드 밸런싱, 캐싱 등의 기능 수행

SSL pinning : 애플리케이션과 서버 사이의 통신을 위한 보안 메커니즘으로, 중간자 공격을 방지하기 위해 사용.
+ Frida로 SSL pinning 우회가 가능

Symmetric Cryptography(대칭키) 와 같은 것은? : Shared Key Crypto(공유 키)

Buffer Overflow 취약점을 방지하기 위한 기술
Stack Overflow Protection : 스택의 경계, 실행 흐름 감지
Canary : 카나리 변경 유무를 확인하여  버퍼 오버플로우를 방지
+ IPS(Intrusion Prevention System) : 네트워크 상에서 악의적인 통신을 차단하는 역할

AndroidManifest의 역할 : 애플리케이션 구성 요소, 권한 설정

C++의 기본 STL 종류
컨테이너(Container)
  Vector, List, Deque, Stack, Queue, Set, Map
  + Vector, Deque, Set, Map 등은 배열을 사용하지만, List의 경우 Linked list를 사용
  + Linked List는 데이터의 삽입과 삭제가 다른 컨테이너에 비해 효율적이지만, 임의 접근에서는 비효율적
알고리즘(Algorithm)
  Sort, Find, Count, Transform, Accumulate
반복자(Iterator), 함수 객체(Function Object), 기타 유틸리티 등.