prev_char=""

length=int(input())
n=length

for letter in str(input()):
    if letter==prev_char:
        n=n-1
        
    prev_char=letter
    
print(n)
    