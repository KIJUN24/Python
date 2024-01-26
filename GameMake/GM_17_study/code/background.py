import pygame

class Background:
    def __init__(self, surface):
        self.background = pygame.image.load("GameMake/GM_17_study/image/background.png")
        self.display_surface = surface

    def screen_draw(self):
            self.display_surface.blit(self.background, (0,0))

    def update(self):
        self.screen_draw()