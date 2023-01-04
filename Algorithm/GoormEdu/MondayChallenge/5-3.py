def select(lump):
    if not False in checker:
        ans.append(lump)
        return 
    
    pre=lump
    for i in range(size):
        lump=pre
        if checker[i]:
            continue
        else:
            checker[i]=True
            lump=pre
            lump=concat(lump,nums[i])
            select(lump)
            lump=pre
            lump=concat(nums[i],lump)
            select(lump)
            checker[i]=False

def concat(a,b):
    if a[-1]==b[0]:
        return a+b[1:]
    else:
        return a+b
        
size=int(input())

nums=list(map(str,input().split()))
checker=[False]*size
ans=[]

for i in range(size):
    lump=nums[i]
    checker[i]=True
    select(lump)
    checker[i]=False

print(min(map(int,ans)))