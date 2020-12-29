def printBoard(toPrint):
    letters = "ABCDEFGHI"
    print("  A B C D E F G H I")
    for x in range(9):
        print(letters[x:x+1], end = ' ')
        for y in range(9):
            print(toPrint[x,y], end ='')
            print(" ", end = '')
        print("")


print("Welcome to Pydoku")
play = True
while play:
    board = { (i,j):0 for i in range(9) for j in range(9) }
    print(board)
    printBoard(board)
    



    prompt = True
    while prompt:
        playAgain = input("Would you like to play again? ")
        playAgain = playAgain.lower()
        if playAgain == "yes" or playAgain == "y":
            prompt = False
        elif not playAgain or playAgain == "no" or playAgain == "n":
            prompt = False
            play = False
