def check_food(i,j):
    for k in range(1,m+1):
        for a in range(k+1):
            b=k-a
            if i+a<n and j+b<n and board[i+a][j+b]==2:
                return True
            if i-a>=0 and j+b<n and board[i-a][j+b]==2:
                return True
            if i+a<n and j-b>=0 and board[i+a][j-b]==2:
                return True
            if i-a>=0 and j-b>=0 and board[i-a][j-b]==2:
                return True
            
    return False

n,m=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            if not check_food(i,j):
                board[i][j]=0
                
count=0

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            count+=1
            
print(count)