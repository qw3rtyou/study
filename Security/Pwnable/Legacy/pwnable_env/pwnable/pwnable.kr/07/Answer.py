from pwn import *

p1=ssh("input2","pwnable.kr",port=2222,password="guest")

print(p1)

arg=["A" for i in range(100)]
arg[ord("A")]='\x00'
arg[ord("B")]='\x20\x0a\x0d'

p=p1.process(executable ="/home/input2/input",argv=arg,env={})
#p = process([“/home/theory/binary”,”AAAA”], env={“LD_PRELOAD”:”./libc.so.6”})

print(p.recv())		#1 clear

buf=""

p.sendline(buf)	