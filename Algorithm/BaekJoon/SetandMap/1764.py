import sys
input=sys.stdin.readline

n,m=map(int,input().split())

never_heard=list()
never_seen=list()

for _ in range(n):
    never_heard.append(input().rstrip())
    
for _ in range(m):
    never_seen.append(input().rstrip())
    
ans=list()

for i in never_heard:
    if i in never_seen:
        ans.append(i)
        
ans.sort()

print(len(ans))
for asdf in ans:
    print(asdf)