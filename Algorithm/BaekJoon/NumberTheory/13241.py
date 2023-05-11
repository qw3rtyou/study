import sys
input=sys.stdin.readline

a,b=map(int,input().split())

ans=a*b
while(b!=0):
    a%=b
    a,b=b,a

ans/=a

print(int(ans))