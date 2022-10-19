#-*- coding: utf-8 -*-
#소인수분해

def print_Prime(num):
    for i in range(2,num):
        if num%i==0:
            print(i)
            print_Prime(num//i)
            return True
        
    print(num)
    return True

num=int(input())

if num !=1:
    print_Prime(num)