#!/usr/bin/env python3
import pygame
import os
import random as rd
from constants import TAILLE, BLACK, LENGTHWIN

pygame.init()


class Grid:
    def __init__(self, win):
        self.font = pygame.font.Font("ressources/Ubuntu-Bold.ttf", 90)
        self.win = win
        self.tailleWin = LENGTHWIN
        self.taille = TAILLE
        self.grid = [[0] * 9 for i in range(9)]

    def __str__(self):
        os.system("clear")
        return "\n".join([str(i) for i in self.grid])

    def draw(self):
        for x in range(9):
            if x % 3 == 0:
                """Draw the bold lines"""
                start = (x * self.taille, 0)
                end = (x * self.taille, self.tailleWin)
                pygame.draw.line(self.win, BLACK, start, end, 5)

            for y in range(9):
                case = (x * self.taille, y * self.taille, self.taille, self.taille)
                pygame.draw.rect(self.win, BLACK, case, 1)

                if y % 3 == 0:
                    """Draw the bold lines"""
                    start = (0, y * self.taille)
                    end = (self.tailleWin, y * self.taille)
                    pygame.draw.line(self.win, BLACK, start, end, 5)

                self.drawNumber(x, y)

    def caseClique(self, pos):
        y, x = [coord // self.taille for coord in pos]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key < 255 and chr(event.key).isnumeric():
                        self.grid[x][y] = int(chr(event.key))
                        return
                    elif event.key not in [pygame.K_LSHIFT, pygame.K_LCTRL]:
                        return

    def drawNumber(self, x, y):
        if self.grid[y][x] > 0:
            label = self.font.render(str(self.grid[y][x]), 1, BLACK)
            self.win.blit(label, (x * self.taille + self.taille // 4, y * self.taille))
