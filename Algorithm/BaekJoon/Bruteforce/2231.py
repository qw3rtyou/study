target=int(input())
flag=False

for i in range(target):
    s=0
    for letter in str(i):
        s+=int(letter)
    s+=i
    
    if s==target:
        flag=True
        print(i)
        break

if not flag:
    print(0)