n,s=input().split()
ans=0

for _ in range(int(n)):
    name=input()
    if s in name:
        ans+=1

print(ans)