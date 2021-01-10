import pygame
from constants import LENGTHWIN, WIDTHWIN, WHITE
from grid import Grid

pygame.init()

WIN = pygame.display.set_mode((LENGTHWIN, WIDTHWIN))
clock = pygame.time.Clock()
grid = Grid(WIN)
pygame.display.set_caption("Jeu de Sudoku")


def draw():
    WIN.fill(WHITE)
    grid.draw()
    pygame.display.update()


def main():
    while True:
        clock.tick(60)
        draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_q
            ):
                pygame.quit()
                return 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                grid.caseClique(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    grid.solve()
                if event.key == pygame.K_c:
                    grid.clear()




main()
