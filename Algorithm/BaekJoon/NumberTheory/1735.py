import sys
input=sys.stdin.readline

def GCD(a,b):
    while(b!=0):
        a%=b
        a,b=b,a

    return a

a,b=map(int,input().split())
c,d=map(int,input().split())

numerator=a*d+b*c
denominator=b*d

gcd=GCD(numerator,denominator)

print(int(numerator/gcd),int(denominator/gcd))