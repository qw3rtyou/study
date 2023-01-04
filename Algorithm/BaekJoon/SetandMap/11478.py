s=input()
n=len(s)
ans=set()

for i in range(n):
    for j in range(i+1,n+1):
        ans.add(s[i:j])
        
print(len(ans))