import sys

input=sys.stdin.readline

n=int(input())
n_dict=dict()
for i in map(int,input().split()):
    n_dict[i]=True

m=int(input())
m_list=list(map(int,input().split()))

ans=[0 for _ in range(m)]

for i in range(m):
    if m_list[i] in n_dict:
        ans[i]=1
        
print(*ans)
