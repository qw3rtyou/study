k=int(input())

direction=[]
distance=[]

for _ in range(6):
    d,l=map(int,input().split())
    direction.append(d)
    distance.append(l)

max_index_A=distance.index(max([distance[i] for i in (1,3,5)]))
max_index_B=distance.index(max([distance[i] for i in (0,2,4)]))

a=distance[max_index_A]
b=distance[max_index_B]
if (direction[max_index_A]+direction[max_index_B])%2==0:
    c=distance[max_index_A-4]
    d=distance[max_index_B-2]
else:
    c=distance[max_index_A-2]
    d=distance[max_index_B-4]

print(a,b,c,d)
print(k*(a*b-c*d))