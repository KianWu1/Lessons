board=[" ", " ", " ", " ", " ", " ", " ", " ", " "]
isPlaying = True

def printBoard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

def askPlayAgain():
    again = input("Do you want to play again? (y or n)")
    if (again == "y"):
                board=[" ", " ", " ", " ", " ", " ", " ", " ", " "]
                isXsTurn = True
    else:
        isPlaying = False

#checkWin("x")
# toCheck = "x"
# Returns true of parameter has won, returns false if it hasn't won
def checkIfWin(toCheck):
    for i in range(3):
        if board[0+i] == toCheck and board[3+i] == toCheck and board[6+i] == toCheck:
            return True
        if board[0+3*i] == toCheck and board[1+3*i] == toCheck and board[2+3*i] == toCheck:
            return True

    if board[2] == toCheck and board[4] == toCheck and board[6] == toCheck:
            return True
    if board[0] == toCheck and board[4] == toCheck and board[8] == toCheck:
            return True
     # Homework: add loop to check the horizontals
    # Add two more if statements to check diagonals
    return False

print("TicTacToe")
print("Your input will correspond to the square you want to play in")
print("1|2|3")
print("-----")
print("4|5|6")
print("-----")
print("7|8|9")

print()

isXsTurn = True

while isPlaying:
    printBoard()

    if isXsTurn == True:
        location=input("Where do you want to go? (X's Turn): ")
        locationAsInt=int(location)
        if locationAsInt > 0 and locationAsInt < 10 and board[locationAsInt-1] == " ":
            board[locationAsInt-1] = "x"
        else:
            print("There is already something there, fatty or it's an invalid number, fatso")
            continue
    else:
        location=input("Where do you want to go? (O's Turn): ")
        locationAsInt=int(location)
        if locationAsInt > 0 and locationAsInt <10 and board[locationAsInt-1] == " ":
            board[locationAsInt-1] = "o"
        else:
            print("There is already something there, fatty or it's an invalid number, fatso")
            continue
    
    #Check if it is x's tturn and if x has won
    if (isXsTurn and checkIfWin("x")):
        printBoard()
        print ("Congratulations, x won!")
        again = input("Do you want to play again? (y or n)")
        if (again == "y"):
            board=[" ", " ", " ", " ", " ", " ", " ", " ", " "]
            isXsTurn = True
        else:
            break
    #Check if it is o's turn and if o has won
    elif (not isXsTurn and checkIfWin("o")):
        printBoard()
        print ("Congratulations, o won!")
        again = input("Do you want to play again? (y or n)")
        if (again == "y"):
            board=[" ", " ", " ", " ", " ", " ", " ", " ", " "]
            isXsTurn = True
        else:
            break
    else:
        isTie=True
        for spot in board:
            if (spot == " "):
                isTie=False
        if (isTie):
            printBoard()
            print ("It's a tie. No one wins :(")
            again = input("Do you want to play again? (y or n)")
            if (again == "y"):
                board=[" ", " ", " ", " ", " ", " ", " ", " ", " "]
                isXsTurn = True
            else:
                break
        else:
            isXsTurn = not isXsTurn