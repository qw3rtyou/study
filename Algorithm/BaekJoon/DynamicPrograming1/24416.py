import sys

input = sys.stdin.readline

count = [0] * 41

count[0] = count[1] = count[2] = 1


def recur_fib(n):
    if count[n] != 0:
        return count[n]

    count[n] = recur_fib(n - 1) + recur_fib(n - 2)
    return count[n]


fib = dict()

fib[1] = 1
fib[2] = 1


def dynamic_fib(n):
    global count

    for i in range(3, n + 1):
        count += 1
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


k = int(input())

recur_fib(k)
print(count[k], end=" ")

count = 0

dynamic_fib(k)
print(count)
