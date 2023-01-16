from collections import deque
from math import inf

n=int(input())
stairs=[int(input()) for _ in range(n)]
max_val=-inf
stack=deque()
stack.append(stairs[0])

def dfs(con_check,height):
    global max_val
    if height==n:
        max_val=max(max_val,sum(stack))
        return
    
    if con_check==0:
        for i in [0,1]:
            stack.append(height+i+1)
            dfs(i,height+i+1)
            stack.pop()
            
    elif con_check==1:
        stack.append(height+1)
        dfs(0,height+1)
        stack.pop()
        
dfs(0,1)
print(max_val)