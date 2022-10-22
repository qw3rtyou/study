def design_pat(board,x1,y1,x2,y2):
    a=(2*x1+x2)//3
    b=(x1+2*x2)//3
    c=(2*y1+y2)//3
    d=(y1+2*y2)//3
    
    if x2-x1<=1:
        return
    
    for row in range(x1,x2):
        for col in range(y1,y2):
            if row>=a and row<b and col>=c and col<d:
                board[row][col]=" "
                
    if a>=1:
        design_pat(board,x1,y1,a,c)
        design_pat(board,a,y1,b,c)
        design_pat(board,b,y1,x2,c)
        design_pat(board,x1,c,a,d)
        #design_pat(board,a,c,b,d)
        design_pat(board,b,c,x2,d)
        design_pat(board,x1,d,a,y2)
        design_pat(board,a,d,b,y2)
        design_pat(board,b,d,x2,y2)
        
def print_dot(board):
    buf=""
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]=="*":
                buf+="*"
            else:
                buf+=" "
        print(buf)
        buf=""
        
        
size=int(input())
board=[["*"]*size for i in range(size)]
design_pat(board,0,0,size,size)
print_dot(board)