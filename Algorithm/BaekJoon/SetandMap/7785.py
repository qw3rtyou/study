import sys
input=sys.stdin.readline

n=int(input())

inside=set()

for _ in range(n):
    name,action=input().split()
    name = name.rstrip()
    
    if action=='enter':
        inside.add(name)
    elif action=='leave':
        inside.discard(name)

inside=sorted(list(inside),reverse=True)
#[print(name) for name in inside]
for name in inside:
    print(name)