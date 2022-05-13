import pygame
import os
from path import *
from settings import *
from weapon import Weapon

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.character = pygame.image.load(os.path.join(image_path, "character.png"))
        self.character_size = self.character.get_rect().size
        self.character_width = self.character_size[0]
        self.character_height = self.character_size[1]
        self.character_x_pos = (SCREEN_WIDTH/2) - (self.character_width/2)
        self.character_y_pos = SCREEN_HEIGHT - self.character_height - stage_height

        self.character_speed = 5
        self.character_to_x = 0
        
    def input(self):
        keys = pygame.key.get_pressed()

        # movement
        if keys[pygame.K_LEFT]:
            self.character_to_x -= self.character_speed
        elif keys[pygame.K_RIGHT]:
            self.character_to_x += self.character_speed

        if keys[pygame.K_SPACE]:
            weapon_x_pos = self.character_x_pos + (self.character_width/2) - (weapon_width/2)
            weapon_y_pos = self.character_y_pos
            self.weapons.append([weapon_x_pos, weapon_y_pos])