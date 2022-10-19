#-*- coding: utf-8 -*-
#ACM호텔

t=int(input())
answers=[]

for _ in range(t):
    h,w,n=map(int,input().split())
    if(n%h==0):
        answers.append(n//h+h*100)
    else:
        answers.append(n//h+1+(n%h)*100)
    
for i in range(t):
    print(answers[i])