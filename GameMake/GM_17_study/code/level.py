import pygame
from settings import *
from player import Player

class Level:
    def __init__(self, surface):
        self.display_surface = surface

        self.background = pygame.image.load("GameMake/GM_17_study/image/background.png")

        self.stage = pygame.image.load("GameMake/GM_17_study/image/stage.png")
        self.stage_size = self.stage.get_rect().size
        self.stage_height = self.stage_size[1]

    def screen_draw(self):
        self.display_surface.blit(self.background, (0,0))
        self.display_surface.blit(self.stage, (0, SCREEN_HEIGHT - self.stage_height))

    def update(self):
        self.screen_draw()