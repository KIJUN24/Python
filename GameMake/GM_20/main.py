import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 400))    # 화면 크기 세팅 set_mode((w,h)) -> 튜플형태
pygame.display.set_caption("Runner")    # 게임 실행 시 이름 설정
Colck = pygame.time.Clock()
test_font = pygame.font.Font('GameMake/GM_20/font/Pixeltype.ttf', 50)   # 폰드 정의 (폰트, 글자 크기)

sky_surface = pygame.image.load('GameMake/GM_20/graphics/Sky.png').convert()    # 사진
ground_surface = pygame.image.load('GameMake/GM_20/graphics/ground.png').convert()  # 사진

# text_surf = test_font.render('My Game', False, 'Black')  # 화면 상 글자 넣기
score_surf = test_font.render('My Game', False, (64,64,64))  # 화면 상 글자 넣기
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('GameMake/GM_20/graphics/snail/snail1.png').convert_alpha()  
snail_rect = snail_surf.get_rect(bottomright = (600, 300))  # snail_surf의 사진 사각형 -> (bottomright를 기준)

player_surf = pygame.image.load('GameMake/GM_20/graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))    # player_surf의 사진 사각형 -> (midbottom를 기준)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 게임 끄기 위함
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEMOTION:  # 마우스가 움직일 때
        #     print(event.pos)
        # if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 클릭할 때
        #     print("MOUSE DOWN")
        # if event.type == pygame.MOUSEBUTTONUP:    # 마우스 클릭하고 땔 때
        #     print("MOUSE UP")

        if event.type == pygame.MOUSEMOTION:
            if (player_rect.collidepoint(event.pos)):   # 마우스가 player_rect와 충돌한다면
                print("collision")

        if event.type == pygame.KEYDOWN:    # 키보드를 누를 때
            if event.key == pygame.K_ESCAPE:    # ESC를 누를 때
                pygame.quit()   # pygame을 꺼라
                sys.exit()      # pygame을 끌 때 에러 방지

    screen.blit(sky_surface, (0,0))         # pygame 화면 상에 그리기
    screen.blit(ground_surface, (0,300))    # pygame 화면 상에 그리기
    pygame.draw.rect(screen, "Pink", score_rect)
    pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
    # pygame.draw.line(screen, "Gold", (0,0), pygame.mouse.get_pos(), 10)
    # pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50,200,100,100))

    screen.blit(score_surf, score_rect)    # pygame 화면 상에 그리기
    snail_rect.x -= 3   # snail_rect의 x값을 3씩 연속적으로 빼면서 snail_surf를 왼쪽으로 움직이게 함.
    # if snail_x_pos < 0:
    #     snail_x_pos = 600
    if snail_rect.right <= 0:       # snail_rect의 오른쪽이 화면의 0보다 같거나 작아지면
        snail_rect.left = 800       # snial_rect의 왼쪽을 800으로 둠 -> 다시 오른쪽에서 왼쪽으로 이동시키기 위함
    screen.blit(snail_surf, snail_rect)     # pygame 화면 상에 그리기 -> 위에서 선언한 사각형
    screen.blit(player_surf, player_rect)   # pygame 화면 상에 그리기 -> 위에서 선언한 사각형

    # if player_rect.colliderect(snail_rect):
    #     print("collision")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
        # print(pygame.mouse.get_pressed())

    pygame.display.update()     # 계속적인 업데이트
    Colck.tick(60)              # FPS(Frame Per Second)는 60으로 선언 -> 1초에 60번씩 업데이트