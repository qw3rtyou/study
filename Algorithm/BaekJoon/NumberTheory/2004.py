import sys
from collections import defaultdict

input=sys.stdin.readline

cache=defaultdict(int)

def combination(n,m):
    if m==1:
        return n
    elif (n-m)==1:
        return n
    elif m==0:
        return 1
    elif n-m==0:
        return 1
    elif cache[(n,m)]:
        return cache[(n,m)]
    else:
        return combination(n-1,m)+combination((n-1),m-1)
	
n,m=map(int,input().split())

print(combination(n,m))

# def factorial(n):
    
    
# n,m=map(int,input().split())

# a=factorial(n)
# b=factorial(m)
# c=factorial(n-m)

# #print(a,b,c)

# data=(a[0]-b[0]-c[0],a[1]-b[1]-c[1])

# ans=min(data)
        
# print(ans)