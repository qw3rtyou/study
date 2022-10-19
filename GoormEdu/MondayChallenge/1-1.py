res=1

cases=list(map(int, input().split()))
for case in cases:
    res*=case

print(res)
