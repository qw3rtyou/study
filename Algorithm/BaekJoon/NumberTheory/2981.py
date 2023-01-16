from functools import reduce
import sys
input=sys.stdin.readline

def GCD(a,b):
    while a%b!=0:
        a=a%b
        a,b=b,a 
    return b

def LCM(a,b):
    return a*b//GCD(a,b)

def multiple(a):
    multi=set()
    for i in range(1,int(a**.5)+1):
        if a%i==0:
            multi.add(i)
            multi.add(a//i)
            
    multi=list(multi)
    multi.sort()
    return multi


size=int(input())
n=[int(input()) for _ in range(size)]
tmp=[]
gcd=0
ans=set()

n.sort()

for i in range(1,size):
    tmp.append(n[i]-n[0])

gcd=reduce(lambda x,y:GCD(x,y),tmp)

ans=multiple(gcd)
ans.remove(1)

print(*ans)




















#2트
# ans=set()

# for rmn in range(min(n)+1):
#     tmp=list(map(lambda x:x-rmn,n))
#     ans.add(reduce(lambda x,y:GCM(x,y),tmp))

# ans.remove(1)

# print(*ans)













#1트
# ans=set()
# rst=None

# for m in range(2,max(n)):
#     for rmn in range(min(n)+1):
#         rst=set(map(lambda x:(x-rmn)%m,n))
#         if len(rst)==1 and 1 in rst:
#             ans.add(m)