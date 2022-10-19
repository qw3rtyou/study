from functools import cmp_to_key

def cmp(a,b):
    if a[0]==b[0]:
        return a[1]<b[1]
    else:
        return a[0]<b[0]

length,target=map(int, input().split())
attendance=[]

for _ in range(length):
    s,t=map(str,input().split())
    attendance.append((s,float(t)))
    
#attendance=sorted(attendance,key=lambda x: (x[0], -x[1]))
attendance=sorted(attendance,key=cmp_to_key(cmp))

print(attendance)

name,height=attendance[target-1]

print(name,"%.2lf"%height)