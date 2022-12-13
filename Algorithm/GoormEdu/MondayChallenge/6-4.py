import sys
input = sys.stdin.readline

N, K = map(int, input().split())
L = 1004
ans = 0

S = [[0 for _ in range(L)] for _ in range(L)]
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    S[y1][x1] += 1
    S[y1][x2] -= 1
    S[y2][x1] -= 1
    S[y2][x2] += 1
    
# 가로로 복원
for i in range(L):
    for j in range(1, L):
        S[i][j] += S[i][j - 1]
        
# 세로로 복원
for j in range(L):
    for i in range(1, L):
        S[i][j] += S[i - 1][j]
    
for i in range(L):
    for j in range(L):
        if S[i][j] == K: ans += 1
        
print(ans)
















# n,k=map(int,input().split())
# ans=0

# board=dict()

# for i in range(1001):
#     for j in range(1001):
#         crd=(i,j)
#         board[crd]=0

# for _ in range(n):
#     a,b,c,d=map(int,input().split())
    
#     for i in range(a,c+1):
#         for j in range(b,d+1):
#             crd=(i,j)
#             board[crd]+=1

# for i in range(1001):
#     for j in range(1001):
#         crd=(i,j)
#         # if board[crd]!=0:
#         #     print(crd)
#         if board[crd]==k:
#             ans+=1

# #print(board)
# print(ans)