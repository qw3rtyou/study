import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int,input().split())
stack=deque()

def dfs():
    if len(stack)==m:
        print(*stack)
        return
    
    for i in range(1,n+1):
        if stack:
            if i < stack[-1]:
                continue
        
        stack.append(i)
        dfs()
        stack.pop()

dfs()
