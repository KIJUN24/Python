# 물고기 공격 고래, 잠수함 피하기
# 물고기 : <a href="https://kr.lovepik.com/images/png-foam.html">거품 Png vectors by Lovepik.com</a>

import pygame
import time

pygame.init()

size = [1300, 800]
screen = pygame.display.set_mode(size)

title = "self make game"
pygame.display.set_caption(title)

clock = pygame.time.Clock()

blue = (80, 188, 223)

class object:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0

    def put_image(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
        self.sx, self.sy = self.img.get_size() # sx ; spaceship_x, sy = spaceship_y

    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()

    def show(self):
        screen.blit(self.img, (self.x, self.y))


cf = object()
cf.put_image("C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_5\\control_fish.png")
cf.change_size(80, 85)
# cf.x = round(size[0] * 1/2) - round(cf.sx * 1/2)
cf.x = round(cf.sx * 1/2) + 30
cf.y = round(size[1] * 1/2 - cf.sy)
cf.move = 5


SB = 0
while SB == 0:
    clock.tick(60)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SB = 1

        print(event)

    screen.fill(blue)

    cf.show()

    pygame.display.flip()
pygame.quit()