#-*- coding: utf-8 -*-
#소수 찾기

def prime_Checker(n):
    if n == 1:
        return False
    
    for i in range(2,n):
        if n%i == 0:
            return False
    return True


length=int(input())
num_List=[]
count=0

num_List=list(map(int,input().split()))

for i in range(length):
    if prime_Checker(num_List[i]):
        count+=1
        
print(count)