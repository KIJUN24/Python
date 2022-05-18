import pygame
from support import import_folder

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):     # 사용하려면 size, x, y값 필요
        super().__init__()
        self.image = pygame.Surface((size, size))   # Surface생성 --> 모든2D객체 --> 색이나 이미지를 가지는 빈 시트
        self.rect = self.image.get_rect(topleft = (x,y))    # rect에 image사각형 반환(topleft 기준 x,y값)

    def update(self, shift):
        self.rect.x += shift

class StaticTile(Tile):
    def __init__(self, size, x, y, surface):    # class 사용하려면 size, x, y, surface 정보 값이 있어야 한다.
        super().__init__(size, x, y)            # Tile class에서 size, x, y값을 불러온다.
        self.image = surface                    # surface를 image에 저장.

class Crate(StaticTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, pygame.image.load('C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_7\\graphics\\terrain\\crate.png').convert_alpha())
        offset_y = y + size # offset_y = y + Tile의 size
        self.rect = self.image.get_rect(bottomleft = (x,offset_y))  # rect는 image의 사각형 반환 값.(bottomleft에 (x, offset_y)를 기준으로 갖는다.)

class AnimatedTile(Tile):
    def __init__(self, size, x, y, path):   # 사용하려면 size, x, y, path값이 필요
        super().__init__(size, x, y)        # Tile의 size, x, y값을 가져옴
        self.frames = import_folder(path)   # frames에 path경로의 파일 정보를 가져옴
        self.frame_index = 0                # frame_index를 0으로 초기화

        self.image = self.frames[self.frame_index]

    def animate(self):
        self.frame_index += 0.15    # frame_index를 0.15만큼 계속 더 해줌.
        if self.frame_index >= len(self.frames):    # frame_index가 frames안에 있는 정보(사진)의 수보다 크면
            self.frame_index = 0                    # frame_iddex값을 0으로 초기화
        self.image = self.frames[int(self.frame_index)]     # image에 frame_index를 정수화 한 frames 값을 저장.

    def update(self, shift):
        self.animate()
        self.rect.x += shift

class Coin(AnimatedTile):   # AnimatedTile class를 불러옴
    def __init__(self, size, x, y, path, value):    # 사용하려면 size, x, y, path, value 값 필요
        super().__init__(size, x, y, path)          # size, x, y, path 값 불러옴
        center_x = x + int(size / 2)                # center_x값 설정
        center_y = y + int(size / 2)                # center_y값 설정
        self.rect = self.image.get_rect(center = (center_x, center_y))  # center를 기준으로 image값 설정.
        self.value = value

class Palm(AnimatedTile):
    def __init__(self, size, x, y, path, offset):
        super().__init__(x, y, size, path)
        offest_y = y - offset
        self.rect.topleft = (x, offest_y)

