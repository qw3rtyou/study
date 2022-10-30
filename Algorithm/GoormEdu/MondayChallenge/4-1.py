from collections import deque

n,m=map(int,input().split())

rsv=deque()

for i in range(m):
    typ,mny=map(str,input().split())
    mny=int(mny)
    
    if typ[0]=='d':
        n+=mny
        while rsv:
            tmp=rsv.popleft()
            if tmp<=n:
                n-=tmp
            else:
                rsv.appendleft(tmp)
                break
        
    elif typ[0]=='p' and mny<=n:
        n-=mny
        
    elif typ[0]=='r':
        if mny<=n:
            n-=mny
        else:
            rsv.append(mny)
            
print(n)