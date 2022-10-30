def GCD(a,b):
    while a%b!=0:
        a=a%b
        a,b=b,a 
    return b
            
def LCM(a,b):
    return a*b//GCD(a,b)

a,b=map(int,input().split())

print(GCD(a,b))
print(LCM(a,b))
