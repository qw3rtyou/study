import sys

def hanoi(n,src,dst):
    mid=6-src-dst
    global proc
    global move
    
    if n==1:
        proc.append((src,dst))
        move+=1
    elif n==2:
        hanoi(1,src,mid)
        hanoi(1,src,dst)
        hanoi(1,mid,dst)
    else:
        hanoi(n-1,src,mid)
        hanoi(1,src,dst)
        hanoi(n-1,mid,dst)
        
    return proc,move

size=int(sys.stdin.readline())
proc=[]
move=0

proc,move=hanoi(size,1,3)

print(move)

for proc,move in proc:
    print(proc,move)