#-*- coding: utf-8 -*-
#베르트랑 공준

def prime_spawner(n):
    check=[False]*2+[True]*(n-1)
    m=int(n**.5)+1
    
    for i in range(2,m+1):
        if check[i]:
            for j in range(i+i,n+1,i):
                check[j]=False
                
    return [i for i in range(2,n+1) if check[i]]


ans=[]

while True:
    n=int(input())
    
    if n==0:
        break
    
    count=0
    primes=prime_spawner(2*n)
    
    for prime in primes:
        if prime>n:
            count+=1
    
    ans.append(count)
            
for count in ans:
    print(count)
    
