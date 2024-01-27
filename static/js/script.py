board = [["", "", ""], ["", "", ""], ["", "", ""]]

currentPlayer = "X"  # X will always start first


def init():
    gameBoard = [[None] * 3 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            cell = {"row": i, "col": j, "value": ""}
    gameBoard[i][j] = cell


def cellClicked(row, col):
    if board[row][col] == "":
        board[row][col] = currentPlayer
        if checkWinner(row, col):
            print(f"{currentPlayer} wins!")
            return


currentPlayer = "O" if currentPlayer == "X" else "X"


def checkWinner(row, col):
    # Check row
    if (
        board[row][0] == currentPlayer
        and board[row][1] == currentPlayer
        and board[row][2] == currentPlayer
    ):
        return True
    # Check column
    if (
        board[0][col] == currentPlayer
        and board[1][col] == currentPlayer
        and board[2][col] == currentPlayer
    ):
        return True
    # Check diagonals
    if (
        row == col
        and board[0][0] == currentPlayer
        and board[1][1] == currentPlayer
        and board[2][2] == currentPlayer
    ):
        return True
    if (
        row + col == 2
        and board[0][2] == currentPlayer
        and board[1][1] == currentPlayer
        and board[2][0] == currentPlayer
    ):
        return True
    return False


init()
