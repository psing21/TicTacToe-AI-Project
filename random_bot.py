import random

def random_move(board):
    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
    return random.choice(empty) if empty else (None, None)
