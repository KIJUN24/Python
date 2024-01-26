import pygame
import os
from path import *
from settings import *

class Character(pygame.sprite.Sprite):
    def __init__(self, display):
        super().__init__()
        stage = pygame.image.load(os.path.join(image_path, "stage.png"))
        stage_size = stage.get_rect().size
        stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

        self.character = pygame.image.load(os.path.join(image_path, "character.png"))
        self.character_size = self.character.get_rect().size
        self.character_width = self.character_size[0]
        self.character_height = self.character_size[1]
        self.character_x_pos = (SCREEN_WIDTH/2) - (self.character_width/2)
        self.character_y_pos = SCREEN_HEIGHT - self.character_height - stage_height
        self.character_speed = 5
        self.character_to_x = 0

        self.weapon_size = self.weapon.get_rect().size
        self.weapon_width = self.weapon_size[0]
        self.weapons = []
        self.weapon_speed = 10
        self.weapon_to_remove = -1
        
    def input(self):
        keys = pygame.key.get_pressed()

        # movement
        if keys[pygame.K_LEFT]:
            self.character_to_x -= self.character_speed
        elif keys[pygame.K_RIGHT]:
            self.character_to_x += self.character_speed

        if keys[pygame.K_SPACE]:
            weapon_x_pos = self.character_x_pos + (self.character_width/2) - (self.weapon_width/2)
            weapon_y_pos = self.character_y_pos
            self.weapons.append([weapon_x_pos, weapon_y_pos])

    def screen_draw(self):
        screen.blit(stage, (0, screen_height - stage_height))