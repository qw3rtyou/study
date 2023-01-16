import sys
import string
alpha_small = list(string.ascii_lowercase)
input = sys.stdin.readline
n = int(input())
arr = list(input().rstrip())
res = ''
for i in range(0, n, 2):
	ch = arr[i]
	num = int(arr[i+1])
	index = (alpha_small.index(ch) + (num * num))%26
	res += alpha_small[index]
print(res)






# def decrypt(let,num):
#     l=ord(str(let))
#     return chr((l-97+int(num)**2)%26+97)
        

# size=int(input())
# s=str(input())
# output=""

# for i in range(len(s)):
#     if i%2==0:
#         output+=decrypt(s[i],s[i+1])
        
# print(str(output))