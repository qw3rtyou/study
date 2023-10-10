# 주의할 점
python3 커맨드를 사용하거나
python3.6 혹은 2.7을 사용해야지만 pwn모듈 import가능


# 사용법

pwntools 모듈을 사용하려면 무조건 포함해줘야 하는 코드

	from pwn import *

​
디버깅할 때 좋다. 무슨 입력을 했고, 어떤 출력을 받았는지 잘 보여줌.

	context.log_level = 'debug'

### remote

	remote("주소", 포트)
	
nc 서버에 접속할 때 주로 쓰인다. 

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
	
옵션으로 gdb.attach(r, "실행될 명령어")를 쓰기도 한다. break 거는데 유용.

### 패킹 언패킹
p64(숫자값) - 해당 값을 64비트(8바이트), 리틀엔디안 형식으로 패킹해준다.
p32(숫자값) - 해당 값을 32비트(4바이트), 리틀엔디안 형식으로 패킹해준다.
u64(문자열) - 해당 문자열을 64비트(8바이트), 리틀엔디안 형식으로 언패킹해준다.
u32(문자열) - 해당 문자열을 32비트(4바이트), 리틀엔디안 형식으로 언패킹해준다.

### 데이터 주고받기
recv(개수) - 입력한 개수 만큼 출력을 받는다.
recvuntil(문자) - 입력한 문자까지만 입력을 받는다.
recvline() - 한 줄을 받는다.(\n을 받으면)
send(데이터) - 입력한 데이터를 보낸다.
sendline(데이터) - 입력한 데이터의 마지막에 "\n" 를 붙여서 보낸다.
sendafter(문자, 데이터) - 입력한 문자까지 받은 이후, 데이터를 보낸다.
sendlineafter(문자, 데이터) - 입력한 문자까지 받은 이후, 데이터를 "\n"를 마지막에 붙여서 함께 보낸다.
​

### ELF 관련 함수

e = ELF("파일 이름") - ELF 파일 선택
libc = ELF("파일 이름") - libc 파일도 ELF 파일이니 선택 가능.

e.plt["함수명"] - 입력한 함수의 plt 주소를 가져옴
e.got["함수명"] - 입력한 함수의 got 주소를 가져옴
e.symbols["함수명"] - 입력한 함수의 함수 베이스 주소와의 offset을 가져옴
list(libc.search("/bin/sh"))]0] - 선택한 파일에 /bin/sh 문자열이 어느 주소에 있는지 알려옴. 주로 libc에 많이 쓰임.
​

### 스트림 관련 함수들

r = remote("") / r = process("")

r.interactive() - 서버에 내가 직접 상호작용하게 해줌
r.close() - 서버와의 연결을 끊음