import sys
from collections import defaultdict

sys.setrecursionlimit(2^10)
input=sys.stdin.readline
cache=defaultdict(int)
cache[1]=1
cache[2]=2
cache[3]=3
cache[4]=5

def tile_recur(n):
    if cache[n]: return cache[n]
    
    if cache[n-2]:
        tmp1=cache[n-2]
    else:
        tmp1=tile_recur(n-2)
        
    if cache[n-3]:
        tmp2=cache[n-3]
    else:
        tmp2=tile_recur(n-3)
        
    cache[n]=2*tmp1+tmp2
    
    return cache[n]

k=int(input())
print(tile_recur(k)%15746)    