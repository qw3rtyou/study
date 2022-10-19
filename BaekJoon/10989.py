import sys

read = lambda: sys.stdin.readline()

N = int(read())

numbers = [0] * 10001

for i in range(N):
    numbers[int(read())] += 1

for i in range(10001):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            print(i)