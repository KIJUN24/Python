# study : https://www.youtube.com/watch?v=YWN8GcmJ-jA&t=2531s

import pygame, sys          # pygame을 위한 import. 모듈 에러를 없애기 위해 sys import(자신이 만든 모듈을 불러와 사용하기 위해)
from settings import *      # settings라는 파일에 있는 정보를 가져와서 쓴다.
from level import Level     # level이라는 파일에서 Level이라는 class 정보를 사용할 것이다.

# Pygame setup
pygame.init()                                                       # pygame을 실행할 때 처음으로 작성해줘야 함.
screen = pygame.display.set_mode((screen_width, screen_height))     # 게임창의 사이즈 조절 (settings에서 작성한 정보를 사용)
clock = pygame.time.Clock()                                         # import한 Level class를 사용.
level = Level(level_map, screen)

while True:                             # while문이 계속 돌아가게끔 설정
    for event in pygame.event.get():    # for문으로 event설정.(pygame의 event를 get()함수를 통해 정보를 가져옴)
        if event.type == pygame.QUIT:   # if문 : get()으로 받아온 정보인 event의 type이 pygame.QUIT일 때 -> pygame의 창을 닫을 때
            pygame.quit()               # pygame을 종료시켜라
            sys.exit()                  # 강제로 스크립트 종료

    screen.fill('black')                # 배경은 검정으로 채워라
    level.run()                         # class Level 안에 있는 함수인 run()을 while문에 종료할 때까지 계속 돌려라.

    pygame.display.update()             # pygame의 화면을 계속 업데이트해라
    clock.tick(60)                      # 초당 60번 -> FPS = 60