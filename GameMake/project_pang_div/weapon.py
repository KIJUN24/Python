import pygame
from path import *

class Weapon:
    def __int__(self):
        self.weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
        self.weapon_size = self.weapon.get_rect().size
        self.weapon_width = self.weapon_size[0]
        self.weapons = []
        self.weapon_speed = 10
        self.weapon_to_remove = -1
