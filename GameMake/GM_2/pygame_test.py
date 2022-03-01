#### alien png : <a href="https://www.flaticon.com/kr/free-icons/" title="외계인 아이콘">외계인 아이콘  제작자: Freepik - Flaticon</a>
#### buttle png : https://www.logoyogo.com/downloads/%EC%B4%9D%EC%95%8C-%EC%95%84%EC%9D%B4%EC%BD%98-%EB%A1%9C%EA%B3%A0-%EC%9D%BC%EB%9F%AC%EC%8A%A4%ED%8A%B8-ai-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C/
#### spaceship png : https://littledeep.com/spaceship-illustration-free-download/


from tkinter.tix import Tree
import pygame
import random
import time
from datetime import datetime

# 1. 게임 초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [400, 900]
screen = pygame.display.set_mode(size)

title = "My Game"
pygame.display.set_caption(title)

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()

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


def crash(a, b):
    if (a.x - b.sx <= b.x) and (b.x <= a.x + a.sx):
        if (a.y - b.sy <= b.y) and (b.y <= a.y + a.sy):
            return True
        else:
            return False
    else:
        return False

def countdown(num_sec):
    while num_sec:
        s = divmod(num_sec, 60)
        sec_format = "{:02d}".format(s)
        print(sec_format, end = '/r')
        time.sleep(1)
        num_sec -= 1
    print("The End")


spaceship = object()
spaceship.put_image("C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_2\\spaceship1.png")
spaceship.change_size(70, 75)
spaceship.x = round(size[0] * 1/2) - round(spaceship.sx * 1/2)
spaceship.y = round(size[1] - spaceship.sy - 10)
spaceship.move = 5

left_go = False
right_go = False
front_go = False
back_go = False
bullet_go = False

m_list = []
a_list = []

black = (0,0,0)
white = (255,255,255)
k = 0

game_over = 0
kill = 0
loss = 0
game_replay = 0

# 4-0. 게임 시작 대기 화면
stop_button = 0
while stop_button == 0:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_button = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stop_button = 1
                

    screen.fill(black)

    # text : start
    font = pygame.font.Font("C:\\Windows\\Fonts\\ariblk.ttf", 15)
    text_start = font.render("PRESS SPACE KEY TO START GAME !!!", True, (255, 255, 255))
    screen.blit(text_start, (40, round(size[1] * 1/2 - 50)))
    
    pygame.display.flip()


# 4. 메인 이벤트
start_time = datetime.now()
stop_button = 0
while stop_button == 0:

    # 4-1. FPS 설정
    clock.tick(60)

    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_button = 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_go = True
            elif event.key == pygame.K_RIGHT:
                right_go = True
            elif event.key == pygame.K_UP:
                front_go = True
            elif event.key == pygame.K_DOWN:
                back_go = True
            # elif event.key == pygame.K_UP and pygame.K_LEFT:
            #     front_go = True
            #     left_go = True
            # elif event.key == pygame.K_UP and pygame.K_RIGHT:
            #     back_go = True
            #     right_go = True
            elif event.key == pygame.K_SPACE:
                bullet_go = True
                k = 0

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False
            elif event.key == pygame.K_UP:
                front_go = False
            elif event.key == pygame.K_DOWN:
                back_go = False
            # elif event.key == pygame.K_UP and pygame.K_LEFT:
            #     front_go = False
            #     left_go = False
            # elif event.key == pygame.K_UP and pygame.K_RIGHT:
            #     front_go = False
            #     right_go = False
            
            elif event.key == pygame.K_SPACE:
                bullet_go = False

    # 4-3. 입력, 시간에 따른 변화
    # time
    now_time = datetime.now()
    delta_time = round((now_time - start_time).total_seconds())

    # spaceship
    if left_go == True:
        spaceship.x -= spaceship.move
        if spaceship.x < 0:
            spaceship.x = 0
    elif right_go == True:
        spaceship.x += spaceship.move
        if spaceship.x > size[0] - spaceship.sx:
            spaceship.x = size[0] - spaceship.sx
    elif front_go == True:
        spaceship.y -= spaceship.move
        if spaceship.y <= 0:
            spaceship.y = 0
    elif back_go == True:
        spaceship.y += spaceship.move
        if spaceship.y > size[1] - spaceship.sy:
            spaceship.y = size[1] - spaceship.sy

    # elif front_go == True and left_go == True:
    #     spaceship.y += spaceship.move
    #     spaceship.x -= spaceship.move
    #     if spaceship.y <= 0:
    #         spaceship.y = 0
    #     if spaceship.x < 0:
    #         spaceship.x = 0

    # bullet
    if bullet_go == True and k % 8 == 0:
        mm = object()
        mm.put_image("C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_2\\bullet.png")
        mm.change_size(25, 40)
        mm.x = round(spaceship.x + spaceship.sx * 1/2 - mm.sx * 1/2)
        mm.y = spaceship.y - mm.sy - 10
        mm.move = 15
        m_list.append(mm)
    k += 1
    d_list = []
    for i in range(len(m_list)):
        m = m_list[i]
        m.y -= m.move
        if m.y <= -m.sy:
            d_list.append(i)
    for d in d_list:
        del m_list[d]

    # alien
    if random.random() > 0.98:
        aa = object()
        aa.put_image("C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_2\\alien.png")
        aa.change_size(40, 45)
        aa.x = random.randrange(0, size[0] - aa.sx - round(spaceship.sx * 1/2))
        aa.y = 10
        aa.move = 2
        a_list.append(aa)
    d_list = []
    for i in range(len(a_list)):
        a = a_list[i]
        a.y += a.move
        if a.y >= size[1]:
            d_list.append(i)
    for d in d_list:
        del a_list[d]
        loss += 1
    
    # crash : bullet and alien
    dm_list = []
    da_list = []
    for i in range(len(m_list)):
        for j in range(len(a_list)):
            m = m_list[i]
            a = a_list[j]
            if crash(m, a) == True:
                dm_list.append(i)
                da_list.append(j)
    dm_list = list(set(dm_list))
    da_list = list(set(da_list))
    for dm in dm_list:
        del m_list[dm]
    for da in da_list:
        del a_list[da]
        kill += 1

    # crash : spaceship and alien 
    for i in range(len(a_list)):
        a = a_list[i]
        if crash(a, spaceship) == True:
            stop_button = 1
            game_over = 1

                
    # 4-4. 그리기
    screen.fill(black)
    #spaceship
    spaceship.show()
    #bullet
    for m in m_list:
        m.show()
    # alien
    for a in a_list:
        a.show()
    
    # text : kill and loss
    font = pygame.font.Font("C:\\Windows\\Fonts\\ariblk.ttf", 20)
    text_kill = font.render("killed : {0}   loss : {1}".format(kill, loss), True, (255, 255, 0))
    screen.blit(text_kill, (10, 5))
    # text : time
    text_time = font.render("time : {0}".format(delta_time), True, (255, 255, 255))
    screen.blit(text_time, (size[0] - 100, 5))

    # 4-5. 업데이트
    pygame.display.flip()

# 5. 게임 종료
while game_over == 1:
    clock.tick(60)
    
    # text : Game over
    font_gameover = pygame.font.Font("C:\\Windows\\Fonts\\ariblk.ttf", 40)
    text_gameover = font_gameover.render("GAME OVER...", True, (255, 0, 0))
    screen.blit(text_gameover, (50, round(size[1] * 1/2 - 80)))
    font_gameover_2 = pygame.font.Font("C:\\Windows\\Fonts\\ariblk.ttf", 20)
    text_gameover_2 = font_gameover_2.render("PRESS SPACE BAR", True, (255, 0, 0))
    screen.blit(text_gameover_2, (53, round(size[1] * 1/2 - 30)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_over = 0
                game_replay = 1

    pygame.display.flip()

# 6. 게임 리플레이(새로운 while문)
while game_replay == 1:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_replay = 0

    screen.fill(black)

    # text : start
    font_replay = pygame.font.Font("C:\\Windows\\Fonts\\ariblk.ttf", 40)
    text_replay = font_replay.render("Game Replay ???", True, (255, 255, 255))
    screen.blit(text_replay, (15, round(size[1] * 1/2 - 100)))

    font_replay = pygame.font.Font("C:\\Windows\\Fonts\\ariblk.ttf", 15)
    text_no = font.render("NO", True, (255, 255, 255))
    screen.blit(text_no, (size[0] * 1/2 - 100, round(size[1] * 1/2 - 30)))

    font_replay = pygame.font.Font("C:\\Windows\\Fonts\\ariblk.ttf", 15)
    text_yes = font.render("YES", True, (255, 255, 255))
    screen.blit(text_yes, (size[0] * 1/2 + 50, round(size[1] * 1/2 - 30)))

    pygame.display.flip()

pygame.quit()