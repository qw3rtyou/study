import sys

input=sys.stdin.readline

n=int(input())
tmp=666
cnt=0
ans=None

while True:
    if "666" in str(tmp):
        cnt+=1
        
    if cnt==n:
        ans=tmp
        break
        
    tmp+=1
    
print(ans)