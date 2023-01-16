from collections import defaultdict

available=list()
tmp=defaultdict(int)

n=int(input())
data=list(map(int,input().split()))

for num in data:
    tmp[num]+=1

for key in tmp:
    value=tmp[key]
    for _ in range(value//2):
        available.append(key)
    
available=sorted(available,reverse=True)
ans=0
        
for i in range(0,len(available) if len(available)%2==0 else len(available)-1 ,2):
    ans+=available[i]*available[i+1]
    
print(ans)