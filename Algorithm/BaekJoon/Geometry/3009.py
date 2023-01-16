arrx=[]
arry=[]

for _ in range(3):
    x,y=map(int,input().split())
    
    if x in arrx:
        arrx.remove(x)
    else:
        arrx.append(x)
    if y in arry:
        arry.remove(y)
    else:
        arry.append(y)
        
print(arrx[0],arry[0])