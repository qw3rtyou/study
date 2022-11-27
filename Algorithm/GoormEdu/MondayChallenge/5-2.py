from collections import deque
import sys
input=sys.stdin.readline

def timePasses(board):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    wave_of_time=[[0 for _ in range(n)] for _ in range(m)]
    
    
    for i in range(m):
        for j in range(n):
            
            if board[i][j]==0:
                for k in range(4):
                    x=dx[k]
                    y=dy[k]
                    if i+x<0 or j+y<0 or i+x>=m or j+y>=n:
                        continue

                    if board[i+x][j+y]==1:
                    	wave_of_time[i+x][j+y]=1
    
    for i in range(m):
        for j in range(n):
            if wave_of_time[i][j]==1:
                board[i][j]=0
        
def checkSplit(board):   
    start=None
    
    for i in range(m):
        if start:
            break
        for j in range(n):
            if board[i][j]==1:
                start=(i,j)
                break
                
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    next_stack=deque()
    next_stack.append(start)
    island=list()
    
    while True:
        
        if not next_stack:
            break
        
        cur=next_stack.pop()
        island.append(cur)
        
        for k in range(4):
            x=cur[0]+dx[k]
            y=cur[1]+dy[k]
            if x<0 or y<0 or x>=m or y>=n:
                continue
            if board[x][y]==1 and (x,y) not in island:
                next_stack.append((x,y))
        
    flag=False

    for i in range(m):
        for j in range(n):
            if board[i][j]==1 and (i,j) not in island:
                flag=True
    
    return flag

def checkSink(board):
    flag=True
    for line in board:
        for cell in line:
            if cell==1:
                flag=False
    return flag


m,n=map(int,input().split())
board=[[i for i in map(int,input().split())] for _ in range(m)]
cnt=1

while(True):
    timePasses(board)
    
    if checkSink(board):
        print(-1)
        exit(0)
    
    elif checkSplit(board):
        print(cnt)
        exit(0)
        
    cnt+=1
