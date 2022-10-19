#-*- coding: utf-8 -*-
#소수 구하기

def prime_spawner(n):
    check=[False]*2+[True]*(n-1)
    m=int(n**.5)+1
    
    for i in range(2,m+1):
        if check[i]:
            for j in range(i+i,n+1,i):
                check[j]=False
                
    return [i for i in range(2,n+1) if check[i]]

m,n=map(int, input().split())

prime=prime_spawner(n)

for num in prime:
    if num>=m:
        print(num)