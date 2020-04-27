import pygame
import numpy as np 

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

bg = 25, 25, 25
screen.fill(bg)

nxC, nyC = 25, 25

dimCW = width / nxC 
dimCH = height / nyC

while True:

    for y in range(0, nxC):
        for x in range(0, nyC):

            poly: [((x)     * dimCW,    y)]
    pass