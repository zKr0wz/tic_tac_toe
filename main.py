import pygame
import sys
from config import *
from game import Game
from graphics import draw_lines, draw_figures

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)
draw_lines(screen)

game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
            x, y = event.pos
            row = y // SQUARE_SIZE
            col = x // SQUARE_SIZE
            result = game.mark_square(row, col)
            if result:
                print(result)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            game.reset()
            screen.fill(BG_COLOR)
            draw_lines(screen)

    draw_figures(screen, game)
    pygame.display.update()

