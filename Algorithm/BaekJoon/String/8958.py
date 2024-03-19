import sys

input = sys.stdin.readline

n = int(input())
cnt = 0


def rec(n):
    if n <= 1:
        return n
    else:
        return n + rec(n - 1)


for _ in range(n):
    data = input()
    cnt = 0
    words = data.split("X")
    for word in words:
        cleaned_text = word.strip()
        cnt += rec(len(cleaned_text))
    print(cnt)
    cnt = 0
