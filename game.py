import pygame
from random_bot import random_move

WIDTH, HEIGHT = 300, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_WIDTH = 6

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic Tac Toe AI")
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_turn = "X"

    def draw_board(self):
        self.screen.fill(WHITE)
        for x in range(1, 3):
            pygame.draw.line(self.screen, BLACK, (x * 100, 0), (x * 100, HEIGHT), LINE_WIDTH)
            pygame.draw.line(self.screen, BLACK, (0, x * 100), (WIDTH, x * 100), LINE_WIDTH)
        for row in range(3):
            for col in range(3):
                mark = self.board[row][col]
                if mark:
                    font = pygame.font.Font(None, 80)
                    text = font.render(mark, True, BLACK)
                    self.screen.blit(text, (col * 100 + 25, row * 100 + 25))
        pygame.display.update()

    def run(self, ai):
        running = True
        while running:
            self.draw_board()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if self.current_turn == "X" and event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row, col = y // 100, x // 100
                    if not self.board[row][col]:
                        self.board[row][col] = "X"
                        self.current_turn = "O"

            if self.current_turn == "O":
                row, col = ai.best_move(self.board)
                if row is not None:
                    self.board[row][col] = "O"
                    self.current_turn = "X"

            if self.check_winner() is not None:
                print("Winner:", self.check_winner())
                pygame.time.delay(2000)
                running = False

    def check_winner(self):
        lines = self.board + list(zip(*self.board)) + [
            [self.board[i][i] for i in range(3)],
            [self.board[i][2 - i] for i in range(3)]
        ]
        for line in lines:
            if line.count(line[0]) == 3 and line[0] != "":
                return line[0]
        if all(cell != "" for row in self.board for cell in row):
            return "Draw"
        return None
