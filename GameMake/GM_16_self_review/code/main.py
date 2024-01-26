import pygame, sys
from settings import *
from tile import Tile
from pytmx.util_pygame import load_pygame

class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("made by self")
        self.clock = pygame.time.Clock()

        self.tmx_data = load_pygame('GameMake/GM_16_self_review/data/tmx/basic.tmx')
        self.sprite_group = pygame.sprite.Group()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill("black")
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()