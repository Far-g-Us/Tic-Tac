from django.shortcuts import render
from django.http import HttpResponse


board = [['', '', ''], ['', '', ''], ['', '', '']]
currentPlayer = 'X'


def init():
    gameBoard = [[None] * 3 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            cell = {'row': i, 'col': j, 'value': ''}
            gameBoard[i][j] = cell
    return gameBoard


def cell_clicked(request, row, col):
    game_board = request.session.get('board', init())
    currentPlayer = request.session.get('currentPlayer', 'X')

    if game_board[row][col]['value'] == '':
        game_board[row][col]['value'] = currentPlayer
        if check_winner(game_board, row, col):
            return HttpResponse(f'{currentPlayer} wins!')
        currentPlayer = 'O' if currentPlayer == 'X' else 'X'

    request.session['board'] = game_board
    request.session['currentPlayer'] = currentPlayer
    
    return render(request, 'game_board.html', {'board': game_board})


def check_winner(game_board, row, col):
    currentPlayer = game_board[row][col]['value']
    if (
        game_board[row][0]['value'] == currentPlayer
        and game_board[row][1]['value'] == currentPlayer
        and game_board[row][2]['value'] == currentPlayer
    ):
        return True
    if (
        game_board[0][col]['value'] == currentPlayer
        and game_board[1][col]['value'] == currentPlayer
        and game_board[2][col]['value'] == currentPlayer
    ):
        return True
    if (
        row == col
        and game_board[0][0]['value'] == currentPlayer
        and game_board[1][1]['value'] == currentPlayer
        and game_board[2][2]['value'] == currentPlayer
    ):
        return True
    if (
        row + col == 2
        and game_board[0][2]['value'] == currentPlayer
        and game_board[1][1]['value'] == currentPlayer
        and game_board[2][0]['value'] == currentPlayer
    ):
        return True
    return False


def game_board(request):
    game_board = init()
    request.session['board'] = game_board
    request.session['currentPlayer'] = 'X'
    return render(request, 'game_board.html', {'board': game_board})


def game_view(request):
    board = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    
    context = {
        'board': board
    }

    return render(request, 'game.html', context)