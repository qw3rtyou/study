import sys

def check_inside(a,b,x,y,r):
    return ((x-a)**2+(y-b)**2<r**2)


test_case=int(input())
counter=0
ans=[]

for _ in range(test_case):
    srcx,srcy,dstx,dsty=map(int,input().split())
    planet_num=int(input())
    
    for i in range(planet_num):
        x,y,r=map(int,sys.stdin.readline().split())
        #print("case "+str(i)+" ")
        #print(x,y,r,a,b,c)
        if check_inside(srcx,srcy,x,y,r)^check_inside(dstx,dsty,x,y,r):
            counter+=1
            
    ans.append(counter)
    counter=0
    
for a in ans:
    print(a)