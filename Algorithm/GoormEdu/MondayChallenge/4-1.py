# from collections import deque

# n,m=map(int,input().split())

# rsv=deque()

# for i in range(m):
#     typ,mny=input().split()
#     mny=int(mny)
    
#     if typ[0]=='d':
#         n+=mny
#         while rsv and rsv[0]<=n:
#             n-=rsv[0]
#             rsv.popleft()
        
#     elif typ[0]=='p' and mny<=n:
#         n-=mny
        
#     elif typ[0]=='r':
#         if not rsv and mny<=n:
#             n-=mny
#         else:
#             rsv.append(mny)
            
# print(n)

from collections import deque

N, M = map(int, input().split())
Q = deque()

for i in range(M):
	op, k = input().split()
	k = int(k)
	
	if op == "deposit":
		N = N + k

		# 잔액이 늘어난 뒤에, 현재 대기 목록에 있는 거래가 결제될 수 있는지를 판단합니다.
		# 큐가 비어있는데 큐의 맨 앞 원소에 접근을 하면 IndexError가 뜨므로,
		# 항상 큐의 원소가 들어있는지를 확인하는 과정이 필요합니다.
		while Q and Q[0] <= N:
			# 거래가 가능한 경우에는 거래를 하고, 다시 위의 과정을 반복합니다.
			N = N - Q[0]
			Q.popleft()

	elif op == "pay":
		if N >= k:
			N = N - k

	elif op == "reservation":
		if not Q and N >= k:
			N = N - k
		else:
			# reservation에서 거래가 실패할 경우에는, 큐에 거래 내역을 추가합니다.
			Q.append(k)

print(N)