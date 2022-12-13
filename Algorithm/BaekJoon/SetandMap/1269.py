a,b=map(int,input().split())

a_set=set(map(int,input().split()))
b_set=set(map(int,input().split()))

print(len(a_set-b_set)+len(b_set-a_set))