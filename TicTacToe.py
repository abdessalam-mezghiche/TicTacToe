import random

print("Welcome to Tic Tac Toe, a two-player game where one player uses X and the other uses O. The goal is to create a straight line with three marks. The game board is represented by a number boardP, and you simply enter a number to place your mark.")
playerX = "❌"
playerO = "⭕"
listInputX=[]
listInputO=[]
board =['1️⃣ ','2️⃣ ','3️⃣ ','4️⃣ ','5️⃣ ','6️⃣ ','7️⃣ ','8️⃣ ','9️⃣ ']
boxAvailable=[1,2,3,4,5,6,7,8,9]
playerRol = random.choices([playerX,playerO])

def printBoard(boardP):
    print( boardP[0]+ ' '+ boardP[1]+ ' '+ boardP[2]+'\n'+ boardP[3]+ ' '+ boardP[4]+ ' '+ boardP[5]+'\n'+ boardP[6]+ ' '+ boardP[7]+ ' '+ boardP[8])

def handelInput(player):
    validInput= False
    while not validInput:
        print()
        inputV =input('Player '+player+' role: Enter a number within the scope of the list ' +str( boxAvailable )+':')
        if (inputV.isdigit()) :
            inputValue=int(inputV)
            if(inputValue in boxAvailable):
                boxAvailable.remove(inputValue)
                board[inputValue-1] = player
                if player== playerO:
                    listInputO.append(inputValue)
                else:
                    listInputX.append(inputValue)
                validInput= True
                continue
            else:
                print(" ⚠️ Error: Input is not within the scope of the list" + str( boxAvailable))
        else:
            print(" ⚠️ Error: Input is not a number")
    else:
       printBoard(board)
       return inputValue

def testWin(listInput):
    win = False
    if len(listInput)!=0:
     listWin =[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
     for list in listWin:
         if all(value in listInput for value in list):
          win= True
          continue
    return win

printBoard(board)
while (len(boxAvailable) != 0) and(not testWin(listInputO) and (not testWin(listInputX))):
    if(playerRol == playerO ):
       playerRol = playerX
    else:
       playerRol = playerO
       
    handelInput(playerRol)
    
else:
   if testWin(listInputO):
      print('Congratulations player '+playerO+' won 👏')
   elif testWin(listInputX):
      print('Congratulations player '+playerX+' won 👏')
   else:
      print('GAME OVER NO WINNER')