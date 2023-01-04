import sys
input=sys.stdin.readline

n,m=map(int,input().split())
board=[list(str(input()).rstrip()) for i in range(n)]

print(board)

for i in range(n):
    for j in range(m):
        if board[i][j]=="B":
            board[i][j]=1
        else:
            board[i][j]=0
            
print(board)

checker1=[[0]*8 for i in range(8)]
for i in range(8):
    for j in range(8):
        if (i+j)%2==1:
            checker1[i][j]=1

checker2=[[0]*8 for i in range(8)]
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            checker2[i][j]=1

# print(checker1)
# print(checker2)

def check(a,b):
    err1=0
    err2=0
    
    for i in range(8):
        for j in range(8):
            if board[a+i][b+j]!=checker1[i][j]:
                err1+=1
            if board[a+i][b+j]!=checker2[i][j]:
                err2+=1
                
    return min(err1,err2)
                
ans=0
for i in range(n-7):
    for j in range(m-7):
        ans=min(ans,check(i,j))
        
print(ans)