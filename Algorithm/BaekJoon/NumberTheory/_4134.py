import sys

input = sys.stdin.readline

MAX_INPUT = 4 * 10**9

size = int(input())
for i in range(size):
    pass

seive = [True] * int(MAX_INPUT * 1.2)


def gen_seive():
    seive_size = len(seive)
    for i in range(2, seive_size**0.5):
        for j in range(0, seive_size, i):
            seive[j] = False


def is_prime():
    return seive


if __name__ == "__main__":
    gen_seive()
