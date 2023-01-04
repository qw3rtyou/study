size, bomb_num=map(int, input().split())

if size==1:
    dmg=bomb_num
    
elif size==2:
    dmg=bomb_num*3

else:
    dmg=bomb_num*5

    for i in range(bomb_num):
        x,y=map(int, input().split())
        if (x==1 or x==size) and (y==1 or y==size):
            dmg-=2

        elif x==1 or x==size or y==1 or y==size:
            dmg-=1
        
print(dmg)