def printBoard(toPrint):
    letters = "ABCDEFGHI"
    print("  A B C D E F G H I")
    for x in range(0,len(toPrint)):
        print(letters[x:x+1], end = ' ')
        for y in range(0,len(toPrint[x])):
            print(toPrint[x][y], end ='')
            print(" ", end = '')
        print("")


print("Welcome to Pydoku")
play = True
while play:
    board = [[0]*9]*9
    print(board)
    printBoard(board)
    
    print(board[2], end = "\n\n")
    board[2][7] = 9
    print(board[2], end = "\n\n")
    print(board[1], end = "\n\n")
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
