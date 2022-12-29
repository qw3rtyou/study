import sys
from collections import defaultdict
input=sys.stdin.readline

case_num=int(input())
cases=list()

for _ in range(case_num):
    cases.append(int(input()))
    
board=defaultdict(int)

def waves(n):
    if n<4:
        return 1
    if board[n]:
        return board[n]
    tmp=waves(n-2)+waves(n-3)
    board[n]=tmp
    return board[n]

for case in cases:
    print(waves(case))