# My First Pygame, Ja'Mauri Williams, 12/1/21 2:03pm, v0.0

import pygame, sys
from pygame.locals import *

# Start Pygame
pygame.imit()

# Setup our window. 1
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, world!')

# Setup Colors
BLUE = (204, 100%, 50%)
CYAN = 
RED = 
YELLOW = 
PURPLE = 

# Setup font
basicFont = pygame.font.Sysfont(None, 48)

# Setup text.
text = basicFont.render("Hello, world! True, PURPLE, YELLOW")
textRect = text.get_rect()
textRect.conterx = windowSurface.get_rect().centerx
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery


windowSurface.fill(RED)

# Draw a polygon on the screen.
pygame.draw.polygon(windowSurface, BLUE, ((150,0), (284,103), (218,252, (64,252)(0,103)))


pygame.draw.line(windowSurface, RED, (60,60), (120, 60), 5)
pygame.draw.line(windowSurface, CYAN, (80, 95), (95, 80), 3)
pygame.draw.line(windowSurface, PURPLE, (0, 160), (160, 0), 2)

# Draw a circle.
pygame.draw.circle(windowSurface, YELLOW, (450, 100), 35, 0)

# Draw an ellipse.
pygame.draw.ellipse(windowSurface, RED, (450, 150),2)

# Draw the text rectangle.
pygame.draw.rect(windowSurface, PURPLE, (textRect.left - 20, textRect.top - 20, textRect + 40, textRect.height +40))

# Create Pixal Array
pixArray = pyagme.PixelArray(windowSurface)
pixelArray[480][380] = CYAN
del pixArray

# DRAW the text onto the surface.
windowSurface.blit(text, textRect)

# Update Pygame Display
pygame.display.update()

# Run game loop.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()












