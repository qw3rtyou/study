from collections import defaultdict,deque
from math import inf
import sys

sys.setrecursionlimit(10**8)

n=int(input())
stack=deque()
board=[int(input()) for i in range(n)]

max_juice=-inf

def search(idx):
    global max_juice
    
    if idx==n:
        cur_juice=0
        for i in list(filter(lambda i:stack[i]==1,range(n))):
            cur_juice+=board[i]
        
        max_juice=max(max_juice,cur_juice)
        
        return
    
    if idx<2:
        for i in 1,2:
            stack.append(i)
            search(idx+1)
            stack.pop()
            
    else:
        if stack[-1]==1 and stack[-2]==1:
            stack.append(0)
            search(idx+1)
            stack.pop()
            
        else:
            for i in 1,2:
                stack.append(i)
                search(idx+1)
                stack.pop()
                
search(0)

print(max_juice)