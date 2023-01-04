#-*- coding: utf-8 -*-
#설탕 배달

n=int(input())
if n is 4 or n is 7:
    print(-1)
    
elif n%5%3 is 0:
    print(n//5+n%5//3)
    
elif n%5%3 is 1:
    print(n//5+n%5//3+1)
    
else:
    print(n//5+n%5//3+2)