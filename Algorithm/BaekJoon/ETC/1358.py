def check_in_circle(a,b,x,y,r):
    return (x-a)**2+(y-b)**2<=r**2

def check_inside(w,h,x,y,a,b):
    r=int(h/2)
    left=check_in_circle(a,b,x,y+r,r)
    mid=((a>=x)and(a<=x+w)and(b>=y)and(b<=y+h))
    right=check_in_circle(a,b,x+w,y+r,r)
    
    return (left or mid or right)


w,h,x,y,p=map(int,input().split())
count=0
for _ in range(p):
    a,b=map(int,input().split())
    if check_inside(w,h,x,y,a,b):
        count+=1
        
print(count)