n,m=map(int,input().split())    #n:event_type_num    m:user_num
from collections import defaultdict

event_table=defaultdict(int)

for _ in range(m):
    data=list(map(int,input().split()))
    #e=data[0]    #e:used_event_time    ->useless
    for event_num in data[1:]:
        event_table[event_num]+=1

sorted_table=sorted(event_table.items(),key=lambda x:(x[1],x[0]),reverse=True)

max_cnt=sorted_table[0][1]
ans=list()
ans.append(sorted_table[0][0])
i=0

while True:
    if len(sorted_table)<i:
        break
    
    if sorted_table[i][1]==max_cnt:
        ans.append(sorted_table[i][0])
        i+=1
    else:
        break
        
print(*ans)
