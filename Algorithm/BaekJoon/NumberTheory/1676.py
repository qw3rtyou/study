def factorial(n):
    if n<2:
        return 1
    
    else:
        return n*factorial(n-1)
    
n=int(input())

data=str(factorial(n))

count=0

for i in range(len(data)-1,0,-1):
    if data[i]=='0':
        count+=1
    else:
        break
        
print(count)