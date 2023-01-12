from math import inf

n=int(input())
series=list(map(int,input().split()))

def seq_sum(start,end,series):
    if end-start<=1:
        return series[start]
    
    new_max=-inf
    for i in range(start+1,end):
        tmp=sum(series[start:i])
        new_max=max(tmp,new_max)
                    
    return max(new_max,seq_sum(start+1,end,series))

print(seq_sum(0,n,series))