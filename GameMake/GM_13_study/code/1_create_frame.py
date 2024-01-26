import pygame

pygame.init()   # 초기화 (반드시 필요)

# 화면 크키 설정
SCREEN_WIDTH = 480  # 가로 크기
SCREEN_HEIGNT = 640 # 세로 크기
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGNT))

# 화면 타이틀 설정
pygame.display.set_caption("Study")

# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

# pygame 종료
pygame.quit()