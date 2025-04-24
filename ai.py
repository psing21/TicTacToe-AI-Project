import math

class AI:
    def best_move(self, board):
        best_score = -math.inf
        move = (None, None)
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "O"
                    score = self.minimax(board, 0, False, -math.inf, math.inf)
                    board[i][j] = ""
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    def minimax(self, board, depth, is_max, alpha, beta):
        winner = self.check_winner(board)
        if winner == "O":
            return 1
        elif winner == "X":
            return -1
        elif winner == "Draw":
            return 0

        if is_max:
            max_eval = -math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "O"
                        eval = self.minimax(board, depth + 1, False, alpha, beta)
                        board[i][j] = ""
                        max_eval = max(max_eval, eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = math.inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "X"
                        eval = self.minimax(board, depth + 1, True, alpha, beta)
                        board[i][j] = ""
                        min_eval = min(min_eval, eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval

    def check_winner(self, board):
        lines = board + list(zip(*board)) + [
            [board[i][i] for i in range(3)],
            [board[i][2 - i] for i in range(3)]
        ]
        for line in lines:
            if line.count(line[0]) == 3 and line[0] != "":
                return line[0]
        if all(cell != "" for row in board for cell in row):
            return "Draw"
        return None
