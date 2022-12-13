import sys
input=sys.stdin.readline

n,m=map(int,input().split())
pokemon_dict=dict()

for i in range(n):
    pokemon_dict[str(input())]=i+1
    
problem_list=list()

for _ in range(m):
    problem_list.append(input())
    
for prob in problem_list:
    if 47<ord(str(prob[0]))<58:
        print(pokemon_dict[int(prob)],end="")
        
    else:
        print(pokemon_dict[prob])
        
        
        
        딕셔너리로 풀어야할듯.. autoincreasement루다가..