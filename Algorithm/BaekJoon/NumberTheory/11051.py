# def factorial(n):
#     if n<2:
#         return 1
    
#     else:
#         return n*factorial(n-1)

def factorial(n):
    tmp=1
    for i in range(1,n+1):
        tmp*=i
    
    return tmp
    
n,k=map(int,input().split())
ans=int(factorial(n)//factorial(k)//factorial(n-k))%10007

print(ans)