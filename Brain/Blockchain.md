# About Bitcoin
## TMI
08년 Satoshi Nakamoto
09년 1월 비트코인 네트워크 탄생
10년, 피자2판 가격으로 10,000비트코인 지불(최초의 비트코인 거래)

## 특징
별도의 중앙서버가 존재하지 않음
신규 bitcoin은 mining이라 불리는 합의과정 중에 생성
누구나 mining 과정에 참가할 수 있음
모든 transaction은 blockchain을 통해 저장됨(삭제 수정 불가)
물리적/전자적 coin 개념이 없음 
Coin은 transaction들 안에 함축적으로 표현됨
Cryptographic key가 bitcoin의 소유권을 증명함
Bitcoin을 소비하기 위해서는 key를 이용한 전자서명을 생성해야 함 
Key는 보통 wallet(지갑)에 저장해서 사용

## 신규 bitcoin 발행 
Mining에 성공한 채굴자가 보상으로 신규 bitcoin을 획득
난이도 조절을 통해 대략 10분마다 신규 발행
보상 규모는 대략 4년주기로 절반으로 감소 (반감기)
2023년 현재, 채굴당 6.25 BTC 보상
2024년 중반에 3.125 BTC로 감소
비트코인의 총 공급량은 2100만 개로 제한

## 구성요소
- Bitcoin protocol 
A decentralized peer-to-peer network 

- Blockchain 
A public transaction ledger 

- Consensus rules 
A set of rules for independent transaction validation and currency issuance 

- Proof-of-Work (PoW) 
A mechanism for reaching global decentralized consensus on the valid blockchain

## 비트코인 이전의 가상화폐
가상화페가 되려면 아래 3가지를 만족해야 함
위조 변조 방지
double-spending(이중 사용) 방지
돈의 소유권(돈의 주인이 맞는지) 증명

1980년 이미 가상화폐 등장
그러나 여전히 중앙집중형 방식
공격자의 타겟이 됨, 
SPoF(single point of failure,하나가 망가지면 다 망가짐) 문제 발생

## Bitcoin Wallet
지갑과 비슷한 역할
사용자와 bitcoin시스템을 연결해주는 인터페이스 역할
wallet에는 개인 key가 들어있음
지갑을 잃어버리면 돈을 잃듯 개인키가 들어있는 wallet을 잃어버리면 다 잃을 수 있음

Desktop wallet
Mobile wallet
Web wallet
Hardware wallet - 따로 하드웨어가 있음, USB랑 비슷
Paper wallet - 종이에 QR 코드가 찍혀있음

## 역할분류
### Full-node client
모든  Transaction를 저장하고 검증하는 역할

### Lightweight client(SPV client)
자신이 관심있는 Transaction 처리만 담당
Transaction이 필요하면 full-node에 연결해야 함

### Third-party API client
제3자(회사)로 bitcoin 연결

## Bitcoin Core
Full-node 구현체

## 계정 생성 예시
Mycelium설치
계정생성
address생성(ID) - public키로 address를 생성
비트코인 전달하고 싶으면 address로 전달하면 됨
address는 여러 개 생성 가능
이렇게 생성된 address와 private키는 wallet에 저장됨
bitcoin network 입장에서는  생성만 하면 저장되는게 없다가
사용자가 활용하면 저장 시작함

## Bitcoin 획득 방법
기존 사용자로부터 직접 구매
물건/서비스 판매를 통한 획득
ATM 기기를 이용한 구매
Bitcoin 거래소를 통한 구매
우리나라 같은 경우 대부분 거래소 가서 거래함

## 비트코인 구매 예시
1bitcoin은 시장이 결정
돈을 받고 싶은 사람이 address를 보냄
wallet에게 address로 전달 요청
wallet이 자동으로 transcation 생성 후 signing(전자서명)
Bitcoin network에 transaction 전파 - 생각보다 얼마 안걸림
전파된 transaction을 받고 싶은 사람 또한 받음
data structure에는 아직 저장 안 됨(unconfirmed 상태)
거래가 완료되려면(돈 받은 사람이 블록체인을 사용하려면)
transaction이 mining을 통해 블럭체인에 기록되어야 confirm상태가 됨
이러한 과정을 기존 금융 시스템에서 cleaning(청산)이라는 용어로 사용됨
confirm상태가 되면 실제로 사용 가능(거래 종료)


## 비트코인 사용자 분류
- 지갑을 가지고 있는 일반 사용자
- full-node
- 채굴하는 유저(채굴하려면 full-node여야함)
- 상인들
- 거래소
- 개발자

## block chain 구분
### public block chain 
거래 내용이 공개된 블록체인, 인터넷에 공개됨 누구나 참여 가능
일반적으로 transaction은 공개되어 있긴 하지만 일반인들은 접근하기 힘듬
### private block chain 
거래 내용이 비공개된 블록체인, 특정인들만 참여함

## bitcoin search engine
누구나 손쉽게 transaction을 확인할 수 있음

블럭을 열람할 수 있고,
블럭 안에 transaction도 확인할 수 있고,
검색까지 가능

BlockCypher Explorer
blockchain.info

## 거래 예시
![[BIP-21 표준안.PNG.png]]
BIP-21 표준안 참고
alice가 bob의 QR코드를 찍음
QR코드엔 거래 내용과 address 정보, 간단한 설명이 담겨있음
QR코드는 비트코인 URL스키마를 이용해서 만듬
alice가 transaction을 생성
<https://www.blockchain.com/btc/tx/0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2>

# Bitcoin의 동작 과정
## Transactions
한 비트코인을 다른 곳으로 옮기는 역할
input ouput 둘 다 여러 개일 수 있음
Transaction fee(수수료)=(sum of inputs) – (sum of outputs)
채굴에 성공한 사람이 모인 수수료를 가짐
이후  Transaction에 전자 서명한 후 network에 전파

## Transaction Chain
과거에 받은 것 중에 안 쓴 것만 사용 가능
alice에게 비트코인을 줬다면 
Transaction에서는 alice에게 보낸다는 조건을 걸고 (locking)
이 transacito에 적힌 돈을 쓰려면 소유권 증명을 해야 함(unlocking)
input에 있는 항목들은 항상 다른 transactio에 있는 output에서 가져와야 함

## Making Changes
마찬가지로 사용하고 남은(수수료 포함) 잔돈을 
자기 자신한테 보낸다는 조건을 걸면 됨

하지만 일반적으로 자신이 가지고 있는 다른 address에 넣음(익명성을 위해)

UTXO - 현재 비트코인 소유액 - 사용하지 않은 모든 output


## 일반적인 거래 형태
이전에 거래한 모든 소유액을 모두 모은 다음 거래 후 잔돈을 거슬러 받음
output에 맞는 input에 맞는 소유액을 거래에 사용함(잔돈 모두 처리)
하나의 큰 돈을 여러 주소로 보냄 - 월급을 주는 경우

## 올바른 input 가져오기
wallet이 적절한 input을 가져옴
큰 UTXO부터 가져올 수도 있고, 작은 것부터 가져올 수도 있음
full-node가 해당 주소의 모든 거래를 확인해서 정확한 UTXO을 가져옴
full-node가 아니라면 full-node에게 요청
1비트코인=1억억satoshi로 주로 사용함


## Output 생성
Transactinon은 locking을 걸 때, 간단한 스크립트를 걸 수 있음
output의 조각을 사용하려면 본인 인증을 요구하는 스크립트를 검
UTFO를 사용하려면 unlocking을 하기 위한 스크립트를 요구하게 만듬

## Propagating Transactions(tx 전파)
자신이 받은 transaction을 적당히 검사 후 주변으로 전파(flooding)
주인이 맞는지, 유효한 input을 사용했는지 등을 검사
transaction이 전파된 건 맞지만 아직 confirm되지는 않음
모종의 이유로 자신의 transaction이 무시될 수 있음 - 기다려야 함
10분에 하나씩 block만들어짐 -> 거래가 최소 완료되려면 10분을 기다려야 함

빠른 반응이 필요한 상황이라면 transaction이 전달 받기만 하면, 
일단 거래를 하고 나중에 컨펌을 기다림
약간의 리스크가 있지만 이건 지금의 화폐에서도 동일함(신용카드)


## Mining(채굴)
채굴자는 들어온 transaction이 유효한지 체크
채굴자에게는 아직 컴펌되지 않는 transaction을 모아 놓는 pool 이라는 공간이 있음
pool 에 들어온 transaction을 저장
새로운 블럭에 선별된(대체적으로 수수료가 높은) transaction을 넣음
하나의 블럭에는 용량이 있음
수수료는 거래 당사자가 정함 -> 적을수록 채택될 이유가 적어짐
그래서 수수료 시세가 있음
합의 알고리즘(PoW)을 수행 - 컴퓨팅 리소스를 많이 소모됨
운 좋게 mining에 성공이라면 블럭이 전파되고 추가됨

성공하면 
새로운 비트코인이 발행 6비트코인(2억)정도
수수료도 모두 가짐
그러나 리워드가 반감기를 가짐
나중에는 새로운 발행에 대한 보상이 없어지지만 수수료 때문에 계속 채굴할 거라고 예상
또 모든 transaction에 수수료를 나한테 준다 + 새롭게 발행한 걸 나에게 준다는 내용을 가진
transaction을 블럭 처음에 추가해서 블록을 만듬

분산된 시스템에서 합의를 도출하기 어려움
초기에는  한 명씩 뽑아서 돌아가면서 블록을 만들게 함
아무나 뽑히면 안되니까 작업을 열심히 한 사람을 뽑음 -> PoW(Proof-of-Work)

## Pow(합의 알고리즘)
비트코인 채굴자가 참여하는 게임
대략 10분마다 초기화
풀기는 어렵지만 게임을 이겼는지 검증하기는 쉬움
hash함수(SHA256)를 사용 - 단반향이기 때문에 위 게임에 적합

블럭을 추가할 때 임의의 nonce를 추가함
블럭 전체를 해시로 넣음
`256개의 비트중에 앞에서 비트가 10개가 나와야 함` 같은 조건을 줌
그래서 해당 조건에 맞는 nonce값을 넣어보면서 해시 값을 체크해야 됨

10분 안에 채굴을 했는지 채크하기 위해
채굴자의 수를 파악해 난이도를 조절함

## 블록체인은 안전한가?
공격자들이 합심해서 리소스를 모아
block이 쌓이기 직전에 block을 넣으면 대체될 수도 있음
그러나 그 위에 있는 모든 블럭을 모두 바꿔치기 해야 함 - 점점 난이도가 올라감
즉, 시간이 지날수록(대체로 6블록) 더 이상 바꿔치기 할 수 없음
따라서 정말 중요한 거래라면 6번의 컴펌을 기다리는걸 권장한다고 함

## Genesis block
볼록체인의 출발점
현시점 811971째 블럭이 쌓임

# Bitcoin Core

프로그램임
오픈소스임 -> 개선, 사용, 수정 가능
초기에는 satosi client라고 불림
가장 많은 노드가 사용하고 있음 -> 다른 것도 있음

## Bitcoin Core Architecture
![[Pasted image 20231013062642.png]]
사진에서 
커넥션은 좌상단
store는 하단
transaction관련은 좌하단
외부, 인터페이스는 우상단

## main network, test network
main은 실제 동작하는 네트워크
test 테스트를 위한 네트워크 
test에 있는 비트코인은 가치가 없음 호환이 안됨

## bitcoin core 설치
mainnet 안되면 testnet 설치
리눅스 안되면 윈도우로
그러나 리눅스가 더 호환이 잘 됨
SSD 3~400GB 용량 필요(실제론 600 이상 필요)
RAM 4GB이상
인터넷 꽤 빨라야 함

<https://bitcoin.org/en/full-node#linux-instructions>
<https://bitcoin.org/en/full-node#windows-instructions>
<https://bitcoin.org/en/download>


설치한 후
bitcoind - d는 데몬, 윈도우에서 서비스 같은 개념
bitcoin.conf에서 txindex=1 로 인덱싱 속도 빠르게
<https://en.bitcoin.it/wiki/Running_Bitcoin>

bitcoin-cli 
bitcoin core의 정보를 얻어오게 하는 인터페이스
bitcoind에 접근하여 요청을 보냄
다른 것도 가능

상황이 안된다면 클라우드를 사용해야 함
<https://www.linode.com/?r=3c7fa15a78407c9a3d4aefb027539db2557b3765>

## full-node의 장점
로컬에 비트코인 정보를 모두 가질 수 있음
굳이 외부에 가져올 필요가 없음
transaction의 검증을 스스로 체크를 할 수 있음
비트코인 네트워크 입장에서 full-node가 많을수록 견고해짐


## bitcoin core api
![[Pasted image 20231013091914.png]]
JSON-RPC 로 웹서버와 소통함 - client와 bitcoind랑 대화하는 방법
JavaScript Object Notation와 
Remote Procedure Call의 이니셜 - 내부 인터페이스와 소통하는 IPC 와 달리 외부의 서버와 소통하는 방법

코어에서 제공하는 api
<https://developer.bitcoin.org/reference/rpc/index.html>

따라서 bitcoin-cli 말고도 api를 이용해서 데이터를 얻어올 수 있음

예를 들어
Transaction ID (txid) : 0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2
라고 한다면 bitcoin-cli에 다음을 입력하면 json가 인코딩된 형태로 데이터를 얻을 수 있음

`getrawtransaction 0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2`
![[Pasted image 20231013121535.png]]

해당 데이터는 실제 데이터의 해시값이고 실제값은 아래의 함수를 이용하여 가져올 수 있음
`decoderawtransaction [encoding data]`
![[Pasted image 20231013121641.png]]
getrawtransaction에 true 옵션을 넣어주면 디코딩을 2번해 줌

getblockhash 277316 
277316번째 블럭에 있는 모든 transaction을 얻어옴

https://chainquery.com/bitcoin-cli/getrawtransaction
이 주소에서 외부 서버를 이용해 실행할 수 있음

아래와 같이 curl를 통해 루프백 주소를 이용해 bitcoin-core에 접근할 수도 있음
![[Pasted image 20231013122936.png]]

아래는 각각 기본적인 블록체인 정보를, 특정 주소의 balance를 가져오는 코드들
![[Pasted image 20231013123615.png]]

![[Pasted image 20231013123635.png]]


## bitcoin-cli 명령어 모음
- `getnewaddress`
- `dumprivkey [address]`
- `getblockchaininfo`
- `getrawtransaction [txid]`
- `getblock [height]`
- `getblockhash [blockid]`


# Key & Addresses
## Blockchain 과 Cryptography
우리가 사용하는 public blockchain은 암호화 기법이 사용되지 않음
private-blockchain에서는 특정 조직이 사용하기 때문에 encrytion이 많이 사용됨
key : 보안에서 key 공격자에게 알려주면 안되는 것
Digital signature(디지털서명) : 적합한 사용자임을 증명하기 위해 쓰이는 것

## 공개키 암호화 시스템
대칭 키 암호화 시스템 : 암호화할 때 사용하는 키와 복호화할 때 사용하는 키가 같음
공개키 암호화 시스템 : public key와 private key 의 쌍으로 이뤄짐

trap door, one way function - 단방향 함수를 이용하되, 비밀정보가 있으면 쉬움(개구멍)

RSA는 Integer factoring(소인수 분해)을 이용해서 만듬

DSA같은 건 (Discrete logarithm)이산대수 문제를 이용해서 만듬
n=(g^k) mod p 

private 키로 public 키가 만들어짐 (차원곡선 곱셈 이용)
address 는 public 키를 해시해서 만들어짐

## DSA를 이용한 비트코인
ECDSA
비교적 적은 키로도 강력한 암호화 기능을 구축할 수 있는 현대식 암호화 기법
타원곡선을 이용함
아래는 키와 주소 등이 어떤 원리로 생성되는지를 설명함

## 합동

`a mod n`
a를 n으로 나눈 나머지

Congruent modulo m  
합동(mod m세상에서 서로 같음)

`a ≡ b (mod m)` 은 정수 `k`가 `a = b + km` 일 때만 가능
`22 ≡ 4 (mod 9)`

모든 수를 mod 뒤에 있는 숫자 n이라고 하면 0~n-1까지 표현 가능

연산가능 +-*

나눗셈은 안됨

## 모듈러 산술(Modular Arithmetic)
### Residue classes (mod n)
Z는 모든 정수
Zn은 n보다 작은 양의 정수 {0,1,2,3,4,5,...,n-1}
![[Pasted image 20231013065803.png]]

### Reducing k modulo n
![[Pasted image 20231013070020.png]]


## 모듈러 역원(Modular Inverse)
a의 -1승은 a의 역원
`(a, m) = 1 -> ax ≡ 1 (mod m)`

예를들어, `5*3^-1 mod 7` 을 계산하려면, 먼저 `3^-1`을 찾아야 함
```
3*3^-1 ≡ 1 mod 7
3*5 ≡ 1 mod 7
```
따라서 mod 7 에서 3의 역원은 5임.

이어서 계산하면,
```
5*3^-1 mod 7
5*5 mod 7
25 mod 7
4
```
임을 알 수 있음

![[Pasted image 20231013070540.png]]

a가 n과 서로소라면  `(a * b) ≡ (a * c)(mod n) -> b ≡ c(mod n)`

a와 n이 서로소가 아니라면 
a에 Zn을 곱한 a의 배수를 나열한 후 모듈러 연산을 해보면 겹치는 수가 나오게 되는데
이 때문에 Zn과 모듈러 연산 결과 집합 사이의 1대 1 매칭이 되지 않아 
고유한 역수가 없는 상황이 나옴
![[Pasted image 20231013072607.png]]
예를 들어 위의 예시에서 모듈러 연산을 하여 결과 값이 2가 나왔을 때  
12인지 36인지 모르기 때문에 원래의 정수를 알 수가 없음
즉, 나머지 연산의 역연산을 수행하기 어려움

응용하여, 아래의  식을 만족하는 a의 모듈러 역원 k는 n과 서로소 이여야만 함
```plain
(a * k) ≡ 1(mod n) 
```

한편, 확장 유클리드 알고리즘(Extended Euclidean algorithm)을 이용해서 쉽게 모듈러 역원을 구할 수 있음


## 대수체계
```plain
mod9 이런 식으로 사용하면 흔히 9의 세계에서~ 이런 표현을 자주한다. 이때 mod9는 Z9라는 유한체를 갖는다고 하는데, 이 유한체라는걸 설명하기 위해 대수체계의 대한 이해가 필요하다. 그룹은 링을 포함하고 링은 필드를 포함하기 때문에 이전의 조건을 만족하면서 추가적인 조건이 붙는 식이다.
```
### Group
이진 연산자 `·` 에 대해서 다음을 만족해야 함
A set of elements with a binary operation `·`
- Closure(닫힘) If a and b belongs to G, then a · b is also in G 
- Associative(결합법칙) a · (b· c) = (a· b) · c for all a, b, c in G 
- Identity element(항등원) There is an element in G such that a · e = e · a = a for all a in G
- Inverse element(역원) For each a in G, there is an element a’ in G such that a · a’ = a’ · a = e
실수의 경우 합에 대한 항등원이 0이다.
#### A finite group
원소가 유한해야 함
#### Abelian group
교환법칙이 성립해야함
#### Cyclic group
그룹 G 내의 모든 원소가 특정 원소 a의 거듭제곱으로 나타낼 수 있는 그룹
a^k (k는 정수)로 표현할 수 있는 모든 원소가 G에 속한다는 것을 의미
a는 그룹 G를 생성하는 원소로, 이를 "생성자" 또는 "generator"라고 함
모든 G의 원소는 a의 거듭제곱으로 나타낼 수 있음

예를들어 {1,-1,i,-i}는  집합의 요소 i를 이용해서 모든 집합을 나타낼 수 있음
이때 i를 generator라고 함

### Ring
Abelian group에서 추가적으로 2개의 이진 연산자에 대해서 다음을 만족해야 함
A set of elements with two binary operations +(addition),  x(multiplication) 
-  R is an abelian group with respect to addition (실수는 덧셈의 대해 abelian group을 만족함)
identity = 0, inverse of a = -a 
- Closure under multiplication (곱해도 닫힘)
If a and b belongs to R, then ab(=axb) is also in R 
- Associativity of multiplication (곱셈의 결합법칙)
a(bc) = (ab)c for all a,b,c in R 
- Distributive laws (분배법칙) 
a(b+c) = ab+ac for all a,b,c in R 
(a+b)c = ac+bc for all a,b,c in R
#### Commutative(교환가능한) ring
Ring에서 추가적으로 곱셈의 교환법칙이 성립해야 함
예를들어 n차원행렬의 곱은 교환법칙이 성립하지 않으므로  Commutative ring이 아님
#### Integral domain
Commutative ring에서 추가적으로 아래가 성립해야 함
- Multiplicative identity  (곱의 항등원 존재)
There is an element 1 in R such that a1 = 1a = a for all a in R 
- No zero divisors  (두 원소의 곱이 0이 되지 않음)
If a,b in R and ab = 0, then either a = 0 or b = 0

### Feild
Integral domain에서 추가적으로 곱의 역원이 존재함을 만족해야 함
For each a in F, except 0, there is an element a-1 in F such that aa-1 = (a-1 )a = 1
집합을 벗어나지 않고 덧셈, 뺄셈, 곱셈, 나눗셈이 가능함

실수는 필드이지만 정수는 나눗셈이 안되므로 필드가 아님
![[Pasted image 20231014061037.png]]

## 유한체
유한체는 암호학에서 중요한 역할을 함
예를 들면 진법 체계는 유한체임
GF(2)면 이진법 체계
추후에 설명할 타원 곡선은 소수체(GF(p))와 이진체(GF(2^m))을 주로 사용(메인은 소수체)

## Galois Field (GF(p))
Galois field
소수 p에 대한 유한체를 나타냄
유한체의 개수는 무조건 `p^n` 이어야 함
유한체의 원소로 구성된 집합이어야 함
0부터 p-1까지의 정수로 이뤄짐
Coummutative ring
연산은 p로 나눈 나머지에 대한 덧셈, 뺄셈, 곱셈 등의 산술 연산으로 이뤄짐
덧셈과 곱셈에 대한 교환 법칙이 성립
어떤 원소 a의 곱셈에 대한 역원을 가지려면, a와 p가 서로소 여야 함
만약 p가 소수이면, 유한체 Zp 내에서 0이 아닌 모든 정수는 p와 서로소
이때 GF(p)에서 곱셈에 대한 역원을 찾으려면 [[Extended Euclidean algorithm]]을 사용해야 함



## 유한체 구현(Python)
```python
class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(
                num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        # this should be the inverse of the == operator
        return not (self == other)

    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        num = (self.num + other.num) % self.prime
        # We return an element of the same class
        return self.__class__(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two numbers in different Fields')
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        num = (self.num - other.num) % self.prime
        # We return an element of the same class
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two numbers in different Fields')
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        num = (self.num * other.num) % self.prime
        # We return an element of the same class
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in different Fields')
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        # use fermat's little theorem:
        # self.num**(p-1) % p == 1
        # this means:
        # 1/n == pow(n, p-2, p)
        num = (self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime
        # We return an element of the same class
        return self.__class__(num, self.prime)

    def __rmul__(self, coefficient):
        num = (self.num * coefficient) % self.prime
        return self.__class__(num=num, prime=self.prime)
```

![[Pasted image 20231016152735.png]]
![[Pasted image 20231016153033.png]]


## Polynomial Arithmetic
다항식의 계수는 field임
따라서 그러한 다항식의 집합은 polynomial ring
정확하진 않지만 나눗셈도 가능
```
5/3 = ? 
5/3 (in rational numbers)
5*3^-1 mod 7 = 4 (in Z7 )
5 = 1*3 + 2 (in Integer, no solution)

(5x^2)/(3x) = ? 
No solution (polynomial over integers)
4x (polynomial over Z7 )
```

GF(2)에서 다항식의 연산은 다음과 같이 간주됨
- addition = XOR 
- multiplication = AND
- addition = subtraction mod 2
비트연산과 동일

`f(x)=(x^7+x^5+x^4+x^3+x+1)` `g(x)=(x^3+x+1)`
이라면 아래의 연산이 가능함
![[Pasted image 20231016201440.png]]
polynomial ring의 모든 조건을 만족

다항식에서도 유클리드 알고리즘을 통해 gcd를 구할 수 있음
![[Pasted image 20231016201954.png]]


## 타원 곡선(Elliptic Curve)
`y^2 = x^3 + ax + b`형태
타원곡선에서는 덧셈의 대해서만 알면 됨
아래 그림에서 P1+P2는 P3임임
![[Pasted image 20231016202417.png]]

아래 3와 같이 곡선과의 교점이 없는 경우 Point at Infinity (무한 원점, 0) 라고 표현하고,
이 점은 타원 곡선에서 항등원의 역할을 함
이러한 항등원은 추후 키교환, 서명 등의 개념에서 사용됨

타원 곡선에서 곱셈은 자기 자신을 여러 번 더하는 형식
따라서 어떤 점과 정수와의 곱셈만 가능
그래프 상으론 접선의 역할
- 2P=P+P
- kP=P+P+...+P(k times)

![[Pasted image 20231016202742.png]]


## 비트코인에서의 타원 곡선
비트코인에서는 `secp256k1`이라는 타원 곡선을 사용함
계산에 용이하고 안전하다고 알려짐

`p=2^256-2^32-2^9-2^8-2^7-2^6-2^4-2` 라고 할 때,
`y^2 = x^3+7 over Fp` 또는
`y^2 mod p = (x^3+7) mod p`

타원 곡선 상의 정수 점들의 개수는 다음과 같으며,
`Order n = 1.1578*10^77 < 2^256`
이때 백터값 시작점(Generator point)에 개인키 만큼을 곱해서 공개키를 만듬

- G 실제 좌표
x: 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
y: 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8

![[Pasted image 20231016210249.png]]

## Point 구현(Python)
```python
class Point:

    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        # x being None and y being None represents the point at infinity
        # Check for that here since the equation below won't make sense
        # with None values for both.
        if self.x is None and self.y is None:
            return
        # make sure that the elliptic curve equation is satisfied
        # y**2 == x**3 + a*x + b
        if self.y**2 != self.x**3 + a * x + b:
            # if not, throw a ValueError
            raise ValueError('({}, {}) is not on the curve'.format(x, y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y \
            and self.a == other.a and self.b == other.b

    def __ne__(self, other):
        # this should be the inverse of the == operator
        return not (self == other)

    def __repr__(self):
        if self.x is None:
            return 'Point(infinity)'
        elif isinstance(self.x, FieldElement):
            return 'Point({},{})_{}_{} FieldElement({})'.format(
                self.x.num, self.y.num, self.a.num, self.b.num, self.x.prime)
        else:
            return 'Point({},{})_{}_{}'.format(self.x, self.y, self.a, self.b)

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError('Points {}, {} are not on the same curve'.format(self, other))
        # Case 0.0: self is the point at infinity, return other
        if self.x is None:
            return other
        # Case 0.1: other is the point at infinity, return self
        if other.x is None:
            return self

        # Case 1: self.x == other.x, self.y != other.y
        # Result is point at infinity
        if self.x == other.x and self.y != other.y:
            return self.__class__(None, None, self.a, self.b)

        # Case 2: self.x ≠ other.x
        # Formula (x3,y3)==(x1,y1)+(x2,y2)
        # s=(y2-y1)/(x2-x1)
        # x3=s**2-x1-x2
        # y3=s*(x1-x3)-y1
        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x = s**2 - self.x - other.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

        # Case 4: if we are tangent to the vertical line,
        # we return the point at infinity
        # note instead of figuring out what 0 is for each type
        # we just use 0 * self.x
        if self == other and self.y == 0 * self.x:
            return self.__class__(None, None, self.a, self.b)

        # Case 3: self == other
        # Formula (x3,y3)=(x1,y1)+(x1,y1)
        # s=(3*x1**2+a)/(2*y1)
        # x3=s**2-2*x1
        # y3=s*(x1-x3)-y1
        if self == other:
            s = (3 * self.x**2 + self.a) / (2 * self.y)
            x = s**2 - 2 * self.x
            y = s * (self.x - x) - self.y
            return self.__class__(x, y, self.a, self.b)

    def __rmul__(self, coefficient):
        coef = coefficient
        current = self
        result = self.__class__(None, None, self.a, self.b)
        while coef:
            if coef & 1:
                result += current
            current += current
            coef >>= 1
        return result

```


## secp256k1 구현(python)
```python
A = 0
B = 7
P = 2**256 - 2**32 - 977
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141


class S256Field(FieldElement):

    def __init__(self, num, prime=None):
        super().__init__(num=num, prime=P)

    def __repr__(self):
        return '{:x}'.format(self.num).zfill(64)

    def sqrt(self):
        return self**((P + 1) // 4)


class S256Point(Point):

    def __init__(self, x, y, a=None, b=None):
        a, b = S256Field(A), S256Field(B)
        if type(x) == int:
            super().__init__(x=S256Field(x), y=S256Field(y), a=a, b=b)
        else:
            super().__init__(x=x, y=y, a=a, b=b)

    def __repr__(self):
        if self.x is None:
            return 'S256Point(infinity)'
        else:
            return 'S256Point({}, {})'.format(self.x, self.y)

    def __rmul__(self, coefficient):
        coef = coefficient % N
        return super().__rmul__(coef)


G = S256Point(
    0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
    0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
```

![[Pasted image 20231016210806.png]]


## 개인키 생성
0~order n-1까지 램덤한 256비트 데이터
적당한 시드에 대한 암호학적으로 안전한 임시램덤 숫자 Generator(CSPRNG)를 사용하여 생성


## 공개키 생성
G에 생성된 개인키만큼 곱함
백터가 G고 스칼라가 개인키임
이때 모든 유저는 동일한 G를 가지고 있음
공개키를 생성하긴 쉽지만 
이산 대수 문제로 인해 공개키를 통해 개인키를 알아내긴 매우 힘듬

`K= k * G`
해당 식을 계산하여 공개키를 생성함
여기서 G와 K를 알더라도 k를 알아낼 수 없음

이산 대수 문제란 아래에서 문제 제시된 문제처럼 
p, g, (g^a) mod p, (g^b) mod p를 알고 있다고 해도, a나 b의 값을 계산하는 것은 어렵다는 문제

```
1. Alice와 Bob이 사용할 소수 p와 기본 생성자 g를 공유합니다.
2. Alice는 비밀 키 a를 선택하고, Bob은 비밀 키 b를 선택합니다.
3. Alice는 (g^a) mod p를 계산하고, Bob은 (g^b) mod p를 계산합니다.
4. Alice와 Bob은 서로에게 이 값을 전송합니다.
5. Alice는 (g^b)^a를 계산하고, Bob은 (g^a)^b를 계산합니다. 이 두 값은 동일하므로, 공유 비밀 키 K가 생성됩니다.
```

![[Pasted image 20231016211835.png]]


## 개인키 구현(Python)
```python
class PrivateKey:

    def __init__(self, secret):
        self.secret = secret
        self.point = secret * G

    def hex(self):
        return '{:x}'.format(self.secret).zfill(64)
```


## Bitcoin Address 생성
k는 개인키, K는 공개키
생성된 공개키에서 주소 파생
1. public key에서 public key hash
A=RIPEMD160(SHA256(K))
결과값은 20바이트(160비트)
2. public key hash에서 Bitcoin Address
address=Base58Check(A)

[[Encoding]]
- Base64
binary 데이터를 text-based 미디어로 전송할 때 사용하는 인코딩
26 lowercase, 26 capital, 10 numerical, +, /
http, email 첨부 등등에 사용

-  Base58
base64에서 0, O, l, I, +, / 제거
<https://learnmeabitcoin.com/>

- Base58Check
사람이 읽기 쉽고 오타를 방지하기 위한 인코딩 방법
용도에 따라 다른 prefix를 적용(Version Prefix)
메인넷에서는 prefix로 1바이트의 0x00을 붙임
따라서 메인넷 주소는 1로 시작함
테스트넷에서는 0x6f를 사용해서 m또는 n으로 시작함
중간에는 payload가 그대로 들어옴
마지막에 checksum이 4byte 들어옴
checksum은 Payload를 SHA256()를 두 번 인코딩한 후 앞 4byte임
비트코인에서는 사용자가 보는 대부분의 데이터가 이 인코딩으로 되어 있음
간편하고, 읽기 쉽고, 에러를 감지하기 쉬움

![[Pasted image 20231017161708.png]]


## 개인키 형식
개인키를 다루는 방식에는 주로 WIF가 사용됨
- wallets 에서 import, export 됨
- QR코드 지원
![[Pasted image 20231017162635.png]]

![[Pasted image 20231017162702.png]]


## 공개키 형식
공개키에서 사용되는 값은 타원곡선 위의 좌표이기 때문에 다음과 같이 표현 됨
K = (x, y)
![[Pasted image 20231017165842.png]]

- Uncompressed 방식
초기에 사용됐으며, 너무 길어서 비효율적임
65byte
Prefix `04` 에 좌표값들을 이어 붙임
"04" || x || y
![[Pasted image 20231017170013.png]]

- Compressed
K길이를 줄이기 위해 고안됨
y는 어차피 구할 수 있기 때문에 x만 저장함
33byte(32byte키 + 1바이트 prefix)
`y^2 mod p = (x^3 + 7) mod p`

y가 만약 y가 짝수라면 Prefix “02”, 홀수라면 Prefix “03” 을 취함
`Prefix “02” : y is even (negative) 
`Prefix “03” : y is odd (positive)``
![[Pasted image 20231019105551.png]]

비트코인 클라이언트의 기본 방식이지만 전부가 다 Compress만 사용하지 않음
두 가지 방식에서 온 키들로 만든 주소는 서로 다름

- WIF-compressed
위에서 언급한 compressed 방식의 공개키에 WIF 방식을 더하면 됨
이때 suffix는 `01`임
![[Pasted image 20231018122803.png]]
<https://learnmeabitcoin.com/technical/wif>

비트코인에서 WIF-compressed 방식의 주소 생성의 과정을 종합하면 아래와 같음
```
1. 적절한 난수를 선정하고 Private Key(32byte)를 생성
2. 타원곡선 위에 있는 Generator에 Private Key만큼 곱해서 Public Key 생성에 이용될 좌표 생성
3. 해당 좌표를 compressed 방식으로 처리하여 Public key(33byte) 생성
4. Public Key를 SHA256, RIPEMD160 해시함수로 더블인코딩하여 Public Key Hash(20byte) 생성
5. Base58Check 인코딩 방법에 따라 Version prefix(0x80)를 Payload 앞에 붙이고 Checksum을 Payload뒤에 붙인 후 compressed됐음을 나타내기 위해 suffix(0x01)를 추가한 후 Base58Check 인코딩하여 WIF-compressed 주소 생성
```
이 때 생성된 주소는 `K`나 `L`로 시작해야 함(일반적으로 메인넷은 k, 테스트넷은 L)

![[Pasted image 20231019110202.png]]


## Advanced Keys and Addresses
- Pay-to-public-key-hash (P2PKH)
주소가 1로 시작함
주소를 보내려면 디지털 서명과 공개키가 있어야 함

- Pay-to-script (P2SH)
주소가 3으로 시작함
소유자의 키가 아닌 스크립트를 사용
스크립트를 풀어야 사용 가능
A = RIPEMD160(SHA256(script))
Base58Check에서 version prefix를 5로 설정

- Multi-signature
사용하려면 2명 이상의 서명이 필요
M-of-N multisig - Require M signatures (threshold) from a total of N keys
P2SH로 구현

## Vanity Address
`1LoveBPzzD72PUXLzCkYAtGFYmK5vYNR33`
사용자가 읽기 쉬운(식별하기) 쉬운 주소
Brute-force로 생성
보안적으로 위험하지 않음
당연히 단어가 길수록 만들기 기하급수적으로 어려워짐
![[Pasted image 20231019121102.png]]


## Paper Wallets
종이에 개인키를 프린트한 것
주소가 있을 수도 있음
오프라인 상에 저장해서 안전할 수도 있음(cold storage)
백업 목적으로도 가능
BIP-38 임임
<http://bitaddress.org/>
![[Pasted image 20231019121151.png]]





# Wallet
사용자 친화적, 안전한, 유동적인 wallet
데이터 저장 구조와 사용자의 키를 관리하는 방법
실질적인 `coin`은 blockchain에 저장되어 있고,
Wallet은 관리하는 역할
관리하는 방식에는 키 간의 독립성에 따라
Non-deterministic wallet(JBOK), Deterministic wallet(HD) 로 나눠짐

## Non-deterministic Wallet (Type-0)
key pair를 램던으로 선정
Original Bitcoin Core가 100개의 키를 미리 만들어 놓고 시작함
백업, 관리, import하기 불리함
주소 재사용 가능성이 생김
`비추`

## Deterministic Wallet (Type-1)
seed로로 난수를 정하고, hash함수를 이용해 개인키 추출
시드로부터 모든 키를 복구할 수 있음
생성 시 백업을 만들 수 있음
wallets 간에 migration이 자유로움
하나를 잃으면 모두를 잃음

## HD Wallet (Type-2)
BIP-32/BIP-44
가장 많이 사용함
type1의 키 파생 + 트리구조
부모키는 자식키를 파생시킬 수 있음
브랜치별로 용도를 다르게 사용할 수 있음
개인키 없이 공개키를 생성할 수 있음 -> 위험한 서버에 공개키만 저장
![[Pasted image 20231020085228.png]]


## Mnemonic Code Words 
BIP-39
12~24글자 문자열이 램덤한 시드가 됨
Mnemonic code(연상 코드) + HD wallet
easy backup & recover
Easy to read & transcribe(따라적기)
사실상 업계 표준임
![[Pasted image 20231020111144.png]]


## Generating Mnemonic Words
Random entropy : 128~256 bits
Mnemonic code : 12~24 words
![[Pasted image 20231020111506.png]]


## From Mnemonic To Seed
PBKDF2(Password Based Key derivation Function 2)
무차별대입공격을 막기 위해 Key-stretching 함수를 사용
위에서 구한 Mnemonic code에 비밀번호 같은 salt를 추가함(사전대입공격 방어)
HMAC-SHA512 해시 함수로 2048번 돌려 512-bit짜리 Seed를 구함
<https://iancoleman.io/bip39/>
![[Pasted image 20231020113205.png]]


## Seed로 부터 HD Wallet 생성하기
### Master Keys 생성
- CSPRNG로 난수생성
- Mnemonic code words 생성
- HMAC-SHA512로 512비트 Seed 생성
- 왼쪽 256비트는 마스터 개인키(m)
- 오른쪽 256비트는 마스터 체인코드
- 타원곡선을 이용해 마스터 개인키로 264비트 마스터 공개키(M) 생성 
![[Pasted image 20231020113412.png]]
![[Pasted image 20231020114431.png]]

### Private Child Key 파생
CKD (Child Key Derivation) function
parent public key로부터 child key가 파생
HMAC-SHA512로 생성됨
부모의 개인키 혹은 공개키, 그리고 부모의 chain code, 32bit의 index number로 해시값을 만듬
해시값 중 왼쪽 256비트 + 부모의 개인키 256비트를 더하여 child의 개인키를 구함

child key로부터 parent key, sibling key를 알아낼 수 없음
각각의 child private key로 bitcoin address를 생성할 수 있음 

![[Pasted image 20231020114812.png]]
![[Pasted image 20231020114818.png]]

### Public Child Key 파생
개인키 없이 공개키만으로 child key가 파생됨
노출되도 안전한 공개키만 전개됨
해시값 중 왼쪽 256비트 + 부모의 공개키 256비트를 더하여 child의 공개키를 구함
- Store public key on a web server (for receiving via various addresses)
- Store private key in a cold-storage or hardware wallet (for spending)
- Private key is not stolen when the server is compromised

그러나 부모의 chain-code가 여전히 필요함
![[Pasted image 20231020120258.png]]

### Extended Key
부모의 공개키로 모든 자식노드의 공개키를 생성할 수 있음 
one (private or public) key(256bit) || one chain code(256bit)
Base58Check encoded with special version #

- Extended private key (xprv)
Can derive all descendant private & public keys
xprv9tyUQV64JT5qs3RSTJkXCWKMyUgoQp7F3hA1xzG6ZGu6u6Q9VM NjGr67Lctvy5P8oyaYAL9CAWrUE9i6GoNMKUga5biW6Hx4tws2six3b9c

- Extended public key (xpub)
Can derive all descendant public keys
xpub67xpozcx8pe95XVuZLHXZeG6XWXHpGq6Qv5cmNfi7cS5mtjJ2tgy peQbBs2UAR6KECeeMVKZBPLrtJunSDMstweyLXhRgPxdp14sk9tJPW9


### Hardened Child Key Derivation
Extended Key를 사용하게 되면 보안적인 문제점이 발생
```
일반적으로 xpub는 공개될 수 있음
xpub에는 Parent Chain Code + Parent public key 가 들어있기 때문에
Parent Chain Code + Parent public key + index로 
1. 모든 child의 private key가 노출당함
만약 이 상황에서 하나의 child private key가 노출된다면
주소를 특정할 수 있게 되고
타원곡선의 연산을 이용해 해당 주소의 child public key를 얻을 수 있게 됨
자식의 개인키는 부모의 개인키 + 해시값 왼쪽 256비트 이므로
2. 해시값과 자식의의 개인키를 알고 있으므로 역산으로 부모의 개인키까지 알아낼 수 있음
3. 같은 방식으로 HD Wallet에 있는 모든 주소를 알아낼 수 있음
```

![[Pasted image 20231020132232.png]]

이러한 취약점을 해결하기 위해 Hardened Child Key Derivation을 이용함
부모의 개인키를 이용해서 자식의 개인키(공개키는 해당 없음)를 파생 시킴
자식과 부모 키 사이에 일종의 방화벽을 만드는 효과
xpub을 공유할 때 유용

![[Pasted image 20231020132703.png]]


### Key Identifier
키를 트리 구조로 관리하게 되면 찾기도 불편할 수 있음
Key Identifier를 이용하여 해결

- Index number
Used in key derivation (32bit)
0x00000000 ~ 0x7FFFFFFF : normal derivation
0x80000000 ~ 0xFFFFFFFF : hardened derivation

- Key identifier
Use the path from root to the key
m : private key, M : public key
0 : first child, 0’ : first hardened child
/ : separate tree level

![[Pasted image 20231020133112.png]]


### HD Wallet Tree Structure
BIP-44
Multi-account hierarchy for deterministic wallets
Handle multiple coins, multiple accounts and addresses

![[Pasted image 20231020133540.png]]
 - purpose’ : 44’ (constant)
 coin_type’
 Bitcoin mainnet : m/44’/0’
 Bitcoin testnet : m/44’/1’
 Litecoin : m/44’/2’
 - account’
 Divide wallet into independent accounts
 Ex) m/44’/0’/0’ , m/44’/0’/1’
 - change
 0 : external chain
 1 : internal chain (거스름돈 전용)
 - address_index

![[Pasted image 20231020133720.png]]



# Transaction
## Tx 자세히 분석하기
block-explorer에 있는 정보는 실제 tx에 있는게 아니라 따로 만든 정보들임
실제론 balance, address, input등이 없음
![[Pasted image 20231020145238.png]]


## Tx Output
비트코인 화폐는 `satoshi`라는 가장 작은 화폐 단위로 이뤄져 있고 더 이상 나눠지지 않음
1BTC=100만 `satoshi`
블록체인에 기록되어 있음
전체 네트워크에서 인식됨

- UTXO(Unspent Transcation Output)
아직 사용이 안된 모든 Output
Full Nodes에 의해서 추적됨
Tx는 UTXO들로 상태를 전이 시킴

Wallet은 자기가 가지고 있는 키 중에 하나로 사용 가능한 UTXO를 찾아냄
빠른 참조를 위해 로컬 DB를 사용하기도 함

UTXO는 나눠지지 않음
쓰려면 한 번에 다 써야 함
Wallet은 필요한 금액을 UXTO에서 적절하게 고르는 각자의 알고리즘이 있음
만약 필요한 금액보다 크다면 Charge UTXO가 생성됨

![[Pasted image 20231024153119.png]]
- scriptPubKey
사용하기 위한 조건을 Output에 걸 수 있음 
locking script, witness script, or scriptPubKey

- Serialization
데이터 구조를 단순 byte stream으로 바꾸는 과정
네트워크를 통해 전송하거나, 파일 형태로 저장할 때 사용
![[Pasted image 20231024160724.png]]
![[Pasted image 20231024154234.png]]
하이라이트 되어있는 부분이 실제 Output을 직렬화한 것에 대한 부분이다. 


## Tx Input
사용될 UTXO가 명시되어 있음
소유권에 대한 증명이 제공됨

Wallet은 각각의 UTXO마다 input을 Tx안에 만듬

![[Pasted image 20231024155518.png]]
txid : reference the tx containing the UTXO being spent 
vout : output index in the referenced tx above (from 0) 
scriptSig : unlocking script for spending

UTXO 정보와 수수료 계산, 다른 노드들을 검증하기 위해서 다른 Tx를 검색해야 함
단순한 연산자지만 다양한 과정과 Tx가 필요

input 부분을 직렬화 한 것은 다음의 하이라이팅 된 부분
Sequence Number는 일정기간 동안 입력을 막는 용도로 사용
![[Pasted image 20231024160734.png]]
![[Pasted image 20231024160742.png]]


## Tx Fee
Miner를 보상
공격자가 공격을 불가능하게 만드는 요소
Miner들은 Fee를 우선순위로 둠

처음에는 고정된 Fee를 사용했지만
Tx의 길이에 따라 Fee를 다르게 책정함
Wallet들이 알아서 책정함

Tx에는 실제로 fee에 대한 field가 없음
input에서 output을 빼서 암시적으로 나타냄
실수로 fee를 너무 크게 잡았다면 그리고 이미 전파했다면 돌이킬 수 없음
*실제로 이런 이유로 20 비트코인을 1비트코인으로 만들어서 19비트코인이 날라감


## Coinbase Transaction
각 블럭에 첫 번째에 위치하면서 채굴에 성공했을 때 블럭 보상과 Tx fee를 주는 Tx
UTXO를 소모하지 않음
100번 확인 이후에 사용할 수 있음


## Transaction Script
일종의 언어이지만 보안성, 안정성 이슈를 위해서 튜링 완전하진 않음
예를 들어 반복문이 가능하다면 스크립트에 의도적으로 무한루프를 돌게 할 수 있고, 
이는 Tx 승인 지연, DoS공격, 블록 크기 증가 등의 문제가 생길 수 있음

Stack-based 언어
사용 조건을 걸기 위해 UTXO안에 Locking Script 사용
TX를 검증할 때 input에서 사용되는 Unlocking Script
반복문, 복잡한 분기문 불가
복잡도에 제한, 실행시간 예상할 수 있음
논리폭탄, 무한 루프 방지
state를 저장하지 않음(실행결과를 메모리에 저장하지 않음, 의존성이 없음)
스크립트 안에 모든 정보가 있음
자신뿐만 아니라 모든 시스템이 script를 검증함


## Script 생성
- Locking script
output의 조건을 검
scriptPubKey로 불렸지만, 더 많은 가능성 내포

- Unlocking script
output의 조건을 해결
모든 transaction input 안에 있음
대부분 사용자의 전자서명이 들어있음
scriptSig(서명 스크립트)라고 불림

- 검증
각각의 비트코인 노드가 검증함
Locking script와 Unlocking script를 실행시켜봄

![[Pasted image 20231024173518.png]]


## Script Excution Stack
말 그대로 stack 기반으로 동작함
왼쪽에서 오른쪽으로 실행
`[Unlocking script]+[Locking Script]` 한 후 실행

X항 연산자인지에 따라 Push or pop 1 or more items
OP_ADD : pop 2 items → add items → push result
OP_EQUAL : pop 2 items → push TRUE(1) if equal
마지막이 TRUE면 valid

![[Pasted image 20231024173930.png]]
![[Pasted image 20231024173945.png]]


## Pay-to-Public-Key-Hash(P2PKH)
일반적으로 P2PKH 스크립트 이용, 가장 상용화 됨

OUTPUT은 
public key hash(address)로 UTXO를 잠금
공개키 해시값(주소)으로 잠궈서 공개키를 공개하지 않음

INPUT은
ECDSA 알고리즘을 이용해 private key로 서명을 생성함
TX 입력을 자신의 개인키로 서명하여 그 서명을 TX 입력 스크립트에 포함

이러한 서명은 이전 UTXO의 소유자인 송신자가 이 트랜잭션을 생성했음을 증명
내가 이 서명을 사용하겠다는 의사를 확인 + 소유자가 맞는지 확인

![[Pasted image 20231024175945.png]]

![[Pasted image 20231024175949.png]]

![[Pasted image 20231024175955.png]]

![[Pasted image 20231024180011.png]]

![[Pasted image 20231024180026.png]]



## ECDSA(Elliptic Curve Digital Signature Algorithm)
ECDSA는 비트코인 및 다른 암호화폐에서 트랜잭션 서명과 블록 생성에 사용되는 주요 알고리즘
ECDSA를 통해 개인키로 트랜잭션 서명을 생성하고, 공개키를 사용하여 해당 서명을 검증

개인키와 메시지의 해시를 사용하여 서명 값(n)을 계산
`n=(g^k) mod p`
여기에서 n은 서명 값, g는 곡선 위의 기본점 (base point), k는 개인키, 그리고 p는 소수 모듈러 (prime modulus)

이때, 개인키의 모듈러 역원 k가 사용되며 이는 확장된 유클리드 알고리즘으로 구함
계산된 모듈러 역원 k를 사용하여 서명 값 r 및 s를 생성
이러한 서명 값은 ECDSA 서명의 일부이며, 메시지의 무결성을 검증하는 데 사용


![[Pasted image 20231024190205.png]]
![[Pasted image 20231024190228.png]]




## Signature Hash Types (SIGHASH)
서명의 대상 = 전부를 서명하는 게 아님
문서에 동의함
문서의 무결성?(integrity - 진실성)
Sighash 가 일종의 flag - 어디서부터 어디까지 서명했다는 의미
![[Pasted image 20231019141204.png]]
아래는 모든 값을 서명함
![[Pasted image 20231019141221.png]]

기본적으로 input은 해시 처리해야 함
None이면 output을 처리하지 않음
Single은 하나의 output을 포함해서 서명함 
정하는 방법은 *검색*
각각의 input마다 서명이 되어 있고, 서로 다른 signhash가 있음
주로 All을 많이 사용

- ANYONECANPAY flag
0x80으로 시작
다른 flag와 조합해서 사용 가능
오직 자기 자신 하나의 input만 서명
여러 사용자가 하나의 tx로 전달하고 싶을 때 사용
서명을 input에 해당하는 대상만 각각 서명함
![[Pasted image 20231019141653.png]]
![[Pasted image 20231019142143.png]]


- ALL | ANYONECANPAY
주로 클라우드 펀딩을 할 때 사용
처음 tx를 만든 사람이 input 하나와 output 모두를 서명함
input만 추가할  수 있게 됨, tx 확장

- NONE
백지 수표같은 개념
받는 사람이 원하는 만큼 금액을 적고 사용할 수 있음
비트코인을 주는게 아니라 tx 자체를 줌
받은 사람은 tx의 output만 수정하면 됨

- NONE | ANYONECANPAY
dust collector?
낙전수입?
비트코인을 사용하다 보면 작은 잔돈이 모임
이 잔돈들을 하나의 트렌젝션에 모음
input이 하나의 잔돈의 역할


## Bitcoin Addresses, Balances, and other Abstractions
흔히 외부 explorer는
tx의 정보를 구체적으로 알려줌
비트코인의 구조는 심플하기 때문에 연결된 다른 tx의 정보들을 적절히 활용함
예를들어 실제로 block안에 input은 없고 utxo를 찾아가야 함
그곳에 있는 script에 있는 public key hash를 보고  address를 유추해냄
수수료도 input과 output을 계산해서 보여줌

P2PKH 말고 다른 방식을 사용하는 tx도 있음
이전의 wallet에서 처리를 못하게 될 수도 있음
호환성이 좋은 wallet을 사용해야 함



# Advanced Transactions and Scripting

## Multisignature
M-of-N scheme
n 명 중에 m명이 서명하면 인증 
- Locking script
`2 <Public Key A> <Public Key B> <Public Key C> 3 CHECKMULTISIG`

- Unlocking script
`<Signature B> <Signature C>`

- Scripts together
`<Signature B> <Signature C> 2 <Public key A> <Public Key B> <Public Key C> 3 CHECKMULTISIG`

![[Pasted image 20231102141946.png|300]]

- 장점
standard script를 사용하면 n이 3명 까지만 재함됨
P2SH 를 사용하면 최대 15명까지 들어남

1명의 사용자가 의도적으로 3개의 서명을 만들어서
분실, 도난의 위험을 줄임
백업 키들도 다시 Multisignature로 관리하여 분실 방지

- 예시
2-of-2 : 2-factor authenication wallet
2-of-3 : parents’ saving account for child
2-of-3 : 에스크로(escrow) 서비스 - 중개자가 거래에 참여함(당근마켓?)


## CHECKMULTISIG의 bug
스택에서 M+N+2만큼 pop해야 함
CHECKMULTISIG가 실제로 pop을 하나 더 하는 버그가 발견
그런데 블록체인은 버그 픽스가 힘듬
그래서 Unlocking script 앞에 쓰레기 값을 하나 더 붙이기로 함
![[Pasted image 20231102143855.png]]



## Pay-to-Script-Hash (P2SH)
2012년 처음 소개
긴 스크립트를 단순화하기 위해 만들어짐
![[Pasted image 20231102144109.png]]
키가 여러 개가 들어가면 수수료가 많이 발생하게 됨

P2PKH에서 publickey 뿐만 아니라 스크립트에서도 인증하게 해주는 것이 P2SH
길게 적어야 했던 스크립트 속 키들을 해시 처리 함
먼저 공개키가 같은지 확인 후 
따로 관리하는 Redeem Script로 확인
Unlocking Script에서 redeem script를 제공

![[Pasted image 20231102144623.png|600]]

기존의 publickey로 만든 address 대신 P2SH는 redeem script를 이용해 address를 이용해 만듬
3으로 시작
![[Pasted image 20231102150852.png|600]]

- 장점
스크립트가 짧음
스크립트가 아닌 주소만 있으면 됨
스크립트를 주는 사람이 만듬
스크립트 자체가 블록체인에 기록되진 않음
받는 사람에게 비용을 대신 부가할 수 있

- 주의점
호환 문제
recursive를 막음 - edeem script 자체가 다른 P2SH 스크립트의 해시를 포함해서는 안 된다는 것
스크립트가 오류가 있다면 그것을 고치기가 어려움(풀 수 없는 스크립트에 비트코인에 묶일 수 있음)


## Data Recording Output (RETURN)

금융뿐만 아니라 데이터 저장을 목적으로 블록체인이 사용하기 시작함
return operator 뒤에 80바이트 데이터를 입력할 수 있음
input, output이 없고, 수수료만 조금 있음

- Proof of Existence
계약서 같은 공증을 저장 
저작권, 소유권 등을 증명
[DOCPROOF](https://proofofexistence.com/)



## Timelock
바로 거래를 주는 게 아니라 일정 기간 후에 유효하게 만듬
![[Pasted image 20231102152601.png|400]]



## Transaction Locktime
tx가 유효해지는 가장 빠른시간을 정의함
절대적 시각으로 locktime으로 함
일반적인 tx는 locktime이 0임 - 바로 전
특정시간을 절대적 시각으로 설정할 수도 있지만
블럭의 높이로도 절대적인 시각으로 설정할 수도 있음
0 < nLocktime < 500 million : block height
nLocktime >= 500 million : Unix Epoch timestamp (sec since Jan 1, 1970)

![[Pasted image 20231102153135.png|600]]

![[Pasted image 20231102152812.png|500]]

- 문제점
지금은 아직 블록체인에 올라간 상태가 아님
중간에 똑같은 UTXO를 다시 다른 사람한테 보낼 수 있음
double-spending 문제


## Check Lock Time Verify (CLTV)
soft fork upgrade?
Dec 2015 (BIP-65)

- CHECKLOCKTIMEVERIFY
output에 들어가는 operator

locking script에 CLTV opcode 를 추가하여 fullnode가 검증
블록체인에 올라간 상태가 되기 때문에 검증이 가능
nlocktime의 용도가 바

![[Pasted image 20231102153802.png]]
![[Pasted image 20231102153808.png]]


## Relative Timelock
상대적인 시각
순서가 중요한 거래

- Transaction-level
Use nSequence (BIP-68)
- Output-level
Use CHECKSEQUENCEVERIFY opcode (BIP-112)


## nSequence
일반적으로 1로 채워서 사용
맨 앞이 0이면 timelock이 걸리는 걸로 인지
22번째는 어떤 방식으로 체크할 건지 
input마다 시간설정가능
tx는 모든 input이 지나야 유효
double-spending문제가 있음

![[Pasted image 20231102154611.png]]



## CSV
CHECKSEQUENCEVERIFY
nSequence랑 같이 사용하여 상대적 timelock을 구현
UTXO’s locking script에 추가
CLTV와 유사한 동작

```gpt
단순히 `nSequence`만 사용하는 경우, 거래가 네트워크에 의해 언제 유효한지만을 정의할 수 있으며, 이는 거래의 스크립트 내에서 직접적인 조건으로 사용되지 않습니다. `CHECKSEQUENCEVERIFY`는 스크립트 수준에서 nSequence 조건을 강제하는 기능을 추가함으로써, 거래의 유효성을 더 세밀하게 제어할 수 있도록 합니다.
```


## lightning network
비트코인의 성능이 높지 않음
tps(tx per second) 가 매우 낮음
체크카드는 1000tps가 나옴 비트코인은 3,4tps
성능을 올리기 위해서 bitcoin network 위에 network 를 하나 더 올림
소액 결제를 잘 묶어서 작은 tx로 만듬
보증금 예치금 등의 개념이 들어감 
이런 개념을 위해서 timelock이 필요해 

![[Pasted image 20231102154946.png]]



## Script with Flow Control
분기문 역할
nesting 가

![[Pasted image 20231102160424.png]]


## Guard Clause
condition역할
- VERIFY
if와의 차이는 조건이 만족하지 않으면 죽음

![[Pasted image 20231102160700.png]]


## Flow Control 사용하기
true가 1

multisig도 구현할 수 있음
![[Pasted image 20231102160746.png]]

script B 실행
![[Pasted image 20231102160751.png]]

복잡한 스크립트 예시
Multisig scheme with timelock 

Mohammed, 2 partners Saeed & Zaira, company lawyer Abdul 
3 partners make decisions based on a majority rule (2 must agree) 
In case of key problem, lawyer can recover with 1 of 3 partners (after 30 days) 
If all partners are unavailable, lawyer can manage directly (after 90 days)

![[Pasted image 20231102161414.png]]
![[Pasted image 20231102161525.png]]


## Segregated Witness
세그윗이라 부름
Aug 2017 (BIP-141)
scriptSig가 비워짐
tx 밖으로 빼냄
구조적인 변화가 필요

![[Pasted image 20231102162056.png]]



## Segwit이 필요한 이유
tx전체에 대해서 전자 서명을 하게 됨
전자서명 자체는 안전함 그러나 원래의 tx에서 1비트정도 바뀔 수 있음
이러면 전체 tx를 해시해서 만들어진 txid를 바꿀 수 있음
double-spending?
이를 방지하기 위해 만들어진 tx를 따로 빼서 서명함

- 그 외의 장점
script versioning
tx의 사이즈가 꽤 작아짐, 수수료 감소, 효율성, 성능

- 주의점
하나의 tx이긴 하지만 input마다 segwit이 따로 적용됨

soft fork에 의해서 업그레이드 됨?

fork란 블록체인을 업그레이드를 한 것을 말함
- soft fork
하위 호환성을 보장함
- hard fork
하위 호환성을 보장하진 않음

업그레이드를 안한 기존의 노드들도 invalid하다고 판단하진 않음(soft fork)
초기에 바로 적용한 것이 아닌 노드의 90프로가 업그레이드 될 때까지 기다림
현재는 잘 적용


## Pay-to-Witness-Public-Key-Hash (P2WPKH)
P2PKH에서 segwit을 적용
![[Pasted image 20231102163729.png]]


## Pay-to-Witness-Script-Hash (P2WSH)
![[Pasted image 20231102163923.png]]







# The Bitcoin Network
## Bitcoin Network
P2P 네트워크를 이용
No server, no centralized service, no network hierarchy
Resilient, decentralized, and open

torrent - 대규모 파일들 저장, file sharing

## Node Types and Roles
- Network routing
All nodes
Validate and propagate txs & blocks
Discover and maintain connections to peers
- Blockchain database
Maintain a complete and up-to-date copy of the blockchain ledger
- Mining
Compete to create new blocks (Proof-of-Work)
- Wallet
Desktop bitcoin client / mobile lightweight wallet
![[Pasted image 20231109141912.png]]
![[Pasted image 20231109142119.png]]


## Extended Bitcoin Network
- Mining pool
개인 채굴자들의 모음
Ex) Stratum protocol

![[Pasted image 20231109142924.png]]
![[Pasted image 20231109143014.png]]


## Bitcoin Relay Network
Overlay network on bitcoin network
miner들 때문에 생김
신규블록을 빨리 받을수록 빨리 참여할 수 있으므로 채굴에 유리해짐
Overlay network를 이용해 latency를 줄임
Created in 2015
Fast synchronization of blocks between miners
Specialized nodes on Amazon Web Service infra
전세계에 몇 개씩 있음

- Fast Internet Bitcoin Relay Engine (FIBRE)
위의 설명에서 UDP로 바뀜
Replace original network in 2016
Compact block optimization

- Falcon


## Network Discovery
지역적 파편화를 방지하기 위해 램덤으로 노드를 찾음

- DNS seeds
신규 노드들에게 램덤한 노드들의 정보를 제공
주기적으로 크롤링함
전세계에 많이 있음
Special DNS servers providing a list of IP address of bitcoin nodes
Some seeds provide a static list of stable nodes
Some seeds provide a random subset of nodes collected by crawling
bitcoin core 안에 이미 DNS seeds의 주소가 있음

- peer끼리 연결
TCP connection
port 8333
Handshake with version message
![[Pasted image 20231109144021.png]]

- Address propagation
handshake가 끝나면 주변 노드에게 연결된 노드의 정보를 전파

- Address discovery
요청하면 해당 노드 주변 노드의 정보를 가져옴

90분정도 유지하다가 응답없으면 끊어졌다고 가정하고 다른 노드 찾음
Dynamic network adjustment without any central control
![[Pasted image 20231109144643.png]]


## Full Node
Only know genesis block embedded in the client SW
Have to synchronize to construct a complete blockchain

- A node checks version msgs
(contain BestHeight) from its peers

- Exchange getblocks msg
Hash of top block on its local blockchain

- The node having longer blockchain sends inv(inventory) msg
Hashes of the first 500 blocks to share

- The node missing these blocks issues getdata msgs
Request the full block data with identifying the block using hash

![[Pasted image 20231109150454.png]]



## SPV Nodes
전체 블록 노드가 있는 건 아님
Download only block headers (no txs in each block) (~50MB) - 블럭의 메타데이터 같은 데이터
P2P transacting → settled on the blockchain ledger through nodes
Cannot construct full UTXO set

![[Pasted image 20231109150939.png]]
![[Pasted image 20231109150951.png]]

![[Pasted image 20231109151500.png]]

double spending 문제가 남아있어서 중요한 결제에서는 사용 지양

아래의 방법으로 검증
- Existence of a transaction in blockchain
Link the tx and the block including it using Merkle proof
Need block header & Merkle path

- Check depth of tx
Depth : how deep the tx is buried by blocks above it
Confirmed as valid if depth >= 6

![[Pasted image 20231109152202.png]]



## Bloom Filter
SPV node uses bloom filter to ask other peers for txs
Matching a specific pattern without revealing which the node search for
익명성 훼손 문제
![[Pasted image 20231109152751.png]]

N bit field
M hash functions - Output is 1~N
![[Pasted image 20231109153126.png]]
![[Pasted image 20231109153455.png]]
![[Pasted image 20231109153501.png]]
![[Pasted image 20231109153539.png]]

정확히 패턴에 일치하는 것 뿐만 아니라 비슷한 패턴도 보내게 됨


# Blockchain

## Blockchain Data Structure
Ordered, back-linked list of blocks of transactions
Blocks are stored in files
Block metadata is stored in LevelDB

![[Pasted image 20231109154302.png]]

- fork
A block has just one parent
A block can have multiple children temporarily -> 이걸 fork라고 부름
Different blocks are discovered simultaneously by different miners
Eventually, only one child block becomes part of the blockchain
![[Pasted image 20231109154649.png]]
## Block Structure
![[Pasted image 20231109160538.png]]


## Block Header
현재 블럭은 이전 블럭의 헤더 부분에 대한 해시값을 가지고 있
![[Pasted image 20231109160631.png]]


## Block Identifiers
- Block hash (block header hash accurately)
Hashing block header through SHA256 twice → 32 bytes
블럭 안에 blockid가 없음 직접 돌려봐야 함
Not included in the block structure
Genesis block

- Block height
Block’s position in the blockchain
Max block height : 814,331 on October 29,2023
Genesis block - Block height 0
Not a uniquely identify a block - 2 or more blocks might compete due to fork


## Immutability
불변, 변조X

![[Pasted image 20231109161213.png]]


## Genesis Block
모든 노드가 동일함
Statically encoded within SW - 하드코드로 박혀있음
Cannot be altered
Every node always knows it
Secure root to build a trusted blockchain
![[Pasted image 20231109161756.png]]


## Linking Blocks
![[Pasted image 20231109162248.png]]


## Merkle Tree
Binary hash tree
Summarize and verify the integrity of large data set

Summarize all txs in a block
Merkle root : digital fingerprint of the entire tx set

Used to verify whether a tx is included in a block
Need only O(log N) hashing with N txs in a block

![[Pasted image 20231109162419.png]]

![[Pasted image 20231109162451.png]]

![[Pasted image 20231109162644.png]]

Proving a tx K is included in the block
With merkle path of K + merkle root
Merkle path of K = { HL , HIJ, HMNOP, HABCDEFGH }
형제 노드랑 실제로 해시 돌려보면서 root값이랑 일치하는지 체크

![[Pasted image 20231109162900.png]]



![[Pasted image 20231109163354.png]]



## Bitcoin’s Test Blockchains
- Testnet
Fully featured live P2P network
Testnet coins are worthless
Mining is easy

테스트넷용 비트코인을 획득할 수 있음
[획득 주소](http://tbtc.bitaps.com)

- Regtest
나 혼자 돌릴 수 있는 시스템
Local blockchain for testing purpose
Run as closed system
Single node only, or add other nodes
![[Pasted image 20231109163956.png]]

- Development process
Test your code locally on a regtest
Switch to testnet for dynamic environment
Deploy code on mainnet


[설명 참고](https://developer.bitcoin.org/examples/testing.html)
![[Pasted image 20231109164131.png]]
![[Pasted image 20231109164139.png]]

새 주소 생성
![[Pasted image 20231109164244.png]]

reward가 100블록 뒤에 오기 때문에 101블럭 mining
![[Pasted image 20231109164251.png]]

50 빗코 획득
![[Pasted image 20231109164258.png]]

다른 새 주소 생성
![[Pasted image 20231109164438.png]]

10 빗코 전송
![[Pasted image 20231109164501.png]]

아직 컨펌 안됨
![[Pasted image 20231109164510.png]]

컴펌 완료
![[Pasted image 20231109164518.png]]














# Mining and Consensus
## Intro 
Mining은 새로운 코인을 만들어내기 위함이 아니라 청산(clearing)을 위해 만들어짐
기존의 중앙화 시스템에서는 간단했던 Clearing 과정이 분산시스템에서는 다소 어려울 수 있음
이를 해결하는 과정이 Mining
신뢰할 수 없는 환경에서 신뢰할 수 있는 공통된 합의을 만들 수 있게 유도하는 장치
Mechanism for decentralized clearinghouse
합의를 이끌어내는 과정
Secure bitcoin system & enable consensus w/o central authority

전파가 완료되어야 confirm - 블록에 기록됨
confirm이 되어야 비트코인 네트워크에 있는 노드들이 합의된 것 - 사용가능

비트코인 보상이 반감기를 가지는 이유는 인플레이션 막기 위해


## Decentralized Consensus
Mining 보다 consensus가 더 넓은 범위, 더 추상적인 개념
다른 블록체인 시스템에서는 채굴말고 다른 방식에 consensus를 사용
Global public ledger
모든 노드를 믿을 수 없음
Instead, full node has a complete copy of blockchain it can trust
Blockchain is assembled independently by every node
Every node can arrive at the same conclusion as everyone else

- Consensus process
Independent verification of each tx
Independent aggregation of txs into a new block (mining)
Independent verification of new block and assembly into a blockchain
Independent selection of the main chain

각각 독립적으로 동작함

## Independent Verification of Tx
모든 노드가 모든 tx에 대해서 아래와 같은 내용을 검증함
검증 후 propagation
![[Pasted image 20231123074247.png]]


## Aggregating Txs into Blocks
transaction pool - 검증된 tx
candidate block - Mining node aggregates these txs 
coinbase는 miner가 직접 만듬
![[Pasted image 20231123074510.png]]

P2SH를 구현할 때 2가지 방식이 나왔었는데 그 때 투표를 위한 결정이 지금까지 남은게 `/P2SH/`라고 함
![[Pasted image 20231123075129.png]]


## Constructing Block Header
위에서 블럭의 body 부분을 만들었다면 이 부분은 head 부분임
![[Pasted image 20231123075655.png]]


## Mining the Block
헤더에서 Nonce제외하고 바꿀 수 없음
Hash block header repeatedly with different random nonces

- Hash properties
For the same input, output can be easily calculated & verified by anyone
Hard to find inputs to produce a desired fingerprint (one-wayness)
Inputs with small different produce very different outputs
![[Pasted image 20231123075905.png]]


## Proof of Work (PoW)
Find a nonce that produces hash output starting with 0 (hexadecimal) 
Find a hash output less than the target 
Target : 0x1000000000000000000000000000000000000000000000000000000000000000
![[Pasted image 20231123080204.png]]
첫째 자리가 0인 해시값을 찾는건 확률적으로 `1/16`의 확률임 = 16번 돌려보면 solution을 찾을 수 있음

Target은 Target보다 작은 해시값을 찾게 만드는 수임
Target이 작을 수록 찾기 힘들어짐(Target의 크기와 난이도는 반비례)

누가 어디서 solution을 찾았는지는 모르지만, 얼마나 걸릴지는 쉽게 예측 가능함
miner들의 hashpower도 알 수 있음

Competition-based consensus algorithm

- Target
Target은 블럭에 명시되어 있음
Target bits in block 277,316 = 0x1903a30c
exponent (2 digits) || coefficient (6 digits)
target = coefficient * 2(8*(exponent–3))
target = 0x03a30c * 20x08*(0x19-0x03) = 0x03a30c * 20xB0 = 0x0000000000000003A30C00000000000000000000000000000000000000000000 
60 leading 0s 
A miner processing 1 TH/sec needs 59 days on average

- Retargeting
2016 블럭마다 새롭게 설정함
New Target = Old Target * (Actual Time of Last 2016 Blocks / 20160 minutes)

## Validating New Block
![[Pasted image 20231123083523.png]]


## Assembling and Selecting Chains of Blocks
- Main chain 
Valid chain having the most cumulative PoW (greatest-cumulative-work)
Longest chain in most cases 
- Secondary chains
Branches with blocks valid but not included in the main chain 
Kept for future reference (in case of switching)
![[Pasted image 20231123083452.png]]

한 Miner가 바라보고 있는 메인 체인이 다를 수 있음(network delay, 동시에 채굴 등등)
이런 경우 branch가 생김
서로 다른 branch끼리 switching이 생길 수 있음, main이 바뀜
시간을 짧게 보면 consistency가 깨질 수 있음
그러나 길게 보면 consistency가 유지됨


## Blockchain Fork

![[Pasted image 20231123084610.png]]
2명의 miner가 동시에 채굴에 성공함
각각의 블럭을 추가함
![[Pasted image 20231123084627.png]]

서로 second chain으로 관리함
![[Pasted image 20231123084736.png]]

정상적으로 한 명만 mining 성공 - 전파
가장 긴 체인을 메인으로 선정
consistency 유지
![[Pasted image 20231123084826.png]]

Almost fork is resolved within 1 block 
Probability for a fork to extend to 2 blocks is very low
1-block fork occurs every day
2-block for occurs few weeks

블럭 생성 시간이 너무 짧으면 fork가 자주 발생함

## Hashing Race
![[Pasted image 20231123085451.png]]
Hashing power has increased exponentially
CPU mining → GPU mining → FPGA mining → ASIC mining


## Extra Nonce
난이도가 너무 높아져서 모든 nonce(4byte)를 해봐도 안될 때 명시
timestamp를 바꿔가면서 다시 시도
이래도 안되는 경우가 생겨서 coinbase tx에 있는 nonce(8byte)를 추가
Extra Nonce를 변경 -> 머클트리 변경 -> 머클 루트 변경 -> 블록해시 변경

## Mining Pool
Miners collaborate to pool their hash power and share reward
안정적인 수익구조
성공하면 pool서버로 감 - 서로 나눔

cheating을 막기 위해 더 쉬운 문제를 제출받음
쉬운 문제를 얼마나 풀었는지에 따라 수익을 분배함


## Consensus Attacks
암호학적인 공격은 불가능
최근 블럭에 대해서 약간의 훼방 정도의 수준임임


## 51% Attack
현재 비트코인 power의  과반수가 넘는 power를 가지고 있다는 가정하에 가능한 공격
원래의 사실과 다른 악의적인 체인을 기존의 main보다 빠르게 생성해 main을 switching하게 만듬
double-spending, dos공격에 사용

Wait at least 6 confirmations before giving the painting

51% guarantees almost attack success, but not mandatory
Attacks with 30% are possible (studied by statistical modeling)

지금은 하기엔 네트워크가 너무 크고, 가능해도 네트워크 자체가 타격을 입어 제대로된 구실을 하기 힘들기 때문에 실재적으론 불가능함


## Changing Consensus Rules
중앙화 서비스의 소프트웨어같은 개념
Hard fork vs. Soft fork
위에 설명된 fork와 조금 다른 개념
consensus rule을 바꾸기 위한 장치

## Hard Fork
분기 이후 서로 호환되지 않음
그 이후로 다시 수렴할 수 없음
![[Pasted image 20231123101722.png]]

- Software fork 
Alternative bitcoin client with new rules is developed 
Some nodes adopt and run this implementation

- Network fork 
Nodes with old client rejects txs & blocks with new rules 
Network partition 
Old nodes remains connected to only old nodes 
- Mining & chain fork 

Once a miner with new rules mines a block 
Mining power & chain forks 
New miners will mine on top of the new block 
Old miners will mine a separate chain

Hard Fork를 하려고 했지만 실패 (Bitcoin XT, Bitcoin Classic, Bitcoin Unlimited cases)

의도하지 않지만 Fork가 발생하기도 함 - 버클리 DB
구현 이슈 때문에 생김
During upgrade of Bitcoin Core 0.7 to 0.8

의도적으로 Fork가 발생하기도 함 - bitcoin classic
성능 때문에 TX 크기를 늘림
성공적으로 됨
Forked at block 478558 (1 Aug. 2017)

Hard fork is risky
자주 사용할 수 없음, 준비해야 함, 많은 커뮤니티 동의가 필요


## Soft Fork
서로 호환이 됨
실제로 Fork가 나오진 않음
천천히 따라오게 만듦

- Soft Fork
Soft fork with redefining NOP opcodes
Bitcoin has 10 NOP opcodes
Soft fork can modify the semantics of a NOP code

- CHECKLOCKTIMEVERIFY (BIP-65) 
Re-defined NOP2 
Clients implementing BIP-65 : valid as a locktime code 
Clients not implementing BIP-65 : valid as a NOP code

Soft fork with other ways
There will be other ways yet to be discovered
segwit


## Soft Fork Signaling
분기를 시작할 때 Activation이라고 표현
signaling - Miner들이 얼마나 새로운 규칙을 적용되었는지 확인하는 방법
그 후 activation함
Activation of a soft fork
Transitioning to new consensus rules
Signaling mechanism
Show miners support (ready & willing to enforce) for rule change

- BIP-34 signaling & activation
New rule - Coinbase tx contains block height
Signaling - Miners (ready for BIP-34) set block version to 2 (instead of 1)
Activation - 
If 75% of recent 1000 blocks are marked with version 2
Version 2 blocks must contain block height in coinbase tx
Version 1 blocks are still accepted
When 95% of recent 1000 blocks are version 2
Version 1 blocks are no longer valid
All new blocks must comply with new rules

BIP-66 (version 3), BIP-65 (version 4)

한번에 하나의 소프트워트만 할 수 있음
버전이 제한적임
거부를 못함

- BIP-9 signaling & activation
Block version as a bit field - Each 29 bits used simultaneous signal readiness for different proposals
비트 단위로 업데이트
동시에 29개 업데이트를 진행할 수 있음
Maximum time for signaling & activation - Not activated within timeout, the proposal is rejected
업데이트가 잘 진행이 안되면 타임아웃하는 기능 
Count signals in retarget period of 2016 blocks - Activated if # of blocks signaling for a proposal exceeds 95%
2016개의 블럭이지나면 activated
![[Pasted image 20231123103716.png]]


## Consensus SW Development

구성원들이 서로의 목소리를 내어 견제하는 형태가 됨
No authority to coordinate
권력이 기울지지 않음
Decision cannot be made unilaterally by any groups
95% threshold for soft fork reflects consensus by majority

Both hard fork & soft fork has risks
Change is difficult
Consensus forces compromise
t makes this system strong






# Bitcoin Security
기존 시스템과 다르게 중앙화 시스템이 아님
기좀 금융 시스템과 다르게 보안적인 관점이 다름
개인이 들고 있는 금과 유사함 - 소유권, 책임저야하는 주체 등등

## Security Principles
- In a centralized model
Traditional bank or payment network
Depend on access control (authentication & authorization)
Prevent exposure of user’s private info (credit card number,…)
Keep bad attackers out of the system
Secure transaction
Secure end-to-end communication - 서버에서 클라이언트까지의 패킷이 다니는 경로애서의 보안
Encrypt stored transactions
- In Bitcoin
Control and responsibility are on the users
Transactions cannot be forged or modified
Not reveal private information
No need of encryption or secure channel
No traditional access control
However, securing keys are hard to normal users

- Root of trust
여러 계층을 나눠서 보안성을 높임
믿을 수 있는 root 기준으로 다음 계층을 점검
Ex) TPM, Root CA
![[Pasted image 20231130154525.png]]

Blockchain ledger is the root of trust
Genesis block as the root of trust
Build a chain of trust up to current block
Fully validated blockchain is the only trusted thing




# Blockchain Applications
단순 금융 시스템이 아니라 일종의 플랫폼으로서 동작하게 만듬

![[Pasted image 20231130151934.png]]

## 어플리케이션 개발 관점 비트코인의 특징
- 중복 사용 방지
- 불변성
- 중립성
- 안전한 타임스탬프
- 인증과정
- 감시가 가능해야 함
- 새로운 비트코인을 만들 수 없음
- tx에는 기한이 없음
- 무결성
- Tx atomicity(Tx is either (valid & confirmed) or not) - 애매한 상태가 없음
- 값을 나눌 수 없음(Tx output cannot be divided or partially spent)
- 여러 사용자가 컨트롤할 수 있음(Multisignature)
- 타임락, aging 기능 제공
- Relication - 애초에 풀노드가 복제된 데이터임
- 위조 방지
- 지속성 - 모든 유저가 동일한 데이터를 볼 수 있음
- 외부 상태를 기록하는 기능(OP_RETURN)
- 반감기를 통한 인플레이션 조절


# Bitcoin Applications
- Proof-of-Existence (digital notary) 
공증 서비스
EX) 그림을 블록체인을 통해 자신의 것을 증명함
Immutability + Timestamp + Durability

- Kickstarter (Lighthouse)
일종의 크라우드 펀딩 제품
Consistency + Atomicity + Integrity

- Payment channels
라이트닝 네트워크?
Quorum of control + Timelock + No double spend + Non-expiration + Neutrality + Authorization



# Payment Channels and State Channels
비트코인은 tps(초당 tx수)가  3~7 정도됨, 너무 낮음
둘 사이의 거래를 위한 채널을 생성 초기 거래 상태와 끝난 후의 상태만을 블록체인에 작성
Virtual channel like TCP stream
성능 향상이 목적



## State Channel
- funding tx
보증금 정리?

- commitment tx
실제 거래 내역이 담겨있음
비트코인 네트워크에는 들어가 있지 않음
최근 데이터가 이전 데이터를 무효화 하게 만들어야 함 - 추후 설명

- settlement tx
청산, 정산의 개념 내포
최종적인 결과 state가 나옴
블록에 기록 - 채널 종료

![[Pasted image 20231207141753.png| 300]]

중간에 연결이 끊어졌을때를 대비해 가장 최근 데이터를 비트코인에 올릴 수 있음
단, 가장 더 최근 데이터가 있으면 덮어씌여짐 


## Simple Payment Channel
단방향 지불 용도 채널

- Fabian
서비스 제공자
비디오 제공 시간 만큼 비트코인을 받음
0.01 mBTC per sec = 36 mBTC per 1 hour
- Emma
서비스 이용자
비트코인 제공자

![[Pasted image 20231207142849.png|300]]

### funding tx
- tx가 많을 예정이므로 채널 생성
- 1시간 분량의 36mBTC을 보증금의 형태로 미리 받음
- 2-of-2 multisig address를 사용
- 각각의 키가 있고, 새로운 주소가 생김, 두 명이 올바른 서명을 해야 만들 수 있음
- 둘 다 합의해야 사용할 수 있음
- 이 funding tx를 비트코인에 기록 - 채널 생성 완료

### commit tx
- 돈의 일부를 지불하고 남은 돈 돌려받는다는 tx를 만들고 서명
- Fadian도 서명
- 두번째에도 똑같이 


### settlement tx
- 사용한 만큼 지불하고 나머지 보증금을 환급하는 tx 생성성

![[Pasted image 20231207143554.png|300]]



### 악의적 사용자에 대한 대책

- nLocktime 사용
환불을 위한 refund tx를 만듬 - 1달 후 회수
채널의 유효기간 refund tx의 nLocktime
tx마다 시간 줄여서 나중 tx가 더 높은 우선순위를 가지게 만듬
채널에서 사용할 수 잇는 블럭에 수가 많아야 4000개정도 밖에 안되서 제한이 많음
![[Pasted image 20231207150800.png|500]]




## Asymmetric Revocable Commitments
철회 가능한 tx
양방향 거래
나쁜짓하면 손해보게 만드는 구조..?










# GPT 질문

- 이용자 증가로 거래가 계속 많아지면 풀노드들의 용량 문제를 어떻게 해결?
```
이 문제에 대한 몇 가지 해결책은 다음과 같습니다:

1. **스케일링 솔루션**: 블록체인 프로토콜은 스케일링 솔루션을 도입하여 처리량을 늘릴 수 있습니다. 예를 들어, 비트코인은 Lightning Network와 같은 두 번째 계층 솔루션을 통해 블록체인 위에서 작동하는 더 빠른 마이크로 거래를 지원하고, 이로써 기존 풀노드의 부담을 줄입니다.
    
2. **분산 스토리지**: 풀노드가 모든 블록체인 데이터를 저장하지 않고, 일부 데이터만 저장하는 방식을 도입하는 것이 가능합니다. 이를 통해 용량 문제를 완화할 수 있으며, 이러한 방식은 블록체인의 일부 구현에서 이미 사용되고 있습니다.
    
3. **하드웨어 업그레이드**: 풀노드 운영자들은 필요한 경우 하드웨어를 업그레이드하여 더 많은 용량과 처리 능력을 확보할 수 있습니다.
    
4. **샤딩**: 몇몇 블록체인 플랫폼은 샤딩(sharding) 기술을 도입하여 네트워크의 데이터를 분할하고 각 샤드에 대해 별도의 풀노드를 운영함으로써 확장성을 향상시키고 용량 문제를 완화합니다.
    
5. **가벼운 클라이언트**: 일반 사용자들은 풀노드 대신 가벼운 클라이언트를 사용할 수 있습니다. 가벼운 클라이언트는 블록체인 데이터의 일부만 다운로드하고 다른 노드에서 필요한 정보를 검색하여 전체 노드보다 적은 용량을 필요로 합니다.
```


- 비트코인이 코인의 양을 제한하는 이유
```
1. **인플레이션 방지**: 비트코인은 고정된 공급량을 가지고 있기 때문에 새로운 비트코인이 무한정으로 생성되지 않습니다. 이는 통화의 가치를 안정화시키고 인플레이션을 방지하는 데 도움이 됩니다.
    
2. **희소성 제고**: 비트코인의 제한된 공급량은 희소성을 높입니다. 희소한 자원일수록 그 가치가 더 커질 가능성이 있으며, 비트코인은 이러한 희소성을 부각시키기 위해 설계되었습니다.
    
3. **신뢰 구축**: 비트코인의 공급량 제한은 사용자들에게 신뢰를 제공합니다. 중앙 은행 또는 정부의 개입이 없는 분산된 통화로서, 사용자들은 새로운 코인의 무제한 생성을 걱정하지 않고 신뢰할 수 있습니다.
    
4. **경제적 자극**: 비트코인은 채굴자들에게 블록 생성과 트랜잭션 처리를 위한 보상으로 비트코인을 제공합니다. 이러한 보상은 채굴자들에게 경제적 자극을 제공하며, 네트워크의 보안과 안정성을 유지하는 데 도움이 됩니다.
    
5. **결제 시스템 운영**: 제한된 공급량을 통해 비트코인은 결제 시스템으로 사용하기에 적합합니다. 공급량이 고정되어 있으면 사용자들은 코인의 가치가 빠르게 하락하지 않을 것으로 예측할 수 있으며, 이는 결제 시스템에서 안정성을 제공합니다.
```


- 신규 발행되는 코인이 없어지면 수수료만으로 mining을 해야하는데, 그러면 수요를 맞추려면 수수료가 올라가고 공급을 맞추게되면 광부들 메리트가 떨어지게 되는거 아닌지?
`채굴자의 메리트가 저하되는 것은 채굴자의 관점에서는 사실일 수 있습니다. 그러나 이러한 변경은 암호화폐 생태계의 지속성과 보안을 확보하기 위한 조치입니다. 수수료가 채굴자에게 더 중요한 수익원으로 작용하면서, 높은 거래 수수료를 지불할 의향이 있는 사용자들에게 혜택을 주고, 채굴자들은 네트워크를 유지하고 보안을 강화하는 역할을 수행하게 됩니다.`

- 비트코인에는 유통기한 같은 게 있는 건지?
`비트코인은 유통기한이나 만료일이 없는 암호화폐입니다. 비트코인은 블록체인 기술을 기반으로 하며, 그 발행량 및 유통은 프로토콜에 의해 조절됩니다`

- Mining을 할 때 문제는 누가 주는 건지?
`각 마이너는 동일한 블록을 만들려고 하는 것이 아니라 자신만의 블록 헤더를 생성하여 해결하려고 하는 독립적인 과정을 수행합니다. 하지만 이들이 풀어야 하는 문제의 조건은 동일하며, 이 조건을 충족시키면 블록을 만들 수 있습니다.
`
- 곱셈에 대한 역원이라는게 모듈러 역원이랑 완전히 동일한건 아닌거야?
```
정확합니다. "곱셈에 대한 역원"과 "모듈러 역원"은 밀접하게 관련되어 있지만, 완전히 동일한 개념은 아닙니다.

1. **곱셈에 대한 역원 (Multiplicative Inverse):** 이 개념은 일반적으로 그룹 또는 반군에서 사용됩니다. 원소 "a"의 곱셈에 대한 역원은 다른 원소 "b"가 존재하여 "a * b"가 항등원(일반적으로 1)이 되는 경우를 나타냅니다. 이 개념은 유한체(Finite Field)에서도 사용되며, 원소 "a"에 대한 역원은 다른 원소와의 곱셈에 대해 역수를 의미합니다. 이는 어떤 원소를 다른 원소로 나누는 것과 관련이 있습니다.
    
2. **모듈러 역원 (Modular Inverse):** 이 개념은 모듈러 산술에서 사용됩니다. 특히, 원소 "a"의 모듈러 "n"에 대한 역원은 다른 원소 "b"가 존재하여 "a * b ≡ 1 (mod n)"를 만족하는 경우를 나타냅니다. 이는 원소 "a"를 모듈러 "n"에 대해 나눌 수 있는 원소를 의미합니다. 모듈러 연산에서 역원은 나머지 연산의 역수와 관련이 있습니다.
```
- 유한체의 개수는 왜 무조건 `p^n` 이어야 하지?
```
다양한 중요한 수학적 및 알고리즘적 특성을 만족하기 때문입니다. 이러한 특성은 유한체 이론과 관련이 있습니다.

아래에 몇 가지 관련된 이유를 설명하겠습니다:

1. **항등원:** 유한체의 크기가 "p^n" 형태라면, 항등원(1에 대한 곱셈의 항등원)이 존재합니다. 항등원은 곱셈에 대한 중요한 개념이며, 유한체의 구조를 보존하는 데 중요합니다.
    
2. **결합법칙:** "p^n" 크기의 유한체에서 곱셈은 결합법칙을 만족하며, 모든 원소 간의 곱셈이 정의됩니다.
    
3. **역원:** "p^n" 크기의 유한체에서 모든 0이 아닌 원소는 역원을 가집니다. 즉, 어떤 원소에 대한 역원을 찾을 수 있으며, 이것은 나눗셈의 가능성을 의미합니다.
    
4. **대수체의 특성:** "p^n" 크기의 유한체는 대수체(Algebraic Field)라고도 불리며, 수학적 연구 및 알고리즘 설계에서 중요한 역할을 합니다.
    
5. **유한체 이론:** 유한체 이론은 암호학, 오류 정정 부호, 유한체 기반의 다양한 알고리즘 및 통신 분야에 널리 적용되며, 이러한 분야에서 "p^n" 크기의 유한체는 효율적인 계산을 가능하게 합니다.
```

- 우연히 서로 다른 두 명이 로컬에서 동일한 개인키로 주소를 만들었고, 한명이 tx를 block에 올린다음 다른 한 사람이 tx를 만들고 전파하면 reject? 
```
서로 다른 두 명이 동일한 개인 키로 트랜잭션을 만들 경우, 블록체인 네트워크에서 두 번째 트랜잭션은 거부될 것입니다.
```

- 튜링 완전하다는게 뭐지?
```
1. 계산 가능성(Computability): 튜링 완전한 언어나 시스템은 어떤 종류의 계산이라도 수행할 수 있습니다. 이는 어떤 프로그램을 작성하여 어떤 문제든 해결할 수 있다는 것을 의미합니다.
    
2. 반복(Loops) 및 조건문(Conditionals): 튜링 완전한 언어는 반복문과 조건문과 같은 제어 구조를 사용하여 다양한 계산을 수행할 수 있습니다. 이로써 복잡한 알고리즘을 표현할 수 있습니다.
    
3. 임의의 메모리 액세스: 튜링 완전한 언어는 메모리에 읽고 쓸 수 있는 능력을 갖추고 있으며, 이를 통해 데이터를 저장하고 조작할 수 있습니다.
    
4. 무한 루프: 튜링 완전한 언어나 시스템은 무한 루프를 생성할 수 있으며, 이는 계산이 끝나지 않는 프로그램을 작성할 수 있음을 의미합니다
```

- 중복되는 정보가 많아보이는데 실제로는 스크립트가 하나만 저장되는지?
![[Pasted image 20231024174339.png]]
```
네, 실제로 블록체인에서 스크립트는 "hex" 형태로 저장되며, "asm" 형태의 스크립트는 블록체인에 저장되지 않습니다
```


- G에 개인키만큼을 곱했을 때 나온 공개키의 좌표가 정수인 이유?
```
타원 곡선 암호학에서 공개 키의 좌표는 정수 값이어야 합니다. 이것은 암호학적 연산의 특성으로 정해진 것입니다. 타원 곡선 암호학은 유한 체(Field) 상에서 작동하며, 연산 결과는 해당 유한 체 내의 정수입니다.

타원 곡선 암호학에서 사용되는 타원 곡선은 유한 체에서 정의되며, 모든 연산은 해당 유한 체 내에서 수행됩니다. 곡선 상의 점은 정수 좌표로 표현됩니다. 따라서 개인 키와 생성자 "G"를 곱한 결과인 공개 키의 좌표도 해당 타원 곡선의 유한 체 내의 정수 값입니다.

결과적으로, 공개 키의 좌표는 항상 정수 값이며, 이러한 특성을 타원 곡선 암호학의 안전성과 보안성을 유지하는 데 사용됩니다.
```

-   HD wallet에서 parent의 공개키를 이용해서 child의 공개키를 만들수도 있고, parant의 개인키를 이용해서 child의 개인키를 만든다음 다시 K=kG를 이용해서 child의 공개키를 만들수도 있는거야?
```
네, HD (Hierarchical Deterministic) 지갑에서는 부모 키로부터 자식 키를 파생시키는 두 가지 주요 방법이 있습니다. 이 두 가지 방법은 BIP32 및 BIP44와 같은 Bitcoin 개선 제안 (BIP)에서 정의되어 있습니다.

1. **부모의 공개 키를 사용하여 자식의 공개 키 생성:** 이 방법은 주로 공개 키의 확장에서 사용됩니다. 부모의 공개 키와 자식의 인덱스를 사용하여 자식의 공개 키를 파생합니다. 이 방법은 보안적으로 안전하며, 부모 키의 노출로부터 자식 키의 노출을 방지합니다.
    
2. **부모의 개인 키를 사용하여 자식의 개인 키 생성 후 공개 키 파생:** 이 방법은 부모의 개인 키와 자식의 인덱스를 사용하여 자식의 개인 키를 먼저 파생하고, 그 개인 키를 사용하여 자식의 공개 키를 생성합니다. 이 방법은 부모의 개인 키를 노출시킬 수 있으므로 주의가 필요합니다.
```



































































































