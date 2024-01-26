# background : <a href='https://www.freepik.com/photos/paper-wallpaper'>Paper wallpaper photo created by rawpixel.com - www.freepik.com</a>
# bomb : <a href="https://www.flaticon.com/kr/free-icons/" title="폭탄 아이콘">폭탄 아이콘  제작자: photo3idea_studio - Flaticon</a>
# character : <a href='https://kr.freepik.com/vectors/baby'>Baby 벡터는 mamewmy - kr.freepik.com가 제작함</a>
'''
하늘에서 떨어지는 폭탄 피하기 게임을 만드시오
[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 폭탄은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
3. 캐릭터가 폭탄을 피하면 다음 폭탄이 다시 떨어짐
4. 캐릭터가 폭탄에 충돌하면 게임 종료
5. FPS는 30으로 고정

[게임 이미지]
1. 배경 : 480 X 640 (가로, 세로) -> background.png
2. 캐릭터 : 70 X 70 -> character.png
3. 폭탄 : 70 X 70 -> enemy.png
'''
import pygame, sys
from random import *

pygame.init()

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Quiz")

clock = pygame.time.Clock()

background = pygame.image.load('GameMake/GM_13_study/image_quiz/background.png')
# background = pygame.image.load('GameMake/GM_13_study/image/background.png')

character_image = pygame.image.load('GameMake/GM_13_study/image_quiz/character.png')
# character_image = pygame.image.load('GameMake/GM_13_study/image/character.png')
character = pygame.transform.scale(character_image, (70,70))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (SCREEN_WIDTH / 2) - (character_width / 2)
character_y_pos = SCREEN_HEIGHT - character_height


enemy_image = pygame.image.load('GameMake/GM_13_study/image_quiz/enemy.png')
# enemy_image = pygame.image.load('GameMake/GM_13_study/image/enemy.png')
enemy = pygame.transform.scale(enemy_image, (70,70))
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
# enemy_x_pos = (SCREEN_WIDTH / 2) - (enemy_width / 2)
# enemy_y_pos = SCREEN_HEIGHT - enemy_height
enemy_x_pos = randint(0, SCREEN_WIDTH - enemy_width)
enemy_y_pos = 0
enemy_speed = 10

to_x = 0
character_speed = 8

running = True
while running:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_LEFT:
                to_x -= character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0

    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > SCREEN_WIDTH - character_width:
        character_x_pos = SCREEN_WIDTH - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > SCREEN_HEIGHT:
        enemy_y_pos = 0
        enemy_x_pos = randint(0, SCREEN_HEIGHT - enemy_width)

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update()

    clock.tick(30)
