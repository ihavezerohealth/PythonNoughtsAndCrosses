import time

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

class Player():
    def __init__(self, marker):
        self.marker = marker
        self.score = 0

    def makeMove(self, indexX, indexY):
        position = board[indexX][indexY]
        if position == 0:
            board[indexX][indexY] = self.marker
        elif position == self.marker:
            print("You can't make that move, it's already taken by you!")
        else:
            print("The opposing player has already taken this spot!")

def fetchIndex():
    global indexX; global indexY
    try:
        indexX = int(input("Which row would you like to move on?\n"))
        indexY = int(input("Which column would you like to move on?\n"))
    except Exception:
        print("You must enter an integer!")
        return -1
    indexX -= 1
    indexY -= 1
    if indexX > 2 or indexY > 2:
        print("That's not on the board!")
        return -1
    elif indexX < 0 or indexY < 0:
        print("That's not on the board!")
        return -1

def printBoard():
    for i in range(3):
        print(board[i])

def checkForWin():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return True
        elif board[0][i] == board[1][i] == board[2][i] != 0:
            return True
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return True
    elif board[2][0] == board[1][1] == board[0][2] != 0:
        return True
    else:
        return False

def printRules():
    print("""
        Rules of the game:
        1. You can only make a move on an empty space.
        2. Indexing starts at 1, not 0. eg. Row 1, Column 1 is the top left corner.
        3. You must take it in turns to make a move.
    """)

def checkIfBoardIsFull():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True

def scoreBoard():
    time.sleep(1)
    print("Player 1: " + str(Players[0].score))
    print("Player 2: " + str(Players[1].score))
    time.sleep(1)
        
def main(amountOfTimesToPlay):
    Player1 = Player("X")
    Player2 = Player("O")
    Players = [Player1, Player2]
    for i in range(amountOfTimesToPlay):
        win = False
        while not win:
            for i in range(2):
                printBoard()
                print("Player " + str(i + 1) + "'s turn!")
                time.sleep(0.3)
                results = fetchIndex()
                if results == -1:
                    results = fetchIndex()
                    if results == -1:
                        return print("Stop messing around!")
                Players[i].makeMove(indexX, indexY)
                print("Finished Move!")
                time.sleep(0.5)
                win = checkForWin() 
                if win:
                    break
        printBoard()
        time.sleep(1)
        print(f"Player {Players[i].marker} wins!")
        Players[i].score += 1
        scoreBoard()

if __name__ == "__main__":
    shouldPrintRules = input("Would you like to see the rules? [Y]es or [N]o?\n")
    if shouldPrintRules.lower() == "y":
        printRules()
    try:
        amountOfTimesToPlay = int(input("How many times would you like to play?\n"))
    except Exception:
        print("You must enter an integer!")
        exit()
    main(1)