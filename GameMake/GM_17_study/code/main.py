import pygame, sys
from player import Player
from weapon import Weapon
from settings import *
from level import Level

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Self Study")

clock = pygame.time.Clock()
level = Level(screen)
player = Player(screen)
weapon = Weapon(screen)
running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    level.update()
    # player.update()
    # weapon.update()

    pygame.display.update()