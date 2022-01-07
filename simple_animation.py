# Simple Animation with Pygame, Ja' Mauri Williams, 1/07/22, 2:09PM, v0.4

import pygame, sys, time
from pygame.locals import

# Setup Pygame
pygame.init()

# Setup the Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pyagme.display.set_caption('Animation Example!')

# Setup the direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4


# Setup color values.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setup the box data.
b1 = {'rect':pyagme.Rect(300, 80, 50, 100), 'color':RED, 'dir' UPRIGHT}
b2 = {'rect':pyagme.Rect(200, 200, 20, 20), 'color':GREEN, 'dir' UPLEFT}
b3 = {'rect':pyagme.Rect(100, 150, 60, 60), 'color':BLUE, 'dir' DOWNLEFT}
boxes = [b1, b2, b3]