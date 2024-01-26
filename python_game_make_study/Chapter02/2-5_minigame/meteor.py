import tkinter as tk
import random

fnt1 = ("Times New Roman", 24)
fnt2 = ("Times New Roman", 50)
index = 0
timer = 0
score = 0
bg_pos = 0                  # 배경 표시 위치 변수
px = 240                    # 플레이어(우주선) x좌표 변수
py = 540                    # 플레이어(우주선) y좌표 변수
METEO_MAX = 30              # 유성 수
mx = [0] * METEO_MAX        # 유성 x 좌표 관리 리스트
my = [0] * METEO_MAX        # 유성 y 좌표 관리 리스트

key = ""                    # 키 값을 대입할 변수
koff = False                # 키를 눌렀다 똈을 때 사용할 변수(플래그)


def key_down(e):            # 함수를 눌렀을 때 실행할 함수
    global key, koff        # 전역 변수 선언

    key = e.keysym          # key에 keysym 값 대입
    koff = False            # koff에 False 대입


def key_up(e):              # 키를 눌렀다가 뗐을 때 실행할 함수
    global koff         

    koff = True             # koff에 True 대입


def main():                 # 메인 처리 수행 함수
    global key, koff, index, timer, score, bg_pos, px

    timer += 1              # timer 값 1씩 증가
    bg_pos = (bg_pos + 1) % 640 # 배경을 그릴 위치 계산
    canvas.delete("SCREEN")     # 우선 화면상의 모든 그림과 문자열 삭제
    canvas.create_image(240, bg_pos - 320, image=img_bg, tag="SCREEN")      # 배경 우주 이미지 그리기
    canvas.create_image(240, bg_pos + 320, image=img_bg, tag="SCREEN")      # 배경 우주 이미지 그리기
    if(index == 0): # 타이틀 화면
        canvas.create_text(240, 240, text="METEOR", fill="gold", font=fnt2, tag="SCREEN")               # 타이틀 문자열 표시
        canvas.create_text(240, 480, text="Press [SPACE] Key", fill="lime", font=fnt1, tag="SCREEN")    # 'Press [SPACE] key' 문자열 표시
        if(key == "space"): # space 키를 눌렀다면
            score = 0       # score를 0으로 변경
            px = 240        # 우주선 위치 화면 중앙으로 지정
            init_enermy()
            index = 1
    if(index == 1):
        score += 1
        move_player()
        move_enermy()
    if(index == 2):
        move_enermy()
        canvas.create_text(240, timer*4, text="GAME OVER", fill="red", font=fnt2, tag="SCREEN")
        if(timer == 60):
            index = 0
            timer = 0
    canvas.create_text(240, 30, text="SCORE " + str(score), fill="white", font=fnt1, tag="SCREEN")
    if(koff == True):
        key = ""
        koff = False
    root.after(50, main)


def hit_check(x1, y1, x2, y2):
    if((x1-x2) * (x1-x2) + (y1-y2) * (y1-y2) < 36 * 36):
        return True
    return False


def init_enermy():
    for i in range(METEO_MAX):
        mx[i] = random.randint(0, 480)
        my[i] = random.randint(-640, 0)


def move_enermy():
    global index, timer

    for i in range(METEO_MAX):
        my[i] = my[i] + 6 + i / 5
        if(my[i] > 660):
            mx[i] = random.randint(0, 480)
            mx[i] = random.randint(-640, 0)
        if(index == 1 and hit_check(px, py, mx[i], my[i]) == True):
            index = 2
            timer = 0
        canvas.create_image(mx[i], my[i], image=img_enemy, tag="SCREEN")


def move_player():
    global px

    if(key == "Left" and px > 30):
        px -= 10
    if(key == "Right" and px < 450):
        px += 10
    canvas.create_image(px, py, image=img_player[timer%2], tag="SCREEN")


root = tk.Tk()
root.title("Mini Game")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tk.Canvas(width=480, height=640)
canvas.pack()

img_player = [
    tk.PhotoImage(file="C:\\Users\\lkjun\\OneDrive\\바탕 화면\\Programing_Workspace\\PythonWorkspace\\python_game_make_study\\Chapter02\\2-5_minigame\\starship0.png"),
    tk.PhotoImage(file="C:\\Users\\lkjun\\OneDrive\\바탕 화면\\Programing_Workspace\\PythonWorkspace\\python_game_make_study\\Chapter02\\2-5_minigame\\starship1.png")
    ]

img_enemy = [
    tk.PhotoImage(file="C:\\Users\\lkjun\\OneDrive\\바탕 화면\\Programing_Workspace\\PythonWorkspace\\python_game_make_study\\Chapter02\\2-5_minigame\\meteo.png")
    ]

img_bg = [
    tk.PhotoImage(file="C:\\Users\\lkjun\\OneDrive\\바탕 화면\\Programing_Workspace\\PythonWorkspace\\python_game_make_study\\Chapter02\\2-5_minigame\\cosmo.png")
    ]

main()
root.mainloop()