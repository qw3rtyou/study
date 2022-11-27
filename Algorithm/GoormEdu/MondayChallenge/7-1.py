n,m=map(int,input().split())    #n:event_type_num    m:user_num
from collections import defaultdict

event_table=defaultdict(int)

for _ in range(m):
    data=input().split()
    e=data[0]    #e:used_event_time
    for event_num in data[1:]:
        event_table[event_num]+=1

event_table=dict(event_table)

wanted=event_table[max(event_table,key=event_table.get)]

ans=[]

for k,v in event_table.items():
    if v==wanted:
        ans.append(k)

ans.sort(reverse=True)

print(*ans)