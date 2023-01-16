def check_multi(a,b):
    if a%b==0:
        return True
    
    else:
        return False

while True:
    a,b=map(int,input().split())
    
    if a==0 or b==0:
        break

    elif check_multi(a,b):
        print("multiple")

    elif check_multi(b,a):
        print("factor")

    else:
        print("neither")