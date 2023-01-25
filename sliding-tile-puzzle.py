import random,sys

global board
BLANK = '  '
def main():
    print("Sliding Tile Puzzle.")
    print('''

    Use the WASD keys to move the tiles
    back to their original order as shown.
              1  2  3  4  5
              6  7  8  9 10
             11 12 13 14 15
             16 17 18 19 20
             21 22 23 24   ''')
    input("Press Enter to begin..")
    gameBoard = getNewPuzzle()
    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(gameBoard)
        makeMove(gameBoard, playerMove)

        if gameBoard == getNewBoard():
            print('YOU WON!')
            sys.exit()
        #else:
            #makeRandomMove(board)

def getNewBoard():
    return [['01', '06', '11', '16', '21'], ['02', '07', '12', '17', '22'],
            ['03', '08', '13', '18', '23'], ['04', '09', '14', '19', '24'],
            ['05', '10', '15', '20', BLANK]]
def displayBoard(board):
    labels = [board[0][0], board[1][0], board[2][0], board[3][0],board[4][0],
              board[0][1], board[1][1], board[2][1], board[3][1],board[4][1],
              board[0][2], board[1][2], board[2][2], board[3][2],board[4][2],
              board[0][3], board[1][3], board[2][3], board[3][3],board[4][3],
              board[0][4], board[1][4], board[2][4], board[3][4],board[4][4]]
    boardtoDraw = '''
+------+------+------+------+------+
|      |      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |      |
+------+------+------+------+------+
|      |      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |      |
+------+------+------+------+------+
|      |      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |      |
+------+------+------+------+------+
|      |      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |      |
+------+------+------+------+------+
|      |      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |      |
+------+------+------+------+------+
'''.format(*labels)
    print(boardtoDraw)

def findBlankSpace(board):
    for x in range(5):
        for y in range(5):
            if board[x][y] == '  ':
                return (x, y)

def askForPlayerMove(board):
    blankx,blanky = findBlankSpace(board)
    w = 'W' if blanky != 4 else ' '
    a = 'A' if blankx != 4 else ' '
    s = 'S' if blanky != 0 else ' '
    d = 'D' if blankx != 0 else ' '
    while True:
        print("                            ({})".format(w))
        print("Enter WASD (or QUIT):   ({}) ({}) ({})".format(a,s, d))
        response = input("> ").upper()
        if response == 'QUIT':
            sys.exit()
        if response in (w + a + s + d).replace(' ',''):
            return response


def makeMove(board, move):
    bx, by = findBlankSpace(board)
    if move == 'W':
        board[bx][by], board[bx][by+1] = board[bx][by+1], board[bx][by]
    elif move == 'A':
        board[bx][by], board[bx+1][by] = board[bx+1][by], board[bx][by]
    elif move == 'S':
        board[bx][by], board[bx][by-1] = board[bx][by-1], board[bx][by]
    elif move == 'D':
        board[bx][by], board[bx-1][by] = board[bx-1][by], board[bx][by]

def makeRandomMove(board):
    blankx,blanky = findBlankSpace(board)
    ValidMoves = []
    if blanky != 4:
        ValidMoves.append('W')
    if blankx != 4:
        ValidMoves.append('A')
    if blanky != 0:
        ValidMoves.append('S')
    if blankx != 0:
        ValidMoves.append('D')
    makeMove(board, random.choice(ValidMoves))

def getNewPuzzle(moves = 5):
    board = getNewBoard()
    for i in range(moves):
        makeRandomMove(board)
    return board


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
