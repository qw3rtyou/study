import sys
input=sys.stdin.readline

cache={}

def factorial(n):
    tmp=1
    for i in range(1,n+1):
        tmp*=i
    
    return tmp

# def factorial(n):
#     if n in cache:
#         return cache[n]
    
#     elif n<2:
#         return 1
    
#     else:
#         return n*factorial(n-1)
    
n,m=map(int,input().split())

data=str(factorial(n)//factorial(m)//factorial(n-m))
count=0
print(data)

for i in range(len(data)-1,0,-1):
    if data[i]=='0':
        count+=1
    else:
        break
        
print(count)