import pygame
from settings import *

class Player(pygame.sprite.sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('GameMake/GM_14_file_sprite/image/character.png')
        self.character = pygame.transform.scale(self.image, (70,70))
        self.character_size = self.character.get_rect().size
        self.character_width = self.character_size[0]
        self.character_height = self.character_size[1]
        self.character_x_pos = (SCREEN_WIDTH / 2) - (self.character_width / 2)
        self.character_y_pos = SCREEN_HEIGHT - self.character_height
        self.to_x = 0
        self.character_speed = 5

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.to_x -= self.character_speed
        elif keys[pygame.K_RIGHT]:
            self.to_x += self.character_speed
        else:
            self.to_x = 0
    
    def update(self):
        self.input()