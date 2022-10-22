ans=[]

while True:
    a,b,c=map(int,input().split())
    
    if a==0 and b==0 and c==0:
        break
        
    if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==b**2+a**2:
        ans.append("right")
    else:
        ans.append("wrong")
        
for a in ans:
    print(a)