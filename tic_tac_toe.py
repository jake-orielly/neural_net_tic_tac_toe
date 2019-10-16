def create_board():
    board = []
    for _ in range(3):
        board.append([0]*3)
    return board

def make_move(num,player,board):
    if num < 0 or num > 8:
        return ['error', player, board]
    y = int(num/3)
    x = num%3
    if board[y][x] != 0:
        return ['error', player, board]
    board[y][x] = player

    if len(set(board[y])) == 1 or \
        len(set([row[x] for row in board])) == 1 or \
        set([board[0][0],board[1][1],board[2][2]]) == {player} or \
        set([board[0][2],board[1][1],board[2][0]]) == {player}:
        return ['win',player, board]

    player = 1 if player == -1 else -1
    return ['success', player, board]