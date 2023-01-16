import sys
input=sys.stdin.readline

nums=[int(input()) for _ in range(5)]

avg1=sum(nums)//5
avg2=sorted(nums)[2]

print(avg1)
print(avg2)