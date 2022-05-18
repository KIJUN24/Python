import pygame
from support import import_folder

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.5
        if type == 'jump':
            self.frames = import_folder('C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_7\\graphics\\character\\dust_particles\\jump')
        if type == 'land':
            self.frames = import_folder('C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_7\\graphics\\character\\dust_particles\\land')
        if type == 'explosion':
            self.frames = import_folder('C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_8_7\\graphics\\enemy\\explosion')
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        # type이 '~'라면 '~~'에 위치한 폴더를 frames에 저장.
        # image에 frames[frame_index] 정보값 저장.
        # rect에 image의 사각형 정보 반환(center를 pos기준으로 잡음.)

    def animate(self):
        self.frame_index += self.animation_speed    # frame_index에 animation_speed를 계속 더해줌
        if self.frame_index >= len(self.frames):    # frame_index가 frames(불러온 해당 파일에 사진 수)보다 크다면
            self.kill() # 초기화시켜라
        else:
            self.image = self.frames[int(self.frame_index)]     # 그렇지 않으면 frame_index를 정수변환해라
    
    def update(self, x_shift):
        self.animate()
        self.rect.x += x_shift  # rect의 x값에 x_shift만큼 더해줌.
