n = int(input())
dp = [[0]*5 for i in range(n+1)]
for i in range(5):
    dp[1][i] = 1
for i in range(2, n+1):
    # 실제 코드에서는 인덱스 때문에, DP[1][0] ~ DP[1][4]로 설정했습니다.
    dp[i][0] = (dp[i-1][0]+dp[i-1][1]+dp[i-1][2]+dp[i-1][3]+dp[i-1][4])%100000007
    dp[i][1] = (dp[i-1][0] + dp[i-1][2] + dp[i-1][3])%100000007
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][3] + dp[i-1][4])%100000007
    dp[i][3] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%100000007
    dp[i][4] = (dp[i-1][0] + dp[i-1][2])%100000007
print((dp[n][0] + dp[n][1] + dp[n][2] + dp[n][3] + dp[n][4])%100000007)

# import sys
# from collections import defaultdict

# sys.setrecursionlimit(10*8)

# n=int(input())
# m=n

# graph=[[0,1,2,3,4],[0,2,3],[0,1,3,4],[0,1,2],[0,2]]
# table_list=[0]
# cache=defaultdict(int)    #(tabletype,remainedline):casenum

# def recurs_tbl(n):
#     cnt=0
#     prev=table_list[-1]
#     #print(table_list)
    
#     if n==0:
#         cnt=1
    
#     elif cache[(prev,n)]:
#         cnt=cache[(prev,n)]
    
#     elif len(table_list)==m+1:
#         cnt=1
#         cache[(prev,n)]=cnt
    
#     else:
#         next=graph[prev]
#         for i in next:
#             table_list.append(i)
#             cnt+=recurs_tbl(n-1)
#             table_list.pop()
    
#         cache[(prev,n)]=cnt
    
#     cnt%=100000007
#     return cnt

# ans=recurs_tbl(n)
# ans%=100000007

# print(ans)