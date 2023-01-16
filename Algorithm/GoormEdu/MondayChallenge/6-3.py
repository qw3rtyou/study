def encrypt(data,key):
    out=""
    
    for i in range(len(data)):
        d=ord(str(data[i]))
        k=ord(str(key[i]))
        if d>=65 and d<=90 or d>=97 and d<=122:
            cor=97 if d>95 else 65
            out+=chr((d-cor+k%26)%26+cor)
        else:
            out+=chr(d)
    
    return out

def decrypt(data,key):
    out=""
    
    for i in range(len(data)):
        d=ord(str(data[i]))
        k=ord(str(key[i]))
        if d>=65 and d<=90 or d>=97 and d<=122:
            cor=97 if d>95 else 65
            out+=chr((d-cor-k%26)%26+cor)
        else:
            out+=chr(d)
    
    return out


size=int(input())
output=[]

for _ in range(size):
    data=str(input())
    op,key=map(str, input().split())
    
    for cnt in range(len(data)-len(key)):
        key+=key[cnt%len(key)]
        
    #print(data,key)
    
    if op=="E":
        output.append(encrypt(data,key))
    else:
        output.append(decrypt(data,key))
        
for o in output:
    print(o)
    