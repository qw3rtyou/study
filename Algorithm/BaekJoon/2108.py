n=int(input())
nums=[]

avg=0
mid=0
frq=0
rng=0

for _ in range(n):
    nums.append(int(input()))
    
nums.sort()

avg=round(sum(nums)/n)
mid=nums[int((n+1)/2)-1]

nums_set=list(set(nums))
counter=0

nus_dict=[]

for element in nums_set:
    for num in nums:
        if num==element:
            counter+=1
        nums_dict.appen