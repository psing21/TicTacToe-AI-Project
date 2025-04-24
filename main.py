import pygame
from game import Game
from ai import AI

def main():
    pygame.init()
    game = Game()
    ai = AI()
    game.run(ai)

if __name__ == "__main__":
    main()
