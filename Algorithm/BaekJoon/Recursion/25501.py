counter=0

def recursion(s, l, r):
    global counter
    counter+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


n=int(input())
words=[]

for _ in range(n):
    words.append(str(input()))
    
for word in words:
    print(isPalindrome(word),counter)
    counter=0