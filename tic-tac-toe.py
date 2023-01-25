import time

ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X,O,BLANK = 'X','O',' '

def main():
    print("Welcome to a game of tic-tac-toe!")
    gameBoard = getBlankBoard()
    currentPlayer, nextPlayer = X, O

    while True:
        print(getBoardStr(gameBoard))
        move = None
        time.sleep(3)
        while not isValidSpace(gameBoard , move):
            print("What is {}\'s move?(1 - 9)".format(currentPlayer))
            move = input('> ')
        UpdateBoard(gameBoard, move, currentPlayer)
        if isWinner(gameBoard, currentPlayer):
            print(getBoardStr(gameBoard))
            print(currentPlayer + " has won the game!")
            break
        elif IsBoardFull(gameBoard):
            print(getBoardStr(gameBoard))
            print("It is a tie!")
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print("Thanks for playing!")



def getBlankBoard():
    #Map of space numbers: 1|2|3
    #                      -+-+-
    #                      4|5|6
    #                      -+-+-
    #                      7|8|9
    # Keys are 1 to 9 and the values are X,O or BLANK
    board ={}
    for space in ALL_SPACES:
        board[space] = BLANK
    return board

def getBoardStr(board):
 # """Return a text-representation of the board."""
    return '''
    {}|{}|{} 1 2 3
    -+-+-
    {}|{}|{} 4 5 6
    -+-+-
    {}|{}|{} 7 8 9'''.format(board['1'], board['2'], board['3'],
    board['4'], board['5'], board['6'],
    board['7'], board['8'], board['9'])





def isValidSpace(board, space):
    return space in ALL_SPACES and board[space] == BLANK

def isWinner(board, player):
    b,p = board,player
    return ((b['1'] == b['2'] == b['3'] == p) or
            (b['4'] == b['5'] == b['6'] == p) or
            (b['7'] == b['8'] == b['9'] == p) or
            (b['1'] == b['4'] == b['7'] == p) or
            (b['2'] == b['5'] == b['8'] == p) or
            (b['3'] == b['6'] == b['9'] == p) or
            (b['1'] == b['5'] == b['9'] == p) or
            (b['3'] == b['5'] == b['7'] == p))

def IsBoardFull(board):
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False
    return True

def UpdateBoard(board, space, mark):
    board[space] = mark

if __name__ == "__main__":
    main()
