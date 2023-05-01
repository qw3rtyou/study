ans=[]

for _ in range(5):
    data=str(input())
    cnt=1
    a=0

    for letter in data:    
        if cnt%2==1:
            a+=int(letter)
            # print(letter)
            # print(a)
        cnt+=1
        
    cnt=1
    for letter in data:    
        if cnt%2==0 and int(letter)!=0:
            a*=int(letter)
            # print(letter)
            # print(a)
        cnt+=1

    ans.append(a%10)

for a in ans:
    print(a)