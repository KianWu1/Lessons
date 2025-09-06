import os

board = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]

currPlayer = 1

def drawBoard():
    print(" 1 2 3 4 5 6 7")
    
    for row in board:
        for item in row:
            # print(item, " ", end="")
            if item == 0:
                print("⬛", end = "")
            elif item == 1:
                print ("🔴", end = "")
            else:
                print("🔵", end = "")
        print()

def addPiece(location, currPlayer):
    for i in range(6):
        if board [5-i][location -1] == 0:
            board[5-i][location -1] = currPlayer
            break

def checkWin(currPlayer):
    #Vertically
    for j in range(7):
        for i in range(3):
            if currPlayer == board[i][j] and currPlayer == board[1+i][j] and currPlayer == board[2+i][j] and currPlayer == board[3+i][j]:
                return True

    #Horizontally
   
    for i in range(6):
        for j in range(4):
            if currPlayer == board[i][j] and currPlayer == board[i][1+j] and currPlayer == board [i][2+j] and currPlayer == board [i][3+j]:
                return True

    #Diagonally down rightt
    for i in range(3):
        for j in range(4):
            if board[i][j] == currPlayer and board[1+i][1+j] == currPlayer and board[2+i][2+j] == currPlayer and board[3+i][3+j] == currPlayer:
                return True

    #Diagonally down left
    for i in range(3):
        for j in range(4):
            if board[i][3+j] == currPlayer and board[1+i][2+j] == currPlayer and board[2+i][1+j] == currPlayer and board[3+i][j] == currPlayer:
                return True

    
#\ is tthe escape key from a string to run a command. \n prints a new line character.
os.system("cls")
keepPlaying = True
while keepPlaying:
    while True:
        drawBoard()
        if currPlayer == 1:
            print("\nIt is 🔴's turn.")
        else:
            print("\nIt is 🔵's turn.")
        location=input("Where would you like to go? ")
        addPiece(int(location), currPlayer)
        os.system("cls")

        if checkWin(currPlayer):
            if currPlayer == 1:
                os.system("cls")
                print("Red has won!")
            else:
                print ("Blue has won!")
            print()
            drawBoard()
            playAgain = input("Would you like to play again?: ")
            if playAgain[0].lower() != "y":
                keepPlaying = False
                print()
                print("Thank you for playing!")
            break

        
    #Change player's tturn
        currPlayer = currPlayer*-1

        os.system("cls")
    
    board = [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
    currPlayer = 1

    os.system("cls")

# Instead of printing out the literal number from the board,
# use if statements to print out a red, blue emoji 🔴 🔵 ⬛

#New HW: Each time you add a piece, it changes color to the next player's color

#New NEW HW Add play again function after someone wins

#NEW NEW HW