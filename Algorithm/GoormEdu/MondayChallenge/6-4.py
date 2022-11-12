n,k=map(int,input().split())
ans=0

board=dict()

for i in range(1001):
    for j in range(1001):
        crd=(i,j)
        board[crd]=0

for _ in range(n):
    a,b,c,d=map(int,input().split())
    
    for i in range(a,c+1):
        for j in range(b,d+1):
            crd=(i,j)
            board[crd]+=1

for i in range(1001):
    for j in range(1001):
        crd=(i,j)
        # if board[crd]!=0:
        #     print(crd)
        if board[crd]==k:
            ans+=1

#print(board)
print(ans)