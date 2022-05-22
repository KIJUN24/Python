import py_compile
import pygame

class Player:
    def __init__(self, pos):
        self.image = pygame.image.load("GameMake/GM_test/image/player.png")
        self.rect = self.image.get_rect(topleft = pos)

    def input(self):
        pass