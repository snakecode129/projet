import random
board =["-","-","-",
        "-","-","-",
        "-","-","-"]
currentpalyer="X"
winner=None
gamerunning=True


#printing the game board 

def printBoard(board):
    print(board[0] + "|" + board[1] + "|" +board[2])
    print(board[3] + "|" + board[4] + "|" +board[5])
    print(board[6] + "|" + board[7] + "|" +board[8])
printBoard(board)


#take palyer input
def playerinput(board):
    inp=int(input("donnez un nombre entre 1 et 9 "))
    if inp>=1 and inp<=9 and board[inp-1]=="-":
        board[inp-1]=currentpalyer
    else:
        print("il y deja un X ou O ")
    


#check for win or Tie
def checkhoriz(board):
     global winner
     if board[0] ==board[1] == board[2] and board[1]!="-" :
         winner= board[0]
         return True 
     elif board[3] ==board[4] == board[5] and board[3]!="-" :
         winner= board[3]
         return True
     elif board[6] ==board[7] == board[8] and board[6]!="-" :
        winner= board[6]
        return True

def checkvert(board):
    global winner
    if board[0] ==board[3] == board[6] and board[0]!="-" :
        winner= board[0]
        return True
    elif board[1] ==board[4] == board[7] and board[1]!="-" :
         winner= board[1]
         return True
    elif board[2] ==board[8] == board[5] and board[2]!="-" :
        winner= board[2]
        return True

def checkdiag(board):
    global winner
    if board[0] ==board[4] == board[8] and board[0]!="-" :
        winner= board[0]
        return True
    elif board[3] ==board[4] == board[6] and board[3]!="-" :
         winner= board[3]
         return True

def checktie(board):
    if "-"not in board :
        printBoard(board)
        print("c'est une egalite")
        gamerunnig=False

def checkwin():
    if checkdiag(board) or checkhoriz(board) or checkvert(board):
        print("the winner is",winner)
    


#switch the player
def changeplayer():
    global currentpalyer
    if currentpalyer=='X':
        currentpalyer='O'
    else:
        currentpalyer='X'
#ordinateur
def auto(board):
    while currentpalyer=='O':
        a=random.randint(0,8)
        if board[a] =='-':
            board[a]='O'
            changeplayer()







#check for win or tie again

while gamerunning:
    printBoard(board)
    playerinput(board)
    checktie(board)
    checkwin()
    changeplayer()
    auto(board)
    checktie(board)
    checkwin()


