case=int(input())

ans=[]

for _ in range(case):
    suc_num=0
    stu_num=int(input())
    scores=list(map(int, input().split()))
    avg=sum(scores)/stu_num
    
    for score in scores:
        if score>=avg:
            suc_num+=1
    
    n,m=suc_num,stu_num
    print(str(n)+"/"+str(m))