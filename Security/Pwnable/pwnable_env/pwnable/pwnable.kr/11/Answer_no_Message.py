#어떻게 해도 느려서 pwnable.kr 서버 tmp 하위에 디렉토리에 파이썬 파일 만들고 localhost로 수정후
#코드돌리니까 매우 양호
#b1NaRy_S34rch1nG_1s_3asy_p3asy

from pwn import *

p=remote("pwnable.kr",9007)

p.recv()

for found_coin in range(100):
    p.recvuntil("N=")
    N=int(p.recvuntil(" "))

    p.recvuntil("C=")
    C=int(p.recvline())
    
    start=0
    end=N-1
    mid=(start+end)//2
    
    for chance in range(C):
        
        if start==mid:
            
            p.sendline(str(start))
            result=p.recvline()     
            
            result=int(result)
            
            if result%10==0:
                start=end
                mid=end
            
        else:
            buffer=" ".join([str(i) for i in range(start, mid)])       

            p.sendline(buffer)        
            result=int(p.recvline())

            if result%10==0:
                start=mid
            else:
                end=mid            
            mid=(start+end)//2
    p.sendline(str(start))
    print(p.recvline())
    
    
print(p.recv()) #print flag