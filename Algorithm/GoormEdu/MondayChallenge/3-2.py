import sys
input=sys.stdin.readline

dic={
    1 : "1.,?!",
    2 : "2ABC",
    3 : "3DEF",
    4 : "4GHI",
    5 : "5JKL",
    6 : "6MNO",
    7 : "7PQRS",
    8 : "8TUV",
    9 : "9WXYZ"
}

size=int(input())
data=input()
ans=""
cnt=0

for i in range(size):
    if data[i]==data[i+1]:
        cnt+=1
        
    else:
        cnt%=len(dic[int(data[i])])
        ans+=dic[int(data[i])][cnt]
        cnt=0
        
print(ans)



#뻘짓
# import sys

# keypad={(1,1):"1",(1,2):".",(1,3):",",(1,4):"?",(1,5):"!",(2,1):"2",(2,2):"A",(2,3):"B",(2,4):"C",(3,1):"3",(3,2):"D",(3,3):"E",(3,4):"F",(4,1):"4",(4,2):"G",(4,3):"H",(4,4):"I",(5,1):"5",(5,2):"J",(5,3):"K",(5,4):"L",(6,1):"6",(6,2):"M",(6,3):"N",(6,4):"O",(7,1):"7",(7,2):"P",(7,3):"Q",(7,4):"R",(7,5):"S",(8,1):"8",(8,2):"T",(8,3):"U",(8,4):"V",(9,1):"9",(9,2):"W",(9,3):"X",(9,4):"Y",(9,5):"Z"}

# size=int(input())
# # data=[]

# # for _ in range(size):
# #     data.append(int(sys.stdin.read(1)))

# data=str(input())

# prev=None
# mes=""
# counter=1

# for letter in data:
#     if prev==None:
#         prev=letter
#     elif letter==prev:
#         counter+=1
#     else:
#         print(letter,counter)
#         mes+=str(keypad.get((letter,counter)))
#         counter=1
#         prev=letter
        
# print(mes)