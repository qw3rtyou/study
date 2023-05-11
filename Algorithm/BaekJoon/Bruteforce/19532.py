import sys
input=sys.stdin.readline

a,b,c,d,e,f=map(int,input().split());
hoxy=[]

for i in range(-1000,1000):
    for j in range(-1000,1000):
        if a*i+b*j==c:
            hoxy.append((i,j))

#print(hoxy)

for i,j in hoxy:
    if d*i+e*j==f:
        print(i,j)