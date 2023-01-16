def common_Factor(a,b):
    tmp=set()
    for i in range(1,a+1 if a>b else b+1):
        if a%i==0 and b%i==0:
            tmp.add(i)
            
    return max(tmp)

size=int(input())
nums=list(map(int,input().split()))

for i in range(1,size):
    factor=common_Factor(nums[0],nums[i])
    print(str(nums[0]//factor)+"/"+str(nums[i]//factor))