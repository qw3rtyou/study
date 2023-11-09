from pwn import *

p=remote("pwnable.kr",9007)

p.recv()

for found_coin in range(100):
    p.recvuntil("N=")
    N=int(p.recvuntil(" "))

    p.recvuntil("C=")
    C=int(p.recvline())
    print(N,C)	#number of coin, number of chance

    start=0
    end=N-1
    mid=(start+end)//2
    
    for chance in range(C):
        print(start,mid,end)
        
        print("\n chance"+str(chance))
        
        if start==mid:
            print("input: "+str(start))
            
            p.sendline(str(start))
            result=p.recvline()     
            
            print("result: "+result)
            
            result=int(result)
            
            if result%10==0:
                start=end
                mid=end
            
    	else:
            buffer=""

            for i in range(start, mid):
                buffer+=str(i)
                buffer+=" "
            buffer=buffer.strip()        

            print("input: "+str(buffer))

            p.sendline(buffer)        
            result=int(p.recvline())

            print("result: "+str(result))

            if result%10==0:
                start=mid
            else:
                end=mid            
            mid=(start+end)//2
            
    print("round"+str(found_coin+1)+" done")
    p.sendline(str(start))
    print(p.recvline())
    
    
print(p.recv()) #print flag