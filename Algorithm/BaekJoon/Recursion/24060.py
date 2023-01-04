def merge_sort(data,start,end):
    if end>start:
        mid=(start+end)//2
        merge_sort(data,start,mid)
        merge_sort(data,mid+1,end)
        merge(data,start,mid,end)
        
def merge(data,start,mid,end):
    i=start
    j=mid+1
    t=0
    tmp=[]
    
    while i<=mid and j<=end:
        if data[i]<data[j]:
            tmp.append(data[i])
            t+=1
            i+=1
        else:
            tmp.append(data[j])
            t+=1
            j+=1
            
    while i<=mid:
        tmp.append(data[i])
        i+=1
        t+=1
    
    while j<=end:
        tmp.append(data[j])
        j+=1
        t+=1
        
    count=0
    
    for i in range(start,end+1):
        data[i]=tmp[count]
        count+=1
        ans.append(data[i])
        
ans=[]
n,k=map(int,input().split())
data=list(map(int,input().split()))
merge_sort(data,0,len(data)-1)

if len(ans)<k:
    print(-1)
else:
    print(ans[k-1])
