













# from collections import deque
# import sys

# input=sys.stdin.readline

# n=int(input())

# stack=deque()
# cnt=0

# def dfs_queen():
#     global cnt
    
#     if not is_observe_rules():
#         return
    
#     if len(stack)==n:
#         cnt+=1
#         return
    
#     for element in range(n):
#         if element in stack:
#             continue
            
#         stack.append(element)
#         dfs_queen()
#         stack.pop()
        
# def is_observe_rules():
#     if not stack:
#         return True
    
#     x=len(stack)-1
#     y=stack[-1]
    
#     for i in range(len(stack)):
#         if x==i:
#             continue
    
#         if (y-stack[i])/(x-i)==-1 or (y-stack[i])/(x-i)==1:
#             return False

#         if stack[i]==stack[x]:
#             return False
    
#     return True

# dfs_queen()
# print(cnt)