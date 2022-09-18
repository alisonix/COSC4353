import numpy as np
import pygame
import unittest

from pygame.locals import QUIT

#initialize pygame
pygame.init()

def main():

  running = True
  

  while running:

    pos = pygame.mouse.get_pos()
    pressed1 = pygame.mouse.get_pressed()[0]

    if rectangle.collidepoint(pos) and pressed1:
      #change boolean status to not status
      status = not status
    
    for event in pygame.event.get():
      #quit when x/quit button hit
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    pygame.display.update()
  
def CellTest():

main()
  