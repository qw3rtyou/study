import sys
from math import inf
from collections import defaultdict

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input())


def default_value():
    return inf


dp = defaultdict(default_value)
dp[0] = 0
dp[1] = 0
dp[2] = 1


def rec(n, depth):
    if dp[n] is not inf or dp[n] < depth:
        return dp[n]

    if n < 2:
        return 0

    tmp = []

    if n % 3 == 0:
        tmp.append(rec(n // 3, depth + 1) + 1)

    if n % 2 == 0:
        tmp.append(rec(n // 2, depth + 1) + 1)

    tmp.append(rec(n - 1, depth + 1) + 1)
    tmp.append(dp[n])

    dp[n] = min(tmp)

    return dp[n]


def bottom_up(n):
    pass


if __name__ == "__main__":
    rec(n, 0)
    print(dp[n])
