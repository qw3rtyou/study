def check_intersection(x1,y1,r1,x2,y2,r2):
    if x1==x2 and y1==y2 and r1==r2:
        return -1
    
    elif (x1==x2 and y1==y2) or (r1+r2)**2<(x2-x1)**2+(y2-y1)**2 or (r1-r2)**2>(x2-x1)**2+(y2-y1)**2:
        return 0
    
    elif (r1+r2)**2==(x2-x1)**2+(y2-y1)**2 or (r1-r2)**2==(x2-x1)**2+(y2-y1)**2:
        return 1
    else:
        return 2
    
test_case=int(input())
ans=[]

for _ in range(test_case):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    ans.append(check_intersection(x1,y1,r1,x2,y2,r2))
for a in ans:
    print(a)