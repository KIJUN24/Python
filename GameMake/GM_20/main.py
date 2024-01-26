import pygame, sys
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time     # current_time은 초 단위로 변환하고 정수화 해줌.
    score_surf = test_font.render(f'Score : {current_time}', False, (64,64,64))     # current_time을 (64,64,64)색으로 포트 설정
    score_rect = score_surf.get_rect(center = (400, 50))    # screen에 넣기 위해 위치 설정.
    screen.blit(score_surf, score_rect)     # screen에 score_surf를 score_rect 위치에 넣음.
    return current_time     # current_time을 어디서든 쓸 수 있게 return을 함

def obstacle_movement(obstacle_list):       # 장애물이 움직일 때 필요한 함수
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []

def collisions(player, obstacles):      # 충돌 시 필요한 함수
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    # play walking animation if the player is on floor
    # display the jump surface when player is not on floor

    global player_surf, player_index

    if player_rect.bottom < 300:
        # jump
        player_surf = player_jump
    else:
        # walk
        player_index += 0.1
        if player_index >= len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]        # player_surf에 저장할 때는 정수화(int형)으로 변환 후 정보값을 넣어준다.
        # player_index가 0일 때 list 안에 있는 walk_1이 화면에 나타난다.
        # 0.1씩 계속 더해지다가 player_index가 1이 되는 순간 list 안에 있는 walk_2가 화면에 나타난다.
        # player_index가 1이 넘어가는 경우 다시 0으로 초기화 시켜준다.

pygame.init()
screen = pygame.display.set_mode((800, 400))    # 화면 크기 세팅 set_mode((w,h)) -> 튜플형태
pygame.display.set_caption("Runner")    # 게임 실행 시 이름 설정
Colck = pygame.time.Clock()
test_font = pygame.font.Font('GameMake/GM_20/font/Pixeltype.ttf', 50)   # 폰드 정의 (폰트, 글자 크기)
game_active = False     # game_active를 False로 선언
start_time = 0          # 초기에 start_time을 0으로 선언(초기화)
score = 0               # 초기에 score을 0으로 선언(초기화)

sky_surface = pygame.image.load('GameMake/GM_20/graphics/Sky.png').convert()    # 사진
ground_surface = pygame.image.load('GameMake/GM_20/graphics/ground.png').convert()  # 사진

# text_surf = test_font.render('My Game', False, 'Black')  # 화면 상 글자 넣기
# score_surf = test_font.render('My Game', False, (64,64,64))  # 화면 상 글자 넣기
# score_rect = score_surf.get_rect(center = (400, 50))

# Obstacles(Snail)
snail_frame_1 = pygame.image.load('GameMake/GM_20/graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('GameMake/GM_20/graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]
# snail_rect = snail_surf.get_rect(bottomright = (600, 300))  # snail_surf의 사진 사각형 -> (bottomright를 기준)

# Obstacles(Fly)
fly_frame_1 = pygame.image.load('GameMake/GM_20/graphics/fly/fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('GameMake/GM_20/graphics/fly/fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []

player_walk_1 = pygame.image.load('GameMake/GM_20/graphics/player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('GameMake/GM_20/graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('GameMake/GM_20/graphics/player/jump.png').convert_alpha()
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))    # player_surf의 사진 사각형 -> (midbottom를 기준)
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('GameMake/GM_20/graphics/player/player_stand.png').convert_alpha()
# player_stand = pygame.transform.scale(player_stand, (200, 400))
# player_stand = pygame.transform.scale2x(player_stand)
player_stand = pygame.transform.rotozoom(player_stand, 0, 2) # (사진, 회전, 배율)
player_stand_rect = player_stand.get_rect(center = (400, 200))      # player_stand의 사각형 기준을 잡음 (기준점 : center)

game_name = test_font.render('Pixel Runner', False, (111,196,169))  # 'Pixel Runner'라는 폰트를 만듦 -> (폰트 내용, 글꼴 부드러움->False, color)
game_name_rect = game_name.get_rect(center = (400, 80))             # game_name 사각형을 기준으로 잡음(기준점 : center)

game_message = test_font.render('Press space to run', False, (111,196,169)) # 'Press apace to run'라는 폰트를 만듦 -> (폰트 내용, 글꼴 부드러움->False, color)
game_message_rect = game_message.get_rect(center = (400, 320))  # game_message 사각형을 기준으로 잡음(기준점 : center)

# Timer
obstacle_timer= pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():    # 게임 이벤트를 만들기 위한 for문
        if event.type == pygame.QUIT:   # 게임 끄기 위함
            pygame.quit()
            sys.exit()
        # if event.type == pygame.MOUSEMOTION:  # 마우스가 움직일 때
        #     print(event.pos)
        # if event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 클릭할 때
        #     print("MOUSE DOWN")
        # if event.type == pygame.MOUSEBUTTONUP:    # 마우스 클릭하고 땔 때
        #     print("MOUSE UP")

        # if event.type == pygame.MOUSEMOTION:
        #     if (player_rect.collidepoint(event.pos)):   # 마우스가 player_rect와 충돌한다면
        #         print("collision")

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (player_rect.collidepoint(event.pos)) and player_rect.bottom >= 300:   # 마우스가 player_rect와 충돌하고 player_rect의 bottom이 300이상일 때
            # 300 : ground_surface 기준
                player_gravity = -20    # -20 : 점프

        if game_active:     # game_active가 True일 때
            if event.type == pygame.KEYDOWN:    # Key를 눌렀을 때
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:   # Space키를 누르고 player_rect의 bottom 값이 300이상일 때
                    player_gravity = -20    # -20 : 점프
                if event.key == pygame.K_ESCAPE:    # ESC키를 눌렀을 때
                    pygame.quit()   # 게임을 끊다
                    sys.exit()      # 오류를 없애기 위함

            # if event.type == pygame.KEYUP:
            #     print("key up")

        else:   # game_active가 False일 때
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:    # Key가 눌리고 Space키를 눌렀을 때
                game_active = True  # game_active를 True로 바꿔준다
                # snail_rect.left = 800   # snail 초기화
                start_time = int(pygame.time.get_ticks() / 1000)    # start_time 선언 : 초 단위로 환산
            if event.type == pygame.KEYDOWN:    # Key가 눌렸을 때
                if event.key == pygame.K_ESCAPE:    # ESC를 눌렀을 때
                    pygame.quit()   # pygame 종료
                    sys.exit()      # pygame 종료 시 오류를 없애기 위함

        if game_active:
            if event.type == obstacle_timer:    # event타입이 obstacle_time이고 game_active가 True라면
                if randint(0,2):    # 0과 1이 랜덤으로 나온다면
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100), 300)))  # obstacle_rect_list에 snail_surf의 사각형을 추가시켜라
                else:   # if문이 아니라면
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100), 210)))    # obstacle_rect_list에 fly_surf의 사각형을 추가시켜라

            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]
            
            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]

    if game_active: # game_active가 True일 때
        screen.blit(sky_surface, (0,0))         # pygame 화면 상에 그리기
        screen.blit(ground_surface, (0,300))    # pygame 화면 상에 그리기
        # pygame.draw.rect(screen, "Pink", score_rect)
        # pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
        # pygame.draw.line(screen, "Gold", (0,0), pygame.mouse.get_pos(), 10)
        # pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50,200,100,100))
        # screen.blit(score_surf, score_rect)    # pygame 화면 상에 그리기
        score = display_score()     # score 변수에 display_score()함수 저장

        # snail_rect.x -= 5   # snail_rect의 x값을 3씩 연속적으로 빼면서 snail_surf를 왼쪽으로 움직이게 함.
        # # if snail_x_pos < 0:
        # #     snail_x_pos = 600
        # if snail_rect.right <= 0:       # snail_rect의 오른쪽이 화면의 0보다 같거나 작아지면
        #     snail_rect.left = 800       # snial_rect의 왼쪽을 800으로 둠 -> 다시 오른쪽에서 왼쪽으로 이동시키기 위함
        # screen.blit(snail_surf, snail_rect)     # pygame 화면 상에 그리기 -> 위에서 선언한 사각형

        # player
        player_gravity += 1     # 점프 후 내려오기 위해 1을 계속적으로 증가시킨다.
        player_rect.y += player_gravity # player_rect값의 y값에 player_gravity를 계속 더해준다.
        if player_rect.bottom >= 300:   # player_rect의 bottom값이 300 이상일 때(ground_surface위에 있을 때)
            player_rect.bottom = 300    # player_rect의 bottom값을 300으로 고정시킨다.
        player_animation()
        screen.blit(player_surf, player_rect)   # pygame 화면 상에 그리기 -> 위에서 선언한 사각형

        # Obastacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collision
        # if snail_rect.colliderect(player_rect): # snail_rect와 player_rect가 충돌할 때
        #     game_active = False     # game_active를 False로 변경
        game_active = collisions(player_rect, obstacle_rect_list)   

    else:   # game_active가 False일 때
        screen.fill((94,129,162))   # screen 색을 (94,129,162)로 둔다.
        screen.blit(player_stand, player_stand_rect)    # player_stand 사진을 복사해 player_stand_rect의 위치에 넣는다.
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0

        score_message = test_font.render(f'Your score : {score}', False, (111,196,169))     # score를 (111,196,169)색으로 폰트 설정
        score_message_rect = score_message.get_rect(center = (400,330))     # 위치 설정을 위한 rect설정
        screen.blit(game_name, game_name_rect)      # game_name을 game_name_rect 위치에 넣는다
        
        if score == 0:  # score가 0일 때
            screen.blit(game_message, game_message_rect)    # game_message를 game_message_rect 위치에 넣어준다
        else:           # score가 0이 아닐 떄
            screen.blit(score_message, score_message_rect)  # score_message를 score_message_rect 위치에 넣어준다

    pygame.display.update()     # 계속적인 업데이트
    Colck.tick(60)              # FPS(Frame Per Second)는 60으로 선언 -> 1초에 60번씩 업데이트