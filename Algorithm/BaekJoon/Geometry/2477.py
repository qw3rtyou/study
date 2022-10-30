import sys
input=sys.stdin.readline

multi_value=int(input())

movement=[]
target=[(1,3),(4,1),(2,4),(3,2)]
prev_move=(0,0)
target_area=0

for _ in range(6):
	movement.append(tuple(map(int,input().split())))
    
prev_move=movement[-1]
		
for i in range(6):
	if target_area!=0:
		break
	for target_move in target:
		if (prev_move[0],movement[i][0])==target_move:
			target_area=prev_move[1]*movement[i][1]
			break
		prev_move=movement[i]

a=max([movement[i][1] for i in range(0,6,2)])
b=max([movement[i][1] for i in range(1,6,2)])

ans=multi_value*(a*b-target_area)

print(ans)