from pwn import *

# stage 1
argvs = [str(i) for i in range(100)]
argvs[ord('A')] = '\x00'
argvs[ord('B')] = '\x20\x0a\x0d'

# stage 2
with open('./stderr', 'a') as f:
    f.write('\x00\x0a\x02\xff')

# stage 3
envVal = {'\xde\xad\xbe\xef':'\xca\xfe\xba\xbe'}

# stage 4
with open('./\x0a', 'a') as f:
    f.write('\x00\x00\x00\x00')

# stage 5
argvs[ord('C')] = '40000'

target = process(executable = '/home/input2/input', argv=argvs, stderr=open('./stderr'), env=envVal)

target.sendline('\x00\x0a\x00\xff')

conn = remote('localhost','40000')
conn.send('\xde\xad\xbe\xef')
target.interactive()

