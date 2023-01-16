import sys

input=sys.stdin.readline

poke_num,prob_num=map(int,input().split())
poke_dict1=dict()
poke_dict2=dict()
prob_list=list()

for i in range(poke_num):
    data=str(input().rstrip())
    poke_dict1[i]=data
    poke_dict2[data]=i

for _ in range(prob_num):
    prob_list.append(str(input().rstrip()))

for prob in prob_list:
    if prob.isdigit():
        print(poke_dict1[int(prob)-1])

    else:
        print(poke_dict2[prob]+1)
















# 시간초과...
# poke_num,prob_num=map(int,input().split())
# pokemon_list=list()
# prob_list=list()

# for i in range(poke_num):
#     pokemon_list.append(str(input()))

# for _ in range(prob_num):
#     prob_list.append(str(input()))

# for prob in prob_list:
#     if prob.isdigit():
#         print(int(prob)-1)
#         print(pokemon_list[int(prob)-1])

#     else:
#         print(pokemon_list.index(prob)+1)