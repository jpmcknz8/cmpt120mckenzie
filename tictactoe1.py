# tictactoe1.py

def printRow(row):
    completedRow = "|"
    for marker in row:
        if marker == 0:
            completedRow = completedRow + ("   |")
        if marker == 1:
            completedRow = completedRow + (" X |")
        if marker == 2:
            completedRow = completedRow + (" O |")
    completedRow += ("\n+-----------+")
    print(completedRow)

def printBoard(board):
    print("+-----------+")
    for row in board:
        printRow(row)
def markBoard(board, row, col, player):
    if hasBlanks(board):
        row = int(row)
        col = int(col)
        if player == 1:
            board[col][row] = 1
        elif player == 2:
            board[col][row] = 2
    else:
        print("This space is not empty")
        return(False)
def hasBlanks(board):
    for row in board:
        for col in row:
            if col == 0:
                return(True)
            else:
                continue
        return(False)
def getPlayerMove():
    row,col = input("Enter the row and column separated by a comma of the location you want to play --> ").split(",")
    return (row,col)

def main():
    board = [[0,0,0],[0,0,0],[0,0,0]]
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        row = int(row)
        col = int(col)
        while board[col][row] != 0  or board[col][row] == None:
            print("The space is full, choose a different one")
            row = int(getPlayerMove()[0])
            col = int(getPlayerMove()[1])
        markBoard(board,row,col,player)

        player = player % 2 + 1

main()
 
