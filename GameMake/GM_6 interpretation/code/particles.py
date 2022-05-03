import pygame
from support import import_folder       # spport라는 파일에서 import_folder 함수를 사용하겠다.

class ParticleEffect(pygame.sprite.Sprite):             # pygame안에 sprite안에 Sprite를 사용하겠다.
    def __init__(self, pos, type):                      # 이 class를 사용하기 위해서 pos, type 정보가 필요하다.
        super().__init__()                              # Sprite에 있는 정보들을 모두 사용할 것이다.
        self.frame_index = 0                            # 변수를 사용하기 전 0으로 초기화
        self.animation_speed = 0.5                      # animation_speed를 0.5으로 설정

        if type == 'jump':  # type이 'jump'일 때
            self.frames = import_folder('C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_6\\graphics\\character\\dust_particles\\jump')
            # ('~jump') 폴더 안에 있는 이미지 가져옴.
        if type == 'land':  # type이 'land'일 때
            self.frames = import_folder('C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_6\\graphics\\character\\dust_particles\\land')
            # ('~land') 폴더 안에 있는 이미지 가져옴.

        self.image = self.frames[self.frame_index]      # 
        self.rect = self.image.get_rect(center = pos)   # 이미지의 사각형 영역 반환, 이미지의 센터를 기준으로 pos잡음.
        # get_rect : 이미지의 크기를 가진 직사각형 객체를 가져온다.

    def animate(self):
        self.frame_index += self.animation_speed                # frame_index에 animation_speed를 연속적으로 증가시킴
        if self.frame_index >= len(self.frames):                # frame_index가 frames이 불러온 파일 안에 사진 수보다 크거나 같으면
            self.kill()                                         # frame_index안에 있는 정보를 제거해라 (0으로 돌아간 후 다시 animation_speed를 더한다.)
            # kill() : (정의)스프라이트가 속해있는 모든 그룹에서부터 스프라이트를 제거한다.
        else:
            self.image = self.frames[int(self.frame_index)]     # 이미지에 frames(dir)에 frame_index값(int)의 값을 갖는다.


    
    def update(self, x_shift):                          # 정보를 업데이트 하기 위한 함수
        self.animate()                                  # animate함수를 실행
        self.rect.x += x_shift                          # 사각형의 x값을 x_shift만큼 증가시킨다.
        # rect.x : 개체의 위치(x값)를 업데이트 하기위해 사용.
