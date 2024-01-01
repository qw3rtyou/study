# from collections import deque
# import sys


# input = sys.stdin.readline
# n = int(input())
# stack = deque()
# cnt = 0


# def dfs_queen():
#     global cnt

#     if not is_observe_rules():
#         return

#     if len(stack) == n:
#         cnt += 1
#         return

#     for element in range(n):
#         if element in stack:
#             continue

#         stack.append(element)
#         dfs_queen()
#         stack.pop()


# def is_observe_rules():
#     if not stack:
#         return True

#     x = len(stack) - 1
#     y = stack[-1]

#     for i in range(len(stack)):
#         if x == i:
#             continue

#         if (y - stack[i]) / (x - i) == -1 or (y - stack[i]) / (x - i) == 1:
#             return False

#         if stack[i] == stack[x]:
#             return False

#     return True


# if __name__ == "__main__":
#     dfs_queen()
#     print(cnt)

# time out~


import sys

input = sys.stdin.readline
n = int(input())
cnt = 0

row = [0] * n

diag1 = [0] * (2 * n - 1)
diag2 = [0] * (2 * n - 1)


def fkingQueen(x):
    global cnt
    if x == n:
        cnt += 1
        # print(diag1)
        return

    for y in range(n):
        if row[y] or diag1[x + y] or diag2[n - 1 + x - y]:
            continue

        diag1[x + y] = diag2[n - 1 + x - y] = row[y] = 1
        fkingQueen(x + 1)
        diag1[x + y] = diag2[n - 1 + x - y] = row[y] = 0


if __name__ == "__main__":
    fkingQueen(0)
    print(cnt)
