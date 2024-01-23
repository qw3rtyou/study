# from collections import defaultdict
# from math import inf

# n = int(input())
# series = list(map(int, input().split()))

# dict = defaultdict(int)


# def seq_sum(start, end):
#     if end - start <= 1:
#         return series[start]

#     new_max = -inf
#     max_end = end
#     for i in range(start + 1, end):
#         tmp = sum(series[start:i])

#         if tmp > new_max:
#             new_max = tmp
#             max_end = i

#     max_start = start
#     for i in range(start, end - 1):
#         tmp = sum(series[i:end])

#         if tmp > new_max:
#             new_max = tmp
#             max_start = i

#     print(max_start, max_end)

#     return sum(series[max_start:max_end])


# if __name__ == "__main__":
#     print(seq_sum(0, n))


# 시간초과 ------------ Round2
# kadane 알고리즘 적용

n = int(input())
data = list(map(int, input().split()))
max_subsum = data.copy()


def seq_sum():
    for i in range(1, n):
        if data[i] < data[i] + max_subsum[i - 1]:
            max_subsum[i] = max_subsum[i - 1] + data[i]


if __name__ == "__main__":
    seq_sum()
    # print(max_subsum)
    print(max(max_subsum))
