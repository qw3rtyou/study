size=int(input())
factor=list(map(int,input().split()))
            
ans=int(min(factor))*int(max(factor))

print(ans)