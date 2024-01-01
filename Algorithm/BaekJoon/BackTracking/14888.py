import sys
import math

input = sys.stdin.readline
size = int(input())
data = list(map(int, input().split()))
op = list(map(int, input().split()))
used = [0] * 4
min = math.inf
max = -math.inf


def rec(res, idx):
    global min, max

    if idx + 1 == size:
        if min > res:
            min = res

        if max < res:
            max = res
        return

    if op[0] - used[0]:
        used[0] += 1
        rec(res + data[idx + 1], idx + 1)
        used[0] -= 1

    if op[1] - used[1]:
        used[1] += 1
        rec(res - data[idx + 1], idx + 1)
        used[1] -= 1

    if op[2] - used[2]:
        used[2] += 1
        rec(res * data[idx + 1], idx + 1)
        used[2] -= 1

    if op[3] - used[3]:
        used[3] += 1
        if res < 0 and data[idx + 1] > 0:
            rec(-(-res // data[idx + 1]), idx + 1)
        else:
            rec(res // data[idx + 1], idx + 1)
        used[3] -= 1


if __name__ == "__main__":
    rec(data[0], 0)
    print(max, min)

"""
2
5 6
0 0 1 0

3
3 4 5
1 0 1 0
"""
