import sys
input=sys.stdin.readline

n,m=map(int,input().split())
n_list=list()

for _ in range(n):
    n_list.append(input())
    
m_list=list()

for _ in range(m):
    m_list.append(input())
    
cnt=0

for i in m_list:
    if i in n_list:
        cnt+=1

print(cnt)