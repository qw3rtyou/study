import sys
input=sys.stdin.readline

data=input().strip()
count=0

while len(str(data))!=1:
    
    tmp=1

    for letter in str(data):
        tmp*=int(letter)

    data=tmp
    count+=1
    
print(count)