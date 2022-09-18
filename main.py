import pygame, sys
import numpy as np
from pygame.locals import QUIT

#Initialize
pygame.init()

#Create Window
WIDTH = 400
HEIGHT = 300
ROWS = 20
PIXEL_WIDTH = (WIDTH / ROWS)
PIXEL_HEIGHT = (HEIGHT / ROWS)
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))

#Create array
a = np.random.rand(ROWS, ROWS)


def draw(width, cell_height, cell_width, surface, rows):
    x = 0
    y = 0
    j = 0
    k = 0

    for i in range(rows):
        x += cell_width
        y += cell_height

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))

        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))
        #print(a[j][k])


#        if (a[j, k] > 0.5):
#            surf = pygame.Surface((WIDTH / ROWS, HEIGHT / ROWS))
#            surf.fill((255, 255, 255))
#            DISPLAYSURF.blit(surf, (x, y))

    for j in range(ROWS):
        for k in range(ROWS):
            if (a[j, k] > 0.8):
                surf = pygame.Surface((cell_width, cell_height))
                surf.fill((255, 255, 255))
                DISPLAYSURF.blit(surf, ((j * cell_width), (k * cell_height)))


def main():

    while True:

        draw(WIDTH, HEIGHT / ROWS, WIDTH / ROWS, DISPLAYSURF, ROWS)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()
