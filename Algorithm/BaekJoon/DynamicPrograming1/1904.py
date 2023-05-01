#행렬의 멱법
import sys
read = sys.stdin.readline

N = int(read())
A = [[1, 1], [1, 0]]

def matrix_mult(A, B):
    temp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (A[i][k] * B[k][j])

    for i in range(2):
        for j in range(2):
            temp[i][j] %= 15746
    return temp

def matrix_pow(n, M):
    if n == 1:
        return M
    if n % 2 == 0:
        temp = matrix_pow(n//2, M)
        return matrix_mult(temp, temp)
    else:
        temp = matrix_pow(n-1, M)
        return matrix_mult(temp, M)

print(matrix_pow(N, A)[0][0])








#캐시메모리 지우고 변수값을 계속 수정하여 풀이
# import sys
# read = sys.stdin.readline

# N = int(read())
# n1 = 1
# n2 = 2
# res = 1 if N == 1 else 2

# for i in range(3, N+1):
#     res = (n1 + n2) % 15746
#     n1, n2 = n2, res
# print(res)








#일반적인 풀이
# import sys
# from collections import defaultdict

# sys.setrecursionlimit(10**8)
# input=sys.stdin.readline
# cache=defaultdict(int)
# cache[1]=1
# cache[2]=2

# n=int(input())

# for i in range(3,n+1):
#     cache[i]=(cache[i-1]+cache[i-2])%15746
    
# print(cache[n])

