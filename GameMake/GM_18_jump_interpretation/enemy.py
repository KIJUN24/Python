import pygame
from tiles import AnimatedTile
from random import randint

class Enemy(AnimatedTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, 'C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_7\\graphics\\enemy\\run')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = randint(3, 5) # enemy의 speed를 3~5로 랜덤하게 지정

    def move(self):
        self.rect.x += self.speed

    def reverse_image(self):
        if self.speed > 0:  # speed가 0보다 크다면
            self.image = pygame.transform.flip(self.image, True, False)     # 사진을 x축 기준으로 반전시킨다.

    def reverse(self):
        self.speed *= -1    # speed에 -1를 곱해준다.

    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverse_image()