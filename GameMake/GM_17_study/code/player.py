import pygame
from settings import *
from stage import Stage

class Player(Stage):
    def __init__(self, surface):
        # Stage information
        super().__init__(self)
        # surface(sreen) draw
        self.display_surface = surface
        # general
        self.player = pygame.image.load("GameMake/GM_17_study/image/player.png")
        self.player_size = self.player.get_rect().size
        self.player_width = self.player_size[0]
        self.player_height = self.player_size[1]
        self.player_x_pos = (SCREEN_WIDTH/2) - (self.player_width/2)
        self.player_y_pos = SCREEN_HEIGHT - self.player_height - self.stage_height
        self.player_to_x = 0
        self.player_speed = 5

        # player rect information update
        self.player_rect = self.player.get_rect()
        self.player_rect.left = self.player_x_pos
        self.player_rect.top = self.player_y_pos

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.player_to_x = self.player_speed
            # print(self.player_to_x, "right")
            print("player file : ",  self.player_x_pos)
        elif keys[pygame.K_LEFT]:
            self.player_to_x = -self.player_speed
            # print(self.player_to_x, "left")
            print("player file : ", self.player_x_pos)
        else:
            self.player_to_x = 0

        self.player_x_pos += self.player_to_x
        # print(self.player_x_pos)

        if self.player_x_pos < 0:
            self.player_x_pos = 0
        elif self.player_x_pos > SCREEN_WIDTH - self.player_width:
            self.player_x_pos = SCREEN_WIDTH - self.player_width

    def surface_draw(self):
        self.display_surface.blit(self.player, (self.player_x_pos, self.player_y_pos))

    def update(self):
        self.surface_draw()
        self.input()