# Simple Animation with Pygame, Ja' Mauri Williams, 1/07/22, 1:40PM, v0.1

import pygame, sys, time
from pygame.locals import

# Setup Pygame
pygame.init()

# Setup the Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pyagme.display.set_caption('Animation Example!')
