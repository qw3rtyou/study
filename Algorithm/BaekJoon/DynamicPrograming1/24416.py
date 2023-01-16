








# import sys

# input=sys.stdin.readline

# count=0

# def recur_fib(n):
#     global count
    
#     if n==1 or n==2:
#         count+=1
#         return 1
    
#     else:
#         return recur_fib(n-1)+recur_fib(n-2)
    
# fib=dict()

# fib[1]=1
# fib[2]=1

# def dynamic_fib(n):
#     global count
    
#     for i in range(3,n+1):
#         count+=1
#         fib[i]=fib[i-1]+fib[i-2]
        
#     return fib[n]
    
# k=int(input())

# recur_fib(k)
# print(count,end=" ")

# count=0

# dynamic_fib(k)
# print(count)