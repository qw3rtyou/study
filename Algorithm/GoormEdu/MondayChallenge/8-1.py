from collections import defaultdict,deque

n=int(input())
data=deque()
for letter in str(input()):
    data.append(letter)

table=defaultdict()
table["qw"]=1
table["as"]=2
table["zx"]=3
table["we"]=4
table["sd"]=5
table["xc"]=6
table["er"]=7
table["df"]=8
table["cv"]=9
table["ze"]=0

ans=""

for i in range(1,n):
    key=str(data[i-1])+str(data[i])
    if key in table:
        ans+=str(table[key])

print(ans)