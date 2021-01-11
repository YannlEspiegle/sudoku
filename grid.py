import pygame
import time
import numpy as np
from constants import TAILLE, BLACK, GREY, LENGTHWIN, WHITE


class Grid:
    def __init__(self, win):
        self.font = pygame.font.Font("ressources/Ubuntu-Bold.ttf", 90)
        self.win = win
        self.tailleWin = LENGTHWIN
        self.taille = TAILLE
        self.grid = np.zeros((9, 9), int)
        self.solved = False
        self.wait = False

    def __str__(self):
        return str(self.grid)

    def draw(self):
        for x in range(9):
            if x % 3 == 0:
                """Draw the bold lines"""
                start = (x * self.taille, 0)
                end = (x * self.taille, self.tailleWin)
                pygame.draw.line(self.win, BLACK, start, end, 5)

            for y in range(9):
                self.drawNumber(x, y)

                case = (x * self.taille, y * self.taille, self.taille, self.taille)
                pygame.draw.rect(self.win, BLACK, case, 1)

                if y % 3 == 0:
                    """Draw the bold lines"""
                    start = (0, y * self.taille)
                    end = (self.tailleWin, y * self.taille)
                    pygame.draw.line(self.win, BLACK, start, end, 5)


    def caseClique(self, pos):
        x, y = [coord // self.taille for coord in pos]

        # make the grey thing (cf. drawNumber())
        self.drawGrey(x,y)
        self.draw()
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # < 255, otherwise, it crashes
                    if event.key < 255 and chr(event.key).isnumeric():
                        self.grid[y, x] = int(chr(event.key))
                        return

                    # pygame starts by 1 and finish by 0
                    if pygame.K_KP1 <= event.key < pygame.K_KP0:
                        self.grid[y, x] = event.key - pygame.K_KP1 + 1   # simulates KP0
                        return

                    elif event.key not in [pygame.K_LSHIFT, pygame.K_LCTRL]:
                        self.grid[y, x] = 0
                        return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.grid[y, x] = 0
                    return

    def drawNumber(self, x, y):
        if self.grid[y][x] > 0:
            label = self.font.render(str(self.grid[y][x]), 1, BLACK)
            self.win.blit(label, (x * self.taille + self.taille // 4, y * self.taille))

    def drawGrey(self, x, y):
        case = (x * self.taille, y * self.taille, self.taille, self.taille)
        pygame.draw.rect(self.win, GREY, case)

    def column(self, col):
        """ return a list of the column """
        return [self.grid[i, col]for i in range(9)]

    def square(self, line, col):
        """ return the 3x3 square of coordonates"""
        prevLine = line - line % 3
        prevCol = col - col % 3
        return self.grid[prevLine:prevLine+3, prevCol:prevCol+3]

    def isplacable(self, line, col, x):
        """ check if the value X is placable in the coord line col"""
        if x not in self.grid[line] and x not in self.column(col) and x not in self.square(line, col):
            return True
        return False

    def __solve(self):
        """ the actual fonction to solve """

        for y in range(9):
            for x in range(9):
                if self.grid[y, x] == 0:
                    for n in range(1, 10):
                        if self.isplacable(y, x, n):
                            self.grid[y, x] = n

                            if self.wait:
                                self.win.fill(WHITE)
                                self.draw()
                                pygame.display.update()
                                time.sleep(0.01)

                            self.__solve()
                            if not self.solved:
                                self.grid[y, x] = 0
                    # if we arrive here, it means that we couldn't place any of the nine numbers
                    # so we go back one step in recursion
                    return

        print("finished solving")
        if not self.solved:
            self.solved = True

    def solve(self):
        self.solved = False
        self.__solve()

    def solve_wait(self):
        self.solved = False
        self.wait = True
        self.__solve()
        self.wait = False

    def clear(self):
        self.grid = np.zeros_like(self.grid)
        self.solved = False
