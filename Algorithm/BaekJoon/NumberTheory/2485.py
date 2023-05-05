import sys
input=sys.stdin.readline
from functools import reduce

def GCD(a,b):
    while(b!=0):
        a,b=b,a%b
    return a

n=int(input())

trees=[int(input()) for _ in range(n)]

dist=[trees[i+1]-trees[i] for i in range(n-1)]

gcd=reduce(GCD,dist)
# gcd=dist[0]
# for i in dist[1:]:
#     gcd=GCD(gcd,i)

print(sum(dist)//gcd-n+1)