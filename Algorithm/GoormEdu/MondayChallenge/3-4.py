import sys
from collections import defaultdict

sys.setrecursionlimit(10**8)
input=sys.stdin.readline

graph=defaultdict(list)

n=int(input())

for _ in range(n):
    s,e=map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
    
visited=[-1]*(n+1)
found=-1
cycle=list()

def findCycle(u,tar):
    global found
    
    if visited[u]==1:
        found=u
        if u not in cycle:
            cycle.append(u)
        return
    
    visited[u]=1
    for i in graph[u]:
        if tar==i:
            continue
        
        findCycle(i,u)
            
        if found==-2:
            return
        
        if found==u:
            found=-2
            return
        
        if found>=0:
            if u not in cycle:
                cycle.append(u)
            return

findCycle(1,1)

cycle.sort()

print(len(cycle))

print(*cycle)
        