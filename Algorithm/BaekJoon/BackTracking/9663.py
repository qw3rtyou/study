from collections import deque
import sys

input=sys.stdin.readline

n=int(input())

stack=deque()
cnt=0

def dfs_queen():
    global cnt
    
    if not is_observe_rules():
        return
    
    if len(stack)==n:
        cnt+=1
        return
    
    for element in range(n):
        stack.append(element)
        dfs_queen()
        stack.pop()
        
def is_observe_rules():
    if not stack:
        return True
    
    cur_stack_len=len(stack)
    buffer1=list(map(lambda x:stack[x]-x,range(cur_stack_len)))
    buffer2=list(map(lambda x:stack[x]+x,range(cur_stack_len)))
    buffer1=list(set(buffer1))
    buffer2=list(set(buffer2))
    
    if len(buffer1)!=cur_stack_len or len(buffer2)!=cur_stack_len:
        return False
    
    buffer1=list(set(stack))
    
    if len(buffer1)!=cur_stack_len:
        return False
    
    return True

dfs_queen()
print(cnt)