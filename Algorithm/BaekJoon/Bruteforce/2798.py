n,m=map(int,input().split())

values=list(map(int,input().split()))
mx_mem=0

for first in values:
    for second in values:
        if first==second:
            continue
        for third in values:
            if second==third or first==third:
                continue
            
            val=first+second+third
            
            if val>m:
                continue
            elif mx_mem<val<=m: 
                mx_mem=val
                
print(mx_mem)