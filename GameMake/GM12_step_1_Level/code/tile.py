import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('GameMake/GM12_step_1_Level/graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)