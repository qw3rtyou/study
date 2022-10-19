#-*- coding: utf-8 -*-
#부녀회장이 될거야

cache={}

def accumulator(a,b):
    if cache.get((a,b),None) is not None:	
        return cache[(a,b)]
    
    elif b==1:
        return 1
    
    elif a==0:
        return b
    
    else:
        cache[(a,b)]=accumulator(a,b-1)+accumulator(a-1,b)
        return cache[(a,b)]
    
num=int(input())
answer_list=[]

for _ in range(num):
    answer_list.append(accumulator(int(input()),int(input())))
    
for i in range(num):
    print(answer_list[i])