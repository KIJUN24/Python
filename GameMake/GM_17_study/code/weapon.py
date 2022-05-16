import pygame
from player import Player

class Weapon(Player):
    def __init__(self, surface):
        super().__init__(self)
        self.display_surface = surface
        self.weapon = pygame.image.load("GameMake/GM_17_study/image/weapon.png")
        self.weapon_size = self.weapon.get_rect().size
        self.weapon_width = self.weapon_size[0]
        self.weapons = []
        self.weapon_speed = 10
        self.weapon_to_remove = -1

    def input(self):
        keys = pygame.key.get_pressed()

        # self.player_x_pos 값이 변하지 않은 것에 의문...
        if keys[pygame.K_SPACE]:
            # self.weapon_x_pos = self.player_x_pos + (self.player_width/2) - (self.weapon_width/2)
            self.weapon_x_pos = self.player_x_pos + (self.player_width/2) - (self.weapon_width/2)
            self.weapon_y_pos = self.player_y_pos
            self.weapons.append([self.weapon_x_pos, self.weapon_y_pos])
            print("weapon file : ", self.player_x_pos)

    def weapon_pos(self):
        self.weapons = [ [w[0], w[1] - self.weapon_speed] for w in self.weapons ]
        self.weapons = [ [w[0], w[1]] for w in self.weapons if w[1] > 0 ]

    def remove_weaopn(self):
        if self.weapon_to_remove > -1:
            del self.weapons[self.weapon_to_remove]
            self.weapon_to_remove = -1

    def surface_draw(self):
        for weapon_x_pos, weaopn_y_pos in self.weapons:
            self.display_surface.blit(self.weapon, (weapon_x_pos, weaopn_y_pos))
            # print(weapon_x_pos, weaopn_y_pos)

    def update(self):
        self.input()
        self.weapon_pos()
        self.remove_weaopn()
        self.surface_draw()