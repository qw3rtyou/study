def pivo(n):
    if n<=1:
        return n
    
    return pivo(n-2)+pivo(n-1)

n=int(input())

print(pivo(n))