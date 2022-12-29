from collections import deque
from math import inf

n=int(input())

board=[list(map(int,input().split())) for _ in range(n)]
stack=deque()
min_val=-inf

def dfs():
    global min_val
    
    if len(stack)==n:
        min_val=min(min_val,sum(board[i][stack[i]] for i in range(n)))
        return
    
    for i in 0,1,2:
        if not stack:
            None
            
        elif i==stack[-1]:
            continue
        stack.append(i)
        dfs()
        stack.pop()
        
dfs()
print(min_val)