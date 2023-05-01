# length,target=map(int, input().split())
# attendance=[]

# for _ in range(length):
#     s,t=map(str,input().split())
#     attendance.append((s,float(t)))
    
# attendance=sorted(attendance,key=lambda x: (x[0], -x[1]))

# #print(attendance)

# name,height=attendance[target-1]

# print(str(name)+' %.2f' % height)


import sys
from functools import cmp_to_key
N, k = map(int, sys.stdin.readline().split())

def cmp(a, b):
    if a[0] == b[0]:
        return a[1] < b[1]
    else:
        return a[0] < b[0]
arr = [] # [[string1, int1], [string2, int2], ...]

for _ in range(N):
	tmp = list(sys.stdin.readline().split())
	arr.append(tmp)
	
arr = sorted(arr,key=cmp_to_key(cmp))
arr = sorted(arr,key = lambda x: (x[0],x[1]))
print(arr[k-1][0]+' '+arr[k-1][1])