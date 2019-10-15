board = []
for _ in range(3):
    board.append(['']*3)

def make_move(num,player):
    if num < 0 or num > 8:
        return ['error', player]
    y = int(num/3)
    x = num%3
    if board[y][x] != '':
        return ['error', player]
    board[y][x] = player

    if len(set(board[y])) == 1 or \
        len(set([row[x] for row in board])) == 1 or \
        set([board[0][0],board[1][1],board[2][2]]) == {player} or \
        set([board[0][2],board[1][1],board[2][0]]) == {player}:
        return ['win',player]

    player = 'X' if player == 'O' else 'O'
    return ['success', player]

player = 'X'
for i in range(5):
    moves = [2,1,4,5,6]
    [status, player] = make_move(moves[i],player)
    print(status)
    #print(board)