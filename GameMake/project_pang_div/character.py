import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.character_speed = 5
        self.character_to_x = 0

    def input(self):
        keys = pygame.key.get_pressed()

        # movement
        if keys[pygame.K_LEFT]:
            self.character_to_x -= self.character_speed
        elif keys[pygame.K_RIGHT]:
            self.character_to_x += self.character_speed

        # attack