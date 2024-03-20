"""
File: template.py
Author: Sebastian Sanchez
Date: 2024-03-20
Description: Flag of Canada
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Program")

# Define colours from https://www.pygame.org/docs/ref/color_list.html
WHITE = pygame.Color("white")
GREY = pygame.Color("gray67")
RED = pygame.Color("Red")

# Main loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw graphics - BEGIN YOUR PROGRAM HERE
    screen.fill(RED)
    pygame.draw.rect(screen, WHITE, pygame.Rect(250, 0, 300, 400))
    pygame.draw.line(screen, RED, (400, 350), (400, 300), 10)
    pygame.draw.polygon(screen, RED, [(400, 300), (450, 310), (405, 250)])
    pygame.draw.polygon(screen, RED, [(400, 300), (350, 310), (395, 250)])

    pygame.draw.polygon(screen, RED, [(435, 290), (500, 225), (405, 250)])
    pygame.draw.polygon(screen, RED, [(365, 290), (300, 225), (405, 250)])

    pygame.draw.polygon(screen, RED, [(425, 275), (500, 190), (400, 240)])
    pygame.draw.polygon(screen, RED, [(375, 275), (300, 190), (400, 240)])

    pygame.draw.polygon(screen, RED, [(410, 265), (475, 170), (390, 230)])
    pygame.draw.polygon(screen, RED, [(390, 265), (325, 170), (410, 230)])

    pygame.draw.polygon(screen, RED, [(400, 120), (370, 300), (430, 300)])

    # Update display
    pygame.display.flip()

# Quit Pygame   
pygame.quit()
sys.exit()
