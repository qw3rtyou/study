from collections import Counter
import sys

input=sys.stdin.readline

n,m=map(int,input().split())
data=[(input().rstrip()) for _ in range(n+m)]
counter=Counter(data)

answer=list()
for key in counter:
    if counter[key]==2:
        answer.append(key)

answer.sort()

print(len(answer))
for a in answer:
    print(a)




#시간초과
# import sys
# input=sys.stdin.readline

# n,m=map(int,input().split())

# never_heard=list()
# never_seen=list()

# for _ in range(n):
#     never_heard.append(input().rstrip())
    
# for _ in range(m):
#     never_seen.append(input().rstrip())
    
# ans=list()

# for i in never_heard:
#     if i in never_seen:
#         ans.append(i)
        
# ans.sort()

# print(len(ans))
# for asdf in ans:
#     print(asdf)