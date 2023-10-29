# Central System 문제점
- 병목현상
- 자원 대비 비용이 많이 듬
- dos같은 공격에 약함
- 하나의 머신에 넣을 수 있는 자원의 양은 한정되어있고, 되더라도 그만큼 성능이 안나옴
- 일부가 망가지면 전부 망가짐

# 분산시스템이란?
독립적인 컴퓨터들의 집합체(Networked Computers) + 하나의 컴퓨터처럼 보여야됨

# Single System Image(Single Image Viewer)
내부구조가 복잡할지라도 하나의 시스템으로 보여야함
어디서 누가 접근하더라도 동일한 리소스를 받을 수 있어야함

# 이질성
Types of Distributed Classificatino of Organization(DS)
하드웨어 + OS 까지를 platform이라고 봤을 때,
같은 Windows OS를 사용한다면, 동일한 플랫폼을 사용한다고 할 수 있음
반면에, 다른 플랫폼을 사용하면 이질성을 갖는다고 함
이상적인 경우에 동질형이 될수도 있지만, 대부분은 이질형을 사용할거임
그리고 동질형을 사용한다고 하더라도, 교체시기, 노후화 정도 등은 다를 수 있음
따라서 이질형을 대비해야함

운영체제는 운영체제의 서비스를 사용해야하는데
운영체제에서 api 비슷한 무언가를 사용함(System Call)
local OS 위에 인터페이스(function, procedure, prototype 등등)가 있음
이를통해 이미 내제되어 있는 System Call을 이용해서 운영체제가 동작함
문제는 OS가 다르면 System Call이 다르기 때문에 
동질형과 이질형을 구분해서 설계해야 함

### 동질형(HomoGeneous) DS

DOS(Distributed Opering System)
여러 머신에 공통적으로 깔려있는 OS
Middleware보다 너 낮은 layer임
서로의 자원을 공유할 수 있음
사용자 입장에서 하나로 느끼게 만들 수 있음
동질형 시스템에서만 가능

다른 방법으로는  
그냥 기존의 로컬 os를 사용하고
그 위의 레이어, 미들웨어 시스템을 이용해서 자원을 관리하는 방법이 있음


### 이질형(Heterogeneous) DS
middle웨어를 통해서만 만들 수 있기 때문에
중간자(미들웨어)를 신경써야함
미들웨어는 하나믜 컴퓨터에서 다른 컴퓨터의 자원을 사용할 수 있게 만들어야함


# 미들웨어
가상의 운영체제
엄밀하게는 운영체제는 아님

시스템 어플리케이션(dbms,jvm) 같은 특수한 경우를 제외하고,
대부분의 어플레케이션 레이어에선 자원을 관리할 수가 없음
따라서 미들웨어가 해줘야함
이질적인 분산 시스템 구축의 해심
하나의 인터페이스를 제공해서 자원을 관리해줌
어떤 머신에 있는 자원을 사용하면 좋겠다
어떤머신한테 자원을 저장해라 등등 이런식으로 관리함


# Design Issues
Centuralized System에서 분산 시스템을 구축하려고 할 때
생길 수 있는 문제점을 설명한것

### Transparency
일반적으로 사용하는 투명성이 아님
Centuralized System처럼 하나의 시스템으로 느낄 수 있게 만들어야한다는 의미
Centuralized System보다 Distributed System에서 더 많이 고려해야함

end-user(실사용자)가 사용할 땐, Transparency가 높아야함
즉, 잘 숨겨야함 
그러나 Transparency가 높을수록 에너지를 많이 소모될 수 있음
Middleware가 힘들어함 -> 코드증가, 자원소모증가, 전력소모증가, 속도 감소

중간사용자(우리같은 전공자)가 사용할땐, 적당하면됨
오히려 적당히 높아야 모니터링하기 편함
각각의 하드웨어 자원들의 다양성들을 확인하기 편함
예를들어 인공지능을 돌려야한다면 GPU가 있는 노드에다가 던지는 식
즉, end-user만큼 Transparency가 높을 필요가 없음
그래야 부담이 감소하고, 관리하기 편함

성늠과 Transparency는 반비례
상황에 따라 적절하게 조절

Access - 데이터가 다르더라도 결론적인 데이터 표현은 같아야함. 결론은 다른 자원이더라도 숨기기
Location - 물리적인 자원이 실제로 어디있는지 숨기기
Migration - 자원이 이동했음을 숨기기(로드밸런싱을 위해서)
Relocation - 옮겨지는 도중에도 자원에 접근가능 해야함
Replication - DB를 가지고 있는 머신에 트레픽을 줄이기 위해 여러 레플리카(복사본인데 원본수정하면 반영됨)가 사용되는데, 그러한 레플리카의 존재를 숨기기
Concurrency - 동시성 숨기기
Failure - 고장난 것을 숨기기

***로드밸런싱이란 트래픽이나 작업 부하를 여러 서버 또는 네트워크 장치로 분산하는 기술 또는 방법을 말함***

### Scalability
확장적
늘어나는 것뿐만아니라 줄어든 경우에도
호율적으로 일처리를 해야함
즉, 다양한 규모에서 잘 동작해야함
생각보다 어려운 문제

#### Potential Bottleneck(병목현상)의 원인
Centralized service - 하나의 머신만 사용
Centralized data - db같은 자원이 하나의 머신에만 있음 -> 일관성문제 등 여러문제가 있어서 고민을 조금해야함
Centralized algorithms - 
완전한 라우팅 테이블을 가지고 있을 때, 훨씬 더 빠르게 전달할 수 있음
그런데 네트워크가 커지면 하나의 머신이 모든 라우팅 테이블을 가질 수가 없음 
따라서 적당량의 라우팅테이블만 가지고 있고, 
DNS탐색이나 IP라우팅과 비슷한 방식으로 동작함

너무커지면 토폴로지(구조)자체가 바뀔수도 있기도 하고,
애초에 모든 정보를 가지는게 불가능하기 때문에,
완전한 정보를 가지고 있다는 가정하에 만들어진 알고리즘이 아니라,
너무 큰 시스템에서 파편적으로 나눠진 정보들만가지고도 돌아가는 알고리즘을 말함

#### Decentralized Algorithms의 특징
1. 어떤 머신도 모든 정보를 알고 있으면 안됨
2. 부분 정보만으로 의사결정을 할 수 있어야함
3. 하나의 머신이 망가지더라도 모든 다른 머신이 망가지면 안됨
4. (가장 중요) 모든 컴퓨터에는 시계가 있는데, 서로의 시계가 똑같이 가고, 동일한 시간을 가리키고 있지 않는걸 가정 

Scalability도 엄청 중요하고 어려운 이슈


### Concurrency
동시성, DB에서 언급하는 동시성과 유사
db에서 하나의 트레픽을 transaction이라고 표현함
serial excution(순차적 실행)을 지원하게 되면, 
하나의 transaction이 끝날 때까지 다른 머신들은 놀고 있어야 함
즉, 느려짐 
그래서 서버 개발할때 나오는 동기화같은 개념으로 동시성 제어를 지원해야함
따라서 동시성을 극대화시키되, 같은 데이터를 제공할 것을 보장해야 함
한편, 다른 사람들이 동시에 같은 자원을 사용하는 걸 몰라야함 - Concurrency에 대한 Transparency


### Failure Handling
결함 포용성
주로 소프트웨어보다 하드웨어가 고장이 많이나는데,
일부 하드웨어가 망가지더라도 계속 잘 동작되게 만들어야함
"서비스가 조금 느려졌지만 동작은 하네" 와 같은 반응을 만드는게 목표

하나의 머신이 망가지면
Takeover process를 거쳐서 일을 넘겨받고
Recovery Process를 통해서 다른 머신이 일을 하는동안 고친다.
이를 위해, 여러 머신 상에서 State와 Task등을 공유해야함 - Overhead가 될 수도 있긴함


### Heterogeneity
### Flexibility
### Security


### 분산시스템 개발 시 나올 수 있는 실수
1. 네트워크는 믿을 수 있다.
2. 네트워크는 보안적으로 안전하다.
3. 네트워크는 동질적이다.
4. 네트워크 토폴로지(구조)는 변하지 않는다.
5. 자연(Latency)은 0이다.
6. 대역이 무한하다.
7. 전송비용이 무료다.
8. 관리자가 하나다.
? 글로벌 시간이 존재한다. -> 해결법으로는 논리적인 시계..? 메시지를 주고 받는 시간으로 조절


### Scaling Techniques(확장성 대표기술)
##### Hiding Communication Latency
`통신의 지연시간을 숨긴다`
메인 프로시저에서 서브 프로시저를 실행시키고 그 실행을 기다리면 동기적
서버와 클라이언트 서버간에도 동기적으로 동작함
비동기적인 방식으로 개발하면 됨
컴퓨터구조에서 interupt의 비동기적인 작업방식과 유사함
***4장 - RPC에서 자세히 설명함***

클라이언트에서 서버로 폼을 보내면
서버측은 두가지 기능을 함 
Check form 입력 값을 검증하는 로직, 
Process form 실제 구현 로직
패킷을 보냈을 때 로직이 틀리면 Check form에서 다시 돌려 보냄
이런 로직을 개선시키는 방법이
Check form을 클라이언트로 넘기는것
그러면 클라이언트의 Local Communication을 하기 때문에 
서버 주변 트래픽을 줄여주고, 서버의 부하를 줄이고, 동작 시간을 줄일 수 있음


##### Distribution
부하를 분산시킴
DNS에서 상위 DNS서버가 하위 DNS서버의 주소를 가지고 있음
이런 식으로 지역적으로 나눔

##### Replication(caching)
다른 노드에 복사본 생성
Replicaiton이랑 Caching은 조금 다름
Caching은 user가 함
Replication은 서버가 함

Distribution과의 차이점은 Distribution은 지역적으로 서비스가 중단될 수 있지만
Replication은 지역적으로 잃어도 원본은 남아 있음 -> 가용성(Availability)이 높다, 중복성이 존재해야함
Replication이 많아야지 엔드포인트가 많아져서 성능이 높일 수 있다.
성능이 낮아지는 경우가 있는데, 영화같은 read-only data라면 괜찮지만
read-write data라면 업데이트가 되어야하기 때문에 업데이트 프로토콜이 필요하다.


# Classification of DSs - DS종류

### Distributed Computing System ; DCS
연산위주의 cpu를 많이 사용하는 경우 유용함
과학기술용 서비스인 경우


### Distributed Information System ; DIS
storage(database)를 이용하는 경우가 많으면 응용함


### DPS

### Cluster Computing Systems
여러가지 형태가 있지만 주로 사용하는 방식으로는
3가지 네트워크가 있음

Master node : 팀장같은 역할, 프로젝트를 따오고, 사원들에게 분배하는 역할, 실제 일은 안하고 관리함
Compute node: 사원같은 역할, 실질적인 일처리를 하는 역할
Parallel aplication : 따온일
Component of Parallel aplication : 따온일 중 한 사원에게 주어진 일
Parallel libs : 각 사원들의 성능, 상황등을 고려해 일을 분배하는 기준, 모니터링, 등등
Management application : 내부의 관리, 프로젝트 따오기와 같은 외부의 관리(Remote Access로 받음)를 책임짐
Remote Access network : Master 노드만 이어짐, 외부 일처리 가져올 때 사용하는 네트워크
Standard network : 모든 노드가 이어짐 모니터링, 전달지시 하달, 일반적으로 사용하는 네트워크
Remote Access network : Compute 노드들만 이어짐, 일처리를 위해서 빠르게 사용할 때 사용하는 네트워크

이런 구조의 Cluster Computing System을 짜고 이러한 구조를 계층구조로 다시 짜면 규모가 매우 커질 수 있음


### Grid Computing Systems
과학기술용, 국가단위
이걸 상업용으로 만든 것이 클라우드 시스템임


### Transaction Processing Systems
Transaction 을 처리하는 시스템
Client가 server에 접근하는게 아니라 TP monitor에 접근함
TP monitor가 필요한 서버의 위치가 어디인지 알고 있기 때문에, 상황마다 적절하게 처리함
TP monitor가 여러개의 머신일 수도 있음, 그래도 지리적으로 같이 있는게 좋음

Transaction Language가 있음
BEGIN TRANSACTION
Mark the start of a transaction

END TRANSACTION
Terminate the transaction and try to commit

ABORT TRANSACTION
Kill the transaction and restore the old values

READ
Read data from a file, a table, or otherwise

WRITE
Write data to a file, a table, or otherwise

ACID 속성을 가지고 있는 db사용

Atomic: To the outside world, the transaction 
happens indivisibly.
Consistent: The transaction does not violate 
system invariants.
Isolated: Concurrent transactions do not 
interfere with each other.
Durable: Once a transaction commits, the 
changes are permanent.

큰 Transaction을 복합 Transaaction이라고 함
하나의 Transaction에 SubTransaction이 있다면 이런 구조를
Nested Transaction이라고 함
이런 Transaction에 대한 처리를 해야함


### Enterprise Application Integration - EAI 시스템
JDBC, ODBC - 서로 다른 DBMS를 서로 같이 사용할 수 있게 만드는 communication middleware
이렇게 기업용 Application을 통합하기 위한 시스템(서버측)


### Distributed Pervasive Systems
분산 확산 시스템
무선 네트워크의 발전으로 나옴(wireless network)

##### Requirements
contextual change(토폴로지같은 구조의 변경, 환경의 변경)를 포용해야 됨
ad hoc - 갑자기 필요시에 라는 뜻, 임시 혹은 가상의 네트워크, 시스템 등을 구축하는 시스템
energy difficient - 모바일 기기에서 베터리를 적절하게 사용하는 것, 전시 사용
ad hoc 서비스를 갖춰야함, 어느시기든 새로운 서비스를 추가할 수 있어야함
자원의 공유를 실현해야함

##### Electronic Health Care Systems
body-area network 에는 다음과 같은 장비들이 들어갈 수 있음
motion sensor
ECG sensor - 심전도 센서
tilt sensor
등등 여러 센서
PDA - 네트워크의 목적이 아닌 일반적인 전자기기, 통신 안되는 핸드폰?
transmitter - 센서에서 온 신호를 외부로 넘겨줌, 게이트웨이?

##### 논점
얻은 데이터는 어디에 저장해야하는가?
crucial(중요한) data 손실을 어떻게 방지하는가?
응급상황 전파및 생성 인프라를 어떻게 구축하는가?
주치의의 온라인 피드백을 어떻게 받을 수 있는가?
견고한 모니터링 설계를 어떻게 실현할 것인가?
환자의 대한 개인정보 유출, security issues를 위해 어떤 적절한 정책이 시행되는가?

##### Sensor Networks - 센서 네트워크


# 2장 ARCHITECTURES

# Architectural Styles
### Layered architectures
OSI7계층이나 운영체제와 어플리케이션의 동작방식과 유사함
하위에 있는 인터페이스를 이용함
![[Pasted image 20231016155614.png]]

### Object-based architectures
객체 기반 아키텍쳐
invokation을 통해 상호작용
![[Pasted image 20231016155625.png]]

### Data-centered architectures


### Event-based architectures
상호작용하는 주체가 2명임 

Subscriber(구독자)
Publisher(출판자)
Event bus - Publisher가 evnet를 넘기는 인프라

store가 없음
![[Pasted image 20231016155707.png]]

### shared data-space architectures
Data-centered architectures + Event-based architectures
store가 있음
![[Pasted image 20231016155724.png]]


# Centralized Architectures
일반적으로 서버와 클라이언트는 다음과 같이 소통함
![[Pasted image 20231016145759.png]]
패킷 로스에 대한 대처를 해야 함 

# Application Layering
일반적으로 서버는 User Interface, Processing, Data
이렇게 3가지 단계로 나눠짐
![[Pasted image 20231016145256.png]]

# Multitiered Architectures
3가지 단계를 서버와 클라이언트 머신이 따로 관리함
![[Pasted image 20231016160047.png]]
a는 비밀번호 입력 제한 과 같은 프로그램
b는 자바의 에플릿 같은 프로그램
c는 
d는 서버가 데이터베이스만 제공
e는 데이터베이스 정보를 캐시하는 겨우

# Decentralize Achitectures 
### Horizontal Distribution(수평적 분산) of fuctionality
### vertircal Distribution 


# peer-to-peer system(P2P system)
각각의 peer들이 data level에서 분할에서 가지고 있음
1. Location of Data item (searching cost, time)
어디에 데이터가 있는지 찾고
using IP address
2. Genuine service cost 
그들 사이에서 다운로드 혹은 스트리밍을 하기 위한 직접적인 연결 구축
이러한 peer를 servent(server + client) 라고도 함 

# Overlay Network
~위에 놓여있는 네트워크
Physical Network혹은 Logical Network 위에 있는 네트워크
Overlay Network 는 Logical Network 임
카카오톡 같은 서비스에서 사용하는 가상의 네트워크
100개의 노드 중에 실제 참여하는 노드는 10개 인 경우
참여하는 노드들끼리 mapping function과 IP 네트워크를 이용해서
네트워크를 구축함
즉, 기존 IP망이랑 다름
logical node
logical channel link
![![/#^Table]]

# P2P System의 분류
Genuine service cost 는 둘 다 비슷함
searching cost 가 차이가 남
## Structured
overlay node들의 구조가 명시적, 체계적, 제한적, 결정적, 선정의된
ring형 토폴로지 
먼저 구조를 정하고 노드를 매핑함

searching cost가 Unstructured보다 적게 듬
임의의 노드가 데이터를 가지고 있는 노드를 forwarding 함  
node management cost가 있음

![[Pasted image 20231016154432.png]]

위와 같은 원형 구조를 Chord라고 함
0~15 는 address space
data item의 식별자이자 node의 식별자이자 키
키는 Destributed hash table 이용해서 적용
그러나 꼭 두 가지 식별자가 같을 필요는 없음
data item보다 node의 수가 일반적으로 적음 
위의 사진에선, 5개의 node와 16개의 data item이 있음
1번 node가 0,1 data item을 다루고
4번 node가 2,3,4 data item을 다루는 방식으로 
자신의 nodeid 보다 작은 data item을 관리함

다음과 같은 operation을 지원 함
- join operation : node가 P2P 네트워크에 참가함
예를들어 10번에 새로운 노드가 들어온다면(10번에 있던 데이터는 사라지는지..?)
10번을 successor, 이전에 관리하고 있던 12번을 desuccessor 라고 함
12번이 10번에게 data 관리 의무를 넘겨 줌
이러한 과정을 data item migration이라고 함
- leave operation : node가 P2P 네트워크에서 나옴
- look-up operation : 키에 해당하는 node의 주소를 리턴 함


![[Pasted image 20231016163951.png]]
위와 같은 구조를 CAN(content data-address network)이라고 함
노드의 식별자를 좌표로 표현
노드가 있는 region을 노드가 관리

새로 노드가 들어오면 spit
![[Pasted image 20231016164134.png]]





## Unstructured
Unstructured P2P Architecture
비구조적, 정의되지 않은
boadcast(flooding) -> 모든 노드에게 물어보기 때문에 비용 발생
node management cost가 없기 때문에 유리할 수 있음

### Pure P2P
특정 노드가 어디있는지 broadcast(flooding)
잘 안씀
일종의 query를 던짐
dns처럼 자신에게 묻는건지 체크하고 맞다면 자신의 위치와 함께 응답
- searching cost가 비쌈
- node management cost가 저렴

### Super-peer Architecture
Pure P2P를 개선함
Peer들을 계층화함
Peer의 종류는 2가지로 나뉨

1. Regular Peer
기존의 일반적인 Peer

2. Super Peer
Regular Peer이지만 추가 역할을 함
Hybrid P2P에서 DS와 같은 역할을 함
해당 Cluster에서 다른 peer를 관장함
자신의 Peer Group과 관련된 요청이라면 Group에 Unicast
아니라면 다른 Super peer에게 Broadcast

- Cluster(Peer Group)
여러 Peer 들의 모임, 아래 그림에선 4개의 클러스터가 있음


![[Pasted image 20231023143445.png]]

Broadcast를 Super Peer에게만 하므로 비용 절감
오버레이 네트워크이기 때문에 IP네트워크에서 사용하는 비트마스킹이랑은 다름(물리적 제약이 없음)
물론 물리적으로 가깝게 Peer Group을 만들어도 되지만 여러가지를 고려할 수 있음

Super Peer가 되기 위한 조건이 있음
- P2P네트워크에 오래있어야 Super Peer가 될 확률이 높음
-  네트워킹이 좋아야하고(bandwidth, speed), 컴퓨팅 파워가 커야 함
-  그 외의 여러 조건을 고려함

### Hybrid P2P
Hybrid Architecture와는 결이 다름
컨텐츠 자체는 기존과 유사하게 Peer들이 나눠서 가지고
컨텐츠 위치는 브로드케스팅이 아닌 하나의 서버에서 관리함
Hybrid P2P 는 Centralized Directory Service임

- Directory Service
컨텐츠 위치(Peer Index)를 알려주는 서비스

- Directory Server
Dirctory Service를 제공하는 서버

DS(Directory Server)는 다른 peer들과 동등한 위치에서,
meta data나 index를 register받음


### Pseduo Code
![[Pasted image 20231023145838.png]]
Overlay Network에서
근접한 노드를 immediate neightbor 라고하고
immediate neightbor 끼리 node info를 전달해줌
하나의 노드가 10개의 neightbor에 대한 정보를 가지고 있다면
해당 노드가 가지고 있는 view를 partial view라고 함

Current Partial view에서 추가 정보가 들어오면 수정을 함
Current Partial view는 queue 형태로 구현(age 기준 정렬 상태)
View의 element는 age 속성을 가짐 늙었으면 dequeue 당함

PUSH_MODE는 자신이 가진 partial view중 하나를 다른 노드로 넘겨줌
자신의 정보를 넣고
자신이 가지고 있는 최신정보를 buffer에 넣어서 상대한테 넘겨줌
PULL_MODE는 다른 노드의 buffer를 받아옴
else문에서 정보를 세팅해놓고 가져가고 싶으면 가져갈 수 있게 하는 로직을 설정함

![[Pasted image 20231023151315.png]]
큰차이 없음




## Topology Management of Overlay Networks

Tcp위에 IP layer를 사용하 듯 overlay를 layer가 있음
추후 추가


## Edge-Server Systems
Netflix 같은 동시에 유저들이 접속하는 스트리밍 서비스, 서버에서 유용하게 사용할 수 있음

- Core Network
백본망 같은 주요 네트워크
- Edge Network
core network가 아닌 하위 단계의 네트워크

Contents Provider에서 Edge Server에 미리 Replication 해놓음
트래픽을 분산시키는 역할

![[Pasted image 20231023154208.png]]



## Collaborative Distributed Systems
Hybrid P2P와 유사함
Dirctory Service를 하지는 않음

pre-rider 방지
다운로드 받을 때 비용을 요청함
모든 Peer가 Contribution을 해야 이용을 할 수 있는 구조(보상 시스템)

![[Pasted image 20231023154310.png]]

- Tracker
특정 파일의 위치를 알고 있는 물리적인 서버
타겟 노드들의 정보를 저장하고 있음

.torrent file에서 Tracker의 정보를 담고 있음
File Server 에서는 .torrent file을 가지고 있음

이때 공헌 여부에 따라 sending rate를 다르게 제공

- Globule
2개 이상의 서버가 Content를 Replication하는 방식
데이터가 없거나 과부화 상태라면  Redirection을 이용함
구현하려면 서로 server status를 monitoring 해야 함


































































###질문