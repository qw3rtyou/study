def prime(n):
    check=[False,False]+[True]*(n-1)
    
    m=int(n ** .5)
    
    for i in range(2,m+1):
        if check[i]:
            for j in range(i+i,n+1,i):
                check[j]=False
                
    return [i for i in range(2,n+1) if check[i]]


n=int(input())
l=prime(n)

nums=list(map(int,input().split()))

ans=0

for i in l:
	ans+=nums[i-1]    
    
print(ans)