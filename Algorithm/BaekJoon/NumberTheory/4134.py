import sys
input=sys.stdin.readline

def GCD(a,b):
    while(b!=0):
        a,b=b,a%b
    return a

def prime_over_than(k):
    

n=int(input())

for _ in range(n):
    target=int(input())

    print(prime_over_than(target))