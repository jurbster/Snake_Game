#Snake Game using pygame

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 0
    w = 0
    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass
    
    def draw(self, surface):
        pass


def drawGrid(w, rows, surface):
    sizeBetween = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBetween
        y = y + sizeBetween

        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))  #drawing down
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y))  #drawing horizontal

    pass


def redrawWindow(surface):
    global width, rows
    surface.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()
    pass


def randomSnack(rows, items):
    pass


def messageBox(subject, content):
    pass


def main():
    global width, rows
    width = 500
    rows = 20       #must be divisible by width
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0), (10,10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)   #ensure game won't run too fast
        clock.tick(10)
        redrawWindow(win)

    pass


main()