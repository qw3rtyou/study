from collections import defaultdict

cache=defaultdict(int)

def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    
    elif a>20 or b>20 or c>20:
        if cache[(20,20,20)]:
            return cache[(20,20,20)]
        return w(20,20,20)
    
    elif a<b and b<c:
        coop1=(a,b,c-1)
        coop2=(a,b-1,c-1)
        coop3=(a,b-1,c)
        
        A=None
        B=None
        C=None
        
        if cache[coop1]:
            A=cache[coop1]
        else:
            cache[coop1]=w(a,b,c-1)
            A=w(a,b-1,c)
        
        if cache[(a,b-1,c-1)]:
            B=cahce[(a,b-1,c-1)]
        else:
            cache[(a,b-1,c-1)]=w(a,b-1,c-1)
            B=w(a,b-1,c-1)
            
        if cache[(a,b-1,c)]:
            C=cache[(a,b-1,c)]
        else:
            cache[(a,b-1,c)]=w(a,b-1,c)
            C=w(a,b-1,c)
            
        return A+B+C
    
    else:
        A=None
        B=None
        C=None
        D=None
        
        return w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    
    