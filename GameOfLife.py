import pygame
import numpy as np 

pygame.init()

width, height = 100, 100
screen = pygame.display.set_mode((height, width))

bg = 25, 25, 25
screen.fill(bg)

nxC, nyC = 25, 25

dimCW = width / nxC 
dimCH = height / nyC

gameState = np.zeros((nxC, nyC))

gameState[5,3] = 1
gameState[5,4] = 1
while True:

    for y in range(0, nxC):
        for x in range(0, nyC):

            n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x) % nxC, (y - 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x - 1) % nxC, (y) % nyC] + \
                      gameState[(x + 1) % nxC, (y) % nyC] + \
                      gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                      gameState[(x) % nxC, (y + 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y + 1) % nyC] 
            
            if gameState[x, y] == 0 and n_neigh == 3:
                gameState[x, y] = 1
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh >3):
                gameState[x, y] = 0
            
            poly: [((x)   * dimCW, y * dimCH),
                   ((x+1) * dimCW, y * dimCH),
                   ((x+1) * dimCW, (y+1) * dimCH),
                   ((x)   * dimCW, (y+1) * dimCH)]
            
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
            pygame.draw.polygon(screen,(128,128,128), poly,1)
    