import sys

player=-1
while player not in (1,0):
    player=int(input("First Player(0) or Second player(1) : "))
if player==0:
    player=True
else:
    player=False
if player:
    p,b='X','O'
    M=10
else:
    b,p='X','O'
    M=-10

turn=True

board=[
    ['-']*3,
    ['-']*3,
    ['-']*3
    ]
print()

def printBoard():
    for i in board:
        print(" ".join(i))
    
def playerTurn():
    global board
    i=j=0
    while not 1<=i<=3 or not 1<=j<=3 or board[i-1][j-1]!="-":
        i=int(input("Valid Row:"))
        j=int(input("Valid Column:"))
    board[i-1][j-1]=p

def MovesPresent(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]=='-':
                return True
    return False
    
def Evaluate(board):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]:
            if board[i][0]==p:
                return M
            elif board[i][0]==b:
                return -M

        if board[0][i]==board[1][i]==board[2][i]:
            if board[0][i]==p:
                return M
            elif board[0][i]==b:
                return -M

    if board[0][0]==board[1][1]==board[2][2]:
        if board[0][0]==p:
            return M
        elif board[0][0]==b:
            return -M

    if board[0][2]==board[1][1]==board[2][0]:
        if board[0][2]==p:
            return M
        elif board[0][2]==b:
            return -M
    return 0

def bestVal(board,turn):
    score=Evaluate(board)
    if score==M or score==-M:
        return score,
    elif not MovesPresent(board):
        return 0,
    if turn==player:
        x=p
    else:
        x=b
    BestM=(-1,-1)
    if turn:
        bestV=-100
        for i in range(3):
            for j in range(3):
                if board[i][j]=='-':
                    board[i][j]=x
                    curVal=bestVal(board,not turn)[0]
                    board[i][j]='-'
                    if curVal>bestV:
                        bestV=curVal
                        BestM=(i,j)
        return bestV,BestM
    else:
        bestV=100
        for i in range(3):
            for j in range(3):
                if board[i][j]=='-':
                    board[i][j]=x
                    curVal=(bestVal(board,not turn))[0]
                    board[i][j]='-'
                    if curVal<bestV:
                        bestV=curVal
                        BestM=(i,j)
        return bestV,BestM

def botMove():
    global board,turn
    Val,move=bestVal(board,turn)
    board[move[0]][move[1]]=b
print("Player :",p,"\tBot :",b)
print("Board:") 
printBoard()
while MovesPresent(board):
    if turn==player:
        print("Player Turn:")
        playerTurn()
        printBoard()
        if Evaluate(board)==M:
            print("Player wins.")
            sys.exit()
    else:
        print("Bot Turn:")
        botMove()
        printBoard()
        if Evaluate(board)==-M:
            print("Bot wins.")
            sys.exit()
    turn= not turn

print("Draw.")
