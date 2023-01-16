import sys
from collections import defaultdict,deque
sys.setrecursionlimit(10**5)

input=sys.stdin.readline

islands,bridges,me=map(int,input().split())

graph=defaultdict(list)

for i in range(bridges):
    s,e=map(int,input().split())
    graph[s].append(e)

def bfs(cur):
    global movement
    
    for next in graph[cur]:       #searching..  
        if next==me:
            print(movement+1)
            sys.exit()
        
        movement+=1
        bfs(next)
        movement-=1

stack=deque()
stack.append(me)
movement=0
bfs(stack.pop())

print(-1)