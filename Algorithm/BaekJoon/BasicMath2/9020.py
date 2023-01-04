#-*- coding: utf-8 -*-
#골드바흐의 추측

def prime_spawner(n):
    check=[False]*2+[True]*(n-1)
    m=int(n**.5)+1
    
    for i in range(2,m+1):
        if check[i]:
            for j in range(i+i,n+1,i):
                check[j]=False
                
    return [i for i in range(2,n+1) if check[i]]


ans=[]

t=int(input())

for _ in range(t):
    n=int(input())
    primes=prime_spawner(n)
    
    a=n//2
    while True:
        b=n-a
        if a in primes and b in primes:
            ans.append((a,b))
            break
        else:
            a-=1
            
for a,b in ans:
    print(a,b)

    
