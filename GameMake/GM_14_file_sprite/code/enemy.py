import pygame
from random import *
from settings import *

class enemy(pygame.sprite.spreite):
    def __init__(self):
        super().__init__()

        self.enemy_image = pygame.image.load('GameMake/GM_13_study/image_quiz/enemy.png')
        self.enemy = pygame.transform.scale(self.enemy_image, (70,70))
        self.enemy_size = enemy.get_rect().size
        self.enemy_width = self.enemy_size[0]
        self.enemy_height = self.enemy_size[1]
        self.enemy_x_pos = randint(0, SCREEN_WIDTH - self.enemy_width)
        self.enemy_y_pos = 0
        self.enemy_speed = 10