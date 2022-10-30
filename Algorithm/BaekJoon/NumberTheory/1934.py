import sys
input=sys.stdin.readline

def GCM(a,b):
    while a%b!=0:
        a=a%b
        a,b=b,a 
    return b


def LCM(a,b):
    return (a*b)//GCM(a,b)

            
size=int(input())

ans=[]

for _ in range(size):
    a,b=map(int,input().split())
    ans.append(LCM(a,b))
    
for a in ans:
    print(a)