import sys
from collections import defaultdict

#sys.setrecursionlimit(10^10000)
input=sys.stdin.readline

friends=int(input())
relations=int(input())

graph=defaultdict(list)

for i in range(relations):
    s,e=map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

def dfs(cur):   
    for next in graph[cur]:
        if next in heard:
            continue
        
        heard.append(next)
        dfs(next)
    
heard=list()
heard.append(1)
dfs(1)

print(len(heard))