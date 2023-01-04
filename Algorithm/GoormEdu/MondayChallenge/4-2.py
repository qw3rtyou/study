import sys
input=sys.stdin.readline

n=int(input())
feild=[]
flag=False

for _ in range(n):
    feild.append(list(map(int,input().split())))

chg=[[0]*n for i in range(n)]
ans=0

while not flag:
    flag=True
    for i in range(n):
        for j in range(n):
            if feild[i][j]!=0:
                flag=False
    if flag==True:
        break
    
    for i in range(n):
        for j in range(n):
            count=0

            if feild[i][j]!=0:           
                if i+1<n:
                    count+=1 if feild[i+1][j]==0 else 0
                if i-1>=0:
                    count+=1 if feild[i-1][j]==0 else 0
                if j+1<n:
                    count+=1 if feild[i][j+1]==0 else 0
                if j-1>=0:
                    count+=1 if feild[i][j-1]==0 else 0

            chg[i][j]=count

    for i in range(n):
        for j in range(n):
            feild[i][j]-=chg[i][j] if feild[i][j]>chg[i][j] else feild[i][j]
    
    flag=True
    for i in range(n):
        for j in range(n):
            if feild[i][j]!=0:
                flag=False
    
    ans+=1
    
print(ans)