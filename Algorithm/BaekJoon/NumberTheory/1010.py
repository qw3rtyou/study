import sys
input=sys.stdin.readline

cache={}

def factorial(n):
    if n in cache:
        return cache[n]
    
    elif n<2:
        return 1
    
    else:
        return n*factorial(n-1)

size=int(input().strip())
ans=[]

for _ in range(size):
    
    n,m=map(int,input().split())
    ans.append(int(factorial(m)//factorial(n)//factorial(m-n)))
    
for a in ans:
    print(a)