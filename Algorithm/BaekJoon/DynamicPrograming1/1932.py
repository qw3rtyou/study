from collections import deque
from math import inf

n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
stack=deque()
stack.append(7)
max_val=-inf

def dfs(depth,pos):
    global max_val
    
    if len(stack)==n:
        max_val=max(max_val,sum(stack))
        return
    
    for i,j in [(depth+1,pos),(depth+1,pos+1)]:
        stack.append(board[i][j])
        dfs(i,j)
        stack.pop()
        
dfs(0,0)
print(max_val)