import sys
input=sys.stdin.readline

def factorial(n):
    tmp=[0,0]
    for i in range(30):
        for j in range(13):
            for k in range(1,n):
                if 2**i*5**j*k<=n and k%5!=0 and k%2!=0:
                    #print(i,j,k,2**i*5**j*k)
                    tmp[0]+=i
                    tmp[1]+=j
                
    return tmp
    
n,m=map(int,input().split())

a=factorial(n)
b=factorial(m)
c=factorial(n-m)

#print(a,b,c)

data=(a[0]-b[0]-c[0],a[1]-b[1]-c[1])

ans=min(data)
        
print(ans)