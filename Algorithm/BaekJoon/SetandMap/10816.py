from collections import Counter

_=int(input())

counter=Counter(map(int,input().split()))

_=int(input())

for key in map(int,input().split()):
    print(counter[key],end=" ")


#나쁘진 않은데 좀 김
# import sys
# from collections import defaultdict

# input=sys.stdin.readline

# n=int(input())
# nums=defaultdict(int)

# for value in map(int,input().split()):
#     nums[value]+=1

# m=int(input())

# for key in map(int,input().split()):
#     print(nums[key],end=" ")