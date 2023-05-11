import sys
input = sys.stdin.readline


def find_prime_under_then(target):
    for i in range(top, target+1):
        if seive[i]:
            for x in range(0, target, i):
                seive[i] = False


def find_partition(target):
    tmp = seive[:target]
    primes = [i for i, x in enumerate(tmp) if x]
    cnt = 0
    print(seive)
    print(primes)
    for prime in primes:
        if (target-prime in primes):
            print("\np : "+str(target-prime), " q : "+str(prime))
            cnt += 1

    return cnt//2+1


t = int(input())
seive = [False]*2+[True]*1000000    # 0부터 소수담기
top = 0

for _ in range(t):
    n = int(input())

    if top < n:
        find_prime_under_then(n)
        top = n

    print(find_partition(n))
