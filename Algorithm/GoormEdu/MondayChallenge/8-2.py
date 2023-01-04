n=int(input())

heights=list(map(int,input().split()))
pains=[0]
tallest=0
cnt=0

for i in range(1,n):
    
    if heights[i]>=heights[tallest]:
        tallest=j
        
    if tallest==i:
        pains.append(0)
        continue
        
    if tallest+1==i:
        pains.append(1)
        continue
        
    for j in range(tallest,i):
        if j+1>=i:
            continue
        
        if max(heights[j+1:i])<heights[j]:
            cnt+=1
            
    pains.append(cnt)
    cnt=1
    
print(*pains)