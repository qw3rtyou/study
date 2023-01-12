from collections import defaultdict

cache=defaultdict(int)

def w(a,b,c):
    if cache[(a,b,c)]:
        return cache[(a,b,c)]
    
    if a<=0 or b<=0 or c<=0:
        return 1
    
    if a>20 or b>20 or c>20:
        return w(20,20,20)
    
    if a<b<c:
        cache[(a,b,c)]=w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
        return cache[(a,b,c)]
    
    else:
        cache[(a,b,c)]=w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
        return cache[(a,b,c)]

prob=list()
    
while True:
    a,b,c=map(int,input().split())
    
    if a==-1 and b==-1 and c==-1:
        break
    else:
        print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))
    
    
