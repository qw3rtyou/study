def decrypt(let,num):
    l=ord(str(let))
    return chr((l-97+int(num)**2)%26+97)
        

size=int(input())
s=str(input())
output=""

for i in range(len(s)):
    if i%2==0:
        output+=decrypt(s[i],s[i+1])
        
print(str(output))