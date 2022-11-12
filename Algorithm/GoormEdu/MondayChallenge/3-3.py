import sys
from collections import defaultdict, deque
input=sys.stdin.readline

n,m,k=int(input())
graph=defaultdict(list)

for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
q=deque()
visited=[-1]*(n+1)

q.append(1)
visited[1]=0

while q:
    cur=q.popleft()
    for nxt in graph[cur]:
        if visited[nxt]!=-1:
            continue
        
        