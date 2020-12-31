from random import randint
from math import floor,ceil

Alpha = { "A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G": 6, "H" : 7, "I": 8}
board = { (i,j):0 for i in range(9) for j in range(9) }

def genBoard():
    outBoard = {(i,j):0 for i in range(9) for j in range(9)}
    for i in range(9):
        noX = []
        noY = []
        noCell =[]
        for ii in range(9):
            x = randint(0,8)
            y = randint(0,8)
            cell = (int((x-1) / 3 + 1) + (int((y-1))/ 3) * 3)
            if not (x in noX or y in noY or cell in noCell):
                noX.append(x)
                noY.append(y)
                noCell.append(cell)
                outBoard[x,y] = i
    return outBoard

def printBoard(toPrint):
    letters = "ABCDEFGHI"
    print("  A B C D E F G H I")
    for x in range(9):
        print(letters[x:x+1], end = ' ')
        for y in range(9):
            print(toPrint[x,y], end ='')
            print(" ", end = '')
        print("")

def checkboard(x,y,val, refBoard):
    if refBoard[x,y] == val:
        return True
    else:
        return False

print("Welcome to Pydoku")
play = True
while play:
    correctBoard = genBoard()
    playerBoard = { (i,j):0 for i in range(9) for j in range(9) }
    print('Correct Board: \n')
    printBoard(correctBoard)
    print('\nPlayer Board: \n')
    printBoard(playerBoard)
    prompt = True
    while prompt:
        playAgain = input("Would you like to play again? ")
        playAgain = playAgain.lower()
        if playAgain == "yes" or playAgain == "y":
            prompt = False
        elif not playAgain or playAgain == "no" or playAgain == "n":
            prompt = False
            play = False
