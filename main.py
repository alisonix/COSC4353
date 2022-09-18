import pygame, sys
import numpy as np
from pygame.locals import QUIT

#Initialize
pygame.init()

#Create Window
WIDTH = 400
HEIGHT = 300
ROWS = 20
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))

#Create random array
randomArray = np.random.rand(ROWS, ROWS)

#Function to draw on the screen
def draw(width, cell_height, cell_width, surface, rows):
  xCoordinate = 0
  yCoordinate = 0

  #for loop to draw the grid
  for i in range(rows):
    xCoordinate += cell_width
    yCoordinate += cell_height

    pygame.draw.line(surface, (255, 255, 255), (xCoordinate, 0), (xCoordinate, width))

    pygame.draw.line(surface, (255, 255, 255), (0, yCoordinate), (width, yCoordinate))

  #for loop to iterate through the nd array
  for j in range(ROWS):
        for k in range(ROWS):
          #If the value of the random array is more than 0.8, draw a cell in those coordinates
            if (randomArray[j, k] > 0.8):
                surf = pygame.Surface((cell_width, cell_height))
                surf.fill((255, 255, 255))
                DISPLAYSURF.blit(surf, ((j * cell_width), (k * cell_height)))

#main function
def main():
  while True:
    draw(WIDTH, HEIGHT / ROWS, WIDTH / ROWS, DISPLAYSURF, ROWS)

    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    pygame.display.update()

if __name__ == "__main__":
  main()
