import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

n,m,k=map(int,input().split())
case=defaultdict()

def biz_recursion(n,m,k):
    if (n,m,k) in case:
        return case[(n,m,k)]
    
    if n==0 or n==n+m:
        case[(n,m,k)]=1
        return 1
    
    if k==0:
        case[(n,m,k)]=0
        return 0
    
    a=biz_recursion(n-1,m+1,k-1)
    b=biz_recursion(n+1,m-1,k-1)
    c=biz_recursion(n,m,k-1)
    tmp=a+b+c
    tmp%=100000007
    case[(n,m,k)]=tmp
    return tmp

ans=biz_recursion(n,m,k)

print(ans)