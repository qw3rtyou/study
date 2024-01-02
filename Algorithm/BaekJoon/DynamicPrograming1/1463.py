import sys
from math import inf
from collections import defaultdict

sys.setrecursionlimit(3000)
input = sys.stdin.readline
n = int(input())


def default_value():
    return inf


dp = defaultdict(default_value)
dp[0] = 0
dp[1] = 0
dp[2] = 1


def rec(n):
    if dp[n] is not inf:
        return dp[n]

    if n < 2:
        return 0

    tmp = 0
    if n % 6 == 0:
        tmp = (
            min(
                rec(n // 3),
                rec(n - 1),
                rec((n - 2) // 2),
            )
            + 1
        )

    elif n % 3 == 0:
        tmp = (
            min(
                rec(n // 3),
                rec((n - 1) // 2),
                rec(n - 2),
            )
            + 1
        )

    elif n % 2 == 0:
        tmp = min(rec(n // 2), rec(n - 1)) + 1

    else:
        tmp = rec(n - 1) + 1

    dp[n] = min(dp[n], tmp)

    return dp[n]


if __name__ == "__main__":
    rec(n)
    print(dp[n])


# 'Bottom-Up' 동적 프로그래밍을 사용
# n을 1씩 뺄 수 있는 경우, n을 2로 나눌 수 있는 경우, n을 3으로 나눌 수 있는 경우를 각각 고려
# round 2!!
