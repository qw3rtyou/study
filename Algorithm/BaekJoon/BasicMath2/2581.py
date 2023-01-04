#-*- coding: utf-8 -*-
#소수

def prime_Checker(n):
    if n == 1:
        return False
    
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

m=int(input())
n=int(input())
res=0
min_res=0

for i in range(m,n+1):
    if prime_Checker(i):
        if min_res == 0:
            min_res=i
        res+=i
        
if res == 0:
    print(-1)
    
else:
    print(res)
    print(min_res)