print("Welcome to Tic Tac Toe, a two-player game where one player uses X and the other uses O. The goal is to create a straight line with three marks. The game board is represented by a number boardP, and you simply enter a number to place your mark.")
playerX = "X"
playerO = "O"
listInputX=[]
listInputO=[]
board =[0,1,2,3,4,5,6,7,8]
boxAvailable = board

def printBoard(boardP):
    print( str(boardP[0] )+ ' '+ str(boardP[1] )+ ' '+ str(boardP[2] )+'\n'+ str(boardP[3] )+ ' '+ str(boardP[4] )+ ' '+ str(boardP[5] )+'\n'+ str(boardP[6] )+ ' '+ str(boardP[7] )+ ' '+ str(boardP[8] ))

def handelInput():
    inputValid= False
    while inputValid != True:
        print('Entry number ,available numbers are : ' +str( boxAvailable ))
        inputValue = input()
        print(str(type(inputValue)))
        print(str( inputValue in boxAvailable))
        if inputValue in boxAvailable:
         boxAvailable.remove(inputValid)
         inputValid= True
         return inputValue
        else:
         print("your input d'snot exist in list of available numbers" + str( boxAvailable))
    


printBoard(board)

while len(boxAvailable) != 0:
    handelInput()
    print("pppp"+ str(handelInput()))