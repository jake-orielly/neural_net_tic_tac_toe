from tic_tac_toe import create_board, make_move
import random

def new_winnable_board():
    player = 1
    board = create_board()
    status = ''
    while True:
        if status == 'win':
            if player == 1:
                break
            else:
                board = create_board()
        if not True in [0 in i for i in board]:
            board = create_board()
        move = random.randrange(0,10)
        [status, player, board] = make_move(move,player,board)
    y = int(move/3)
    x = move%3
    board[y][x] = 0
    return [board,move]

def flatten_board(board):
    output = []
    for i in board:
        for j in i:
            output.append(j)
    return output

def generate_winnable_boards(num):
    boards = []
    for i in range(num):
        [board, move] = new_winnable_board()
        board = flatten_board(board)
        boards.append([board,move])
    return boards
