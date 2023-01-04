import sys

input=sys.stdin.readline

n=int(input())
graph=[[i for i in map(int,input().split())] for i in range(n)]

my_team=list()
ans=list()

def dfs():
    if len(my_team)==n//2:
        your_team=list()
        
        for member in range(n):
            if member not in my_team:
                your_team.append(member)
        #print(my_team,your_team)
        
        ans.append(abs(cal_ability(my_team)-cal_ability(your_team)))
        
        #print(ans)
        return
    
    for member in range(n):
        if member in my_team:
            continue
            
        my_team.append(member)
        dfs()
        my_team.pop()
        
def cal_ability(team):
    pairs=list()
    for member1 in team:
        for member2 in team:
            if member1!=member2:
                pairs.append((member1,member2))
                
    synergy_sum=0
    
    for pair in pairs:
        synergy_sum+=graph[pair[0]][pair[1]]+graph[pair[1]][pair[0]]
        
    return synergy_sum//2

dfs()
print(min(ans))