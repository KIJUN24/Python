import pygame, sys
import os
from settings import *


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Pang Div File")

clock = pygame.time.Clock()

running = True

while running:
    dt = clock.tick(FPS)

    