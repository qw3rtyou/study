# ~~호환성~~
~~python3 커맨드를 사용하거나
python3.6 혹은 2.7을 사용해야지만 pwn모듈 import가능~~


# 설치
```sh
sudo apt-get update
sudo apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential 
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pwntools
```


# 사용법

pwntools 모듈을 임포트

	from pwn import *

​
디버깅할 때 좋음 무슨 입력을 했고, 어떤 출력을 받았는지 잘 보여줌

	context.log_level = 'debug'

### remote

	remote("주소", 포트)
	`p=remote("host3.dreamhack.games",12294)`

nc 서버에 접속할 때 주로 쓰임

```python
r=remote("")

class remote(sock):
    def __init__(self, host, port,
                 fam = "any", typ = "tcp",
                 ssl=False, sock=None, ssl_args=None, *args, **kwargs):
        super(remote, self).__init__(*args, **kwargs)

        self.rport  = int(port)
        self.rhost  = host

        if sock:
            self.family = sock.family
            self.type   = sock.type
            self.proto  = sock.proto
            self.sock   = sock

        else:
            typ = self._get_type(typ)
            fam = self._get_family(fam)
            try:
                self.sock   = self._connect(fam, typ)
            except socket.gaierror as e:
                if e.errno != socket.EAI_NONAME:
                    raise
                self.error('Could not resolve hostname: %r' % host)
        if self.sock:
            self.settimeout(self.timeout)
            self.lhost, self.lport = self.sock.getsockname()[:2]

            if ssl:
                self.sock = _ssl.wrap_socket(self.sock,**(ssl_args or {}))

    def _connect(self, fam, typ):
        sock    = None
        timeout = self.timeout

        with self.waitfor('Opening connection to %s on port %d' % (self.rhost, self.rport)) as h:
            for res in socket.getaddrinfo(self.rhost, self.rport, fam, typ, 0, socket.AI_PASSIVE):
                self.family, self.type, self.proto, _canonname, sockaddr = res

                if self.type not in [socket.SOCK_STREAM, socket.SOCK_DGRAM]:
                    continue

                h.status("Trying %s" % sockaddr[0])

                sock = socket.socket(self.family, self.type, self.proto)

                if timeout is not None and timeout <= 0:
                    sock.setblocking(0)
                else:
                    sock.setblocking(1)
                    sock.settimeout(timeout)

                try:
                    sock.connect(sockaddr)
                    return sock
                except socks.ProxyError:
                    raise
                except socket.error:
                    pass
            self.error("Could not connect to %s on port %d" % (self.rhost, self.rport))

    @classmethod
    def fromsocket(cls, socket):
        """
        Helper method to wrap a standard python socket.socket with the
        tube APIs.
        Arguments:
            socket: Instance of socket.socket
        Returns:
            Instance of pwnlib.tubes.remote.remote.
        """
        s = socket
        host, port = s.getpeername()
        return remote(host, port, fam=s.family, typ=s.type, sock=s)
```

remote는 이렇게 되어있다. 

이 안에서는 소켓 통신을 진행하고 있음

​
### process
remote는 서버 접속이라면, process는 로컬 파일 접속

	process("파일 이름")

또한 이것과 연계해서

	r = process("파일 이름")
	gdb.attach(r)
	
옵션으로 gdb.attach(r, "실행될 명령어")를 쓰기도 한다. break 거는데 유용


### 데이터 주고받기
recv(개수) - 입력한 개수 만큼 출력을 받는다.
recvuntil(문자) - 입력한 문자까지만 입력을 받는다.
recvline() - 한 줄을 받는다.(\n을 받으면)
recvn(개수) - 바이트 크기 만큼 받아서 data에 저장
recvall() - 데이터를 프로세스가 종료될 때까지 받아서 data에 저장

send(데이터) - 입력한 데이터를 보낸다.
sendline(데이터) - 입력한 데이터의 마지막에 "\n" 를 붙여서 보낸다.
sendafter(문자, 데이터) - 입력한 문자까지 받은 이후, 데이터를 보낸다.
sendlineafter(문자, 데이터) - 입력한 문자까지 받은 이후, 데이터를 "\n"를 마지막에 붙여서 함께 보낸다.
​

### 패킹, 언패킹


p64(숫자값) - 해당 값을 64비트(8바이트), 리틀엔디안 형식으로 패킹
p32(숫자값) - 해당 값을 32비트(4바이트), 리틀엔디안 형식으로 패킹

u64(문자열) - 해당 문자열을 64비트(8바이트), 리틀엔디안 형식으로 언패킹
u32(문자열) - 해당 문자열을 32비트(4바이트), 리틀엔디안 형식으로 언패킹

```python
print(hex(u32(b"ABCD")))
# 0x44434241

print(p32(0x41424344))
# b'DCBA'
```

### ELF 관련 함수
ELF 헤더에는 Exploit에 사용될 수 있는 각종 정보가 기록 되어 있음

`e = ELF("파일 이름")` - ELF 파일 선택
`libc = ELF("파일 이름")` - libc 파일도 ELF 파일이니 선택 가능

`e.plt["함수명"]` - 입력한 함수의 plt 주소를 가져옴
`e.got["함수명"]` - 입력한 함수의 got 주소를 가져옴
`e.symbols["함수명"]` - 입력한 함수의 함수 베이스 주소와의 offset을 가져옴
`list(libc.search("/bin/sh"))[0]` - 선택한 파일에 /bin/sh 문자열이 어느 주소에 있는지 알려옴. 주로 libc에 많이 쓰임.
`next(e.search(b'/bin/sh'))`로도 사용

- 섹션 정보 확인
바이너리의 섹션 정보를 확인
`for section in e.sections:     print(f"{section.name}: {section.header}")`

- 심볼 테이블 확인
함수나 변수와 같은 심볼들의 정보를 확인
`for symbol in e.symbols:     print(f"{symbol}: {hex(e.symbols[symbol])}")`

- GOT 및 PLT 정보 확인
GOT(Global Offset Table)와 PLT(Procedure Linkage Table) 정보를 확인
`print("GOT:", e.got) print("PLT:", e.plt)`

- 함수 확인
바이너리에 정의된 함수들의 목록을 확인
`print("Functions:", e.functions)`

- 엔트리 포인트 및 기타 정보 확인
엔트리 포인트와 기타 주요 정보들을 확인
`print("Entry point:", hex(e.entry)) print("Checksec:", e.checksec())`

​

# 쉘과 상호작용
- r.interactive()
셸을 획득했거나, 익스플로잇의 특정 상황에 직접 입력을 주면서 출력을 확인하고 싶을 때 사용하는 함수

- r.close()
서버와의 연결을 끊음



# 익스플로잇 디버깅
```python
from pwn import *
context.log_level = 'error' # 에러만 출력
context.log_level = 'debug' # 대상 프로세스와 익스플로잇간에 오가는 모든 데이터를 화면에 출력
context.log_level = 'info' # 비교적 중요한 정보들만 출력
```


# 대상 아키텍쳐 설정
- context.arch
pwntools는 셸코드를 생성하거나, 코드를 어셈블, 디스어셈블하는 기능 등을 가지고 있는데, 이들은 공격 대상의 아키텍처에 영향을 받음
그래서 pwntools는 아키텍처 정보를 프로그래머가 지정할 수 있게 하며, 
이 값에 따라 몇몇 함수들의 동작이 달라짐

```python
from pwn import *
context.arch = "amd64" # x86-64 아키텍처
context.arch = "i386" # x86 아키텍처
context.arch = "arm" # arm 아키텍처
```


# shellcraft
자주 사용되는 쉘코드를 이용할 수 있음
매우 편리한 기능이지만 정적으로 생성된 셸 코드는 셸 코드가 실행될 때의 메모리 상태를 반영하지 못함
또한 프로그램에 따라 입력할 수 있는 셸 코드의 길이나, 구성 가능한 문자의 종류에 제한이 있을 수 있는데, 이런 조건들도 반영하기 어려움

```python
#!/usr/bin/env python3
# Name: shellcraft.py 

from pwn import *
context.arch = 'amd64' # 대상 아키텍처 x86-64 
code = shellcraft.sh() # 셸을 실행하는 셸 코드 
print(code)
```

```sh
$ python3 shellcraft.py 
/* execve(path='/bin///sh', argv=['sh'], envp=0) */ 
/* push b'/bin///sh\x00' */ 
push 0x68 
mov rax, 0x732f2f2f6e69622f 
... 
yscall
```


# 어셈블하기
아키텍처를 미리 설정해야 함 

```python
#!/usr/bin/env python3
# Name: shellcraft.py 

from pwn import *
context.arch = 'amd64' # 대상 아키텍처 x86-64 
code = shellcraft.sh() # 셸을 실행하는 셸 코드 
code = asm(code)
print(code)
```

```sh
$ python3 asm.pyb'jhH\xb8/bin///sPH\x89\xe7hri\x01\x01\x814$\x01\x01\x01\x011\xf6Vj\x08^H\x01\xe6VH\x89\xe61\xd2j;X\x0f\x05'
```


# 바이트 순서 뒤집기
1. `cnry=p64(u64(cnry), endian='big')`
2. `cnry[::-1]`


# 각종 변환
`p32`, `u32` 함수들이 유용하지만, 때로는 정확히 4, 8바이트 단위로 나눠진 바이트가 아니라 
직접 바이트를 만들어야 할 때가 있음
- 정수 -> 바이트
`str([정수값]).encode()`

- 바이트 -> 정수
`int([바이트값].decode())`

- `%p`로 출력된 주소 다시 패킹
예를 들어 `0x7fffffff`이런 주소값이 나왔다면
```python
encoded_data=0x7fffffff
encoded_data=encoded_data[2:]
p32(int(encoded_data, 16))
```

- 텍스트 바이트로 변환
```python
data_str = "54586b6458754f7b215c7c75424f21634f744275517d6d" 
data_bytes = bytes.fromhex(data_str)
```