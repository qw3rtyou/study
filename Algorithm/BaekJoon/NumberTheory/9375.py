testcase=int(input())
ans=[]

for _ in range(testcase):
    n=int(input())
    clothes={}
    
    for _ in range(n):
        _,cloth_type=map(str,input().split())
        if bool(clothes.get(cloth_type)):
            clothes[cloth_type]+=1
        else:
            clothes[cloth_type]=1
            
    tmp=1
    for c in clothes.values():
        tmp*=(c+1)
    tmp-=1
    
    ans.append(tmp)
    
for t in ans:
    print(t)