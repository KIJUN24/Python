from tkinter import *
import math
import time
from PIL import Image, ImageTk


win = Tk()

win.title("Game")
# window size -> 800, 800
win_w, win_h = (800, 800)
# win.geometry("{0}x{1}".format(win_w, win_h))
win.geometry(f"{win_w}x{win_h}")

def press(event):
    global up_go, down_go, space_go
    global stage
    if stage == 1:
        # print(event.keysym)
        if event.keysym == "Up":
            up_go = True
        elif event.keysym == "Down":
            down_go = True
        if event.keysym == "space":
            space_go = True
            stage = 2


def release(event):
    global up_go, down_go, space_go
    global bomb_cx, bomb_cy, bomb_vx, bomb_vy, bomb
    global stage
    if stage == 1:
        # print(event.keysym)
        if event.keysym == "Up":
            up_go = False
        elif event.keysym == "Down":
            down_go = False    
    if stage == 2:
        if event.keysym == "space":
            space_go = False
            # bomb
            bomb_cx = round(tank_cx + tank_w*1/2 * math.cos(angle_now))
            bomb_cy = round(tank_cy - tank_w*1/2 * math.sin(angle_now))
            bomb_vx = round(bomb_v_max * power * 1/100 * math.cos(angle_now))
            bomb_vy = round(-bomb_v_max * power * 1/100 * math.sin(angle_now))
            bomb = cvs.create_oval((bomb_cx - bomb_r, bomb_cy - bomb_r), (bomb_cx + bomb_r, bomb_cy + bomb_r), fill = "red")
            stage = 3

up_go, down_go, space_go = (False, False, False)
win.bind("<KeyPress>", press)
win.bind("<KeyRelease>", release)

stage = 1

##################### background #####################
cvs = Canvas(win)
cvs.config(width=win_w, height=win_h, bd = 0, highlightthickness=0)
cvs.pack()

bot_h = round(win_h * 1/5)
bot_c = "#a6a6a6"
cvs.create_rectangle((0,win_h - bot_h), (win_w, win_h), fill=bot_c, outline=bot_c)

mid_h = round((win_h - bot_h) * 1/8)
mid_c = "#994d00"
cvs.create_rectangle((0,win_h - bot_h - mid_h), (win_w, win_h - bot_h), fill=mid_c, outline=mid_c)

top_h = win_h - bot_h - mid_h
top_c = "#b5b5fd"
cvs.create_rectangle((0,0), (win_w, top_h), fill=top_c, outline=top_c)



##################### angle #####################
angle_r = round(bot_h * 1/2)
angle_mx = round(win_w * 1/20)
angle_my = round(bot_h * 1/4)
angle_ctr = (angle_r + angle_mx, win_h - bot_h + angle_my + angle_r)
cvs.create_arc((angle_ctr[0] - angle_r, angle_ctr[1] - angle_r), (angle_ctr[0] + angle_r, angle_ctr[1] + angle_r), fill = "#6666ff", extent = 180)
angle_min = 30 * math.pi / 180
angle_max = 90 * math.pi / 180
cvs.create_line(angle_ctr, (angle_ctr[0] + angle_r*math.cos(angle_min), angle_ctr[1] - angle_r*math.sin(angle_min)), width = 2)
cvs.create_line(angle_ctr, (angle_ctr[0] + angle_r*math.cos(angle_max), angle_ctr[1] - angle_r*math.sin(angle_max)), width = 2)
cvs.create_arc((angle_ctr[0] - round(angle_r*1/5), angle_ctr[1] - round(angle_r*1/5)), (angle_ctr[0] + round(angle_r*1/5), angle_ctr[1] + round(angle_r*1/5)), fill = "#ffcccc", extent = 180)
angle_now = 45 * math.pi / 180
angle_line = cvs.create_line(angle_ctr, (angle_ctr[0] + angle_r*math.cos(angle_now), angle_ctr[1] - angle_r*math.sin(angle_now)), fill = "red", width = 3)



##################### Tank #####################
tank_w, tank_h = round(min(win_w, win_h) * 1/10), round(min(win_w, win_h) * 1/10)
tank_cx = round(win_w*1/40 + tank_w*1/2)
tank_cy = top_h - round(tank_h*1/2)
tank_img = Image.open("C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_1\\tank.png")
tank_img = tank_img.resize((tank_w, tank_h), Image.ANTIALIAS)
tank_img = tank_img.rotate(angle_now * 180 / math.pi - 10) # 마이너스 방향도 가능.
tank_img = ImageTk.PhotoImage(tank_img, master = win)
tank = cvs.create_image(tank_cx, tank_cy, image = tank_img)


##################### Gauge bar #####################
gbar_mx = angle_mx
gbar_my = angle_my
gbar_w = win_w - angle_mx - gbar_mx*2 - angle_r*2
gbar_h = bot_h - gbar_my*2
gbar_x = angle_mx + angle_r*2 + gbar_mx
gbar_y = win_h - gbar_my - gbar_h
cvs.create_rectangle((gbar_x, gbar_y), (gbar_x + gbar_w, gbar_y + gbar_h), fill = "white")
rbar_mx = round(gbar_h * 1/8)
rbar_my = rbar_mx
rbar_x = gbar_x + rbar_mx
rbar_y = gbar_y + rbar_my
power = 0
rbar_w = (gbar_w - rbar_mx*2) * power * 1/100
rbar_h = gbar_h - rbar_my*2
rbar = cvs.create_rectangle((rbar_x, rbar_y), (rbar_x + rbar_w, rbar_y + rbar_h),width = 0 ,fill = "red")


##################### Bomb #####################
bomb_r = 10
bomb_v_max = 50
bomb_ay = 3


win.update()


while True:
    time.sleep(0.01)

    cvs.delete(angle_line)
    cvs.delete(tank)
    cvs.delete(rbar)
    try:
        cvs.delete(bomb) # bomb이 없을 때 지울 경우 오류가 생길 수 있으므로 try ~ except ~ 사용
    except:
        pass

    if stage == 1:
        if up_go == True and down_go == False and angle_now <= angle_max:
            angle_now += 0.01
        elif down_go == True and up_go == False and angle_now >= angle_min:
            angle_now -= 0.01

    # angle
    angle_line = cvs.create_line(angle_ctr, (angle_ctr[0] + angle_r*math.cos(angle_now), angle_ctr[1] - angle_r*math.sin(angle_now)), fill = "red", width = 3)

    # tank
    tank_img = Image.open("C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_1\\tank.png")
    tank_img = tank_img.resize((tank_w, tank_h), Image.ANTIALIAS)
    tank_img = tank_img.rotate(angle_now * 180 / math.pi - 10)
    tank_img = ImageTk.PhotoImage(tank_img, master = win)
    tank = cvs.create_image(tank_cx, tank_cy, image = tank_img)

    # gauge
    if stage == 2:
        if space_go == True and power < 100:
            power += 3
    rbar_w = (gbar_w - rbar_mx*2) * power * 1/100
    if power > 0:
        
        rbar = cvs.create_rectangle((rbar_x, rbar_y), (rbar_x + rbar_w, rbar_y + rbar_h), width = 0 ,fill = "red")

    # bomb
    if stage == 3:
        bomb_vx += 0
        bomb_vy += bomb_ay
        bomb_cx += bomb_vx
        bomb_cy += bomb_vy
        bomb = cvs.create_oval((bomb_cx - bomb_r, bomb_cy - bomb_r), (bomb_cx + bomb_r, bomb_cy + bomb_r), fill = "red")
        if bomb_cy >= top_h:
            stage = 1
            power = 0


    win.update()