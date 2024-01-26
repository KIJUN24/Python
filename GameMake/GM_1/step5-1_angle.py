from tkinter import *
import math
import time
from PIL import Image, ImageTk


def press(event):
    global up_go, down_go
    print(event.keysym)
    if event.keysym == 'Up':
        up_go = True
    elif event.keysym == "Down":
        down_go = True


def release(event):
    global up_go, down_go
    # print(event.keysym)
    if event.keysym == 'Up':
        up_go = False
    elif event.keysym == "Down":
        down_go = False    


up_go, down_go = (False, False)

win = Tk()

win.title("Game")
# window size -> 800, 800
win_w, win_h = (800, 800)
# win.geometry("{0}x{1}".format(win_w, win_h))
win.geometry(f"{win_w}x{win_h}")


win.bind("<KeyPress>", press)
win.bind("<KeyRelease>", release)


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

win.update()

while True:
    time.sleep(0.01)
    cvs.delete(angle_line)
    cvs.delete(tank)
    if up_go == True and down_go == False and angle_now <= angle_max:
        angle_now += 0.01
    elif down_go == True and up_go == False and angle_now >= angle_min:
        angle_now -= 0.01

    angle_line = cvs.create_line(angle_ctr, (angle_ctr[0] + angle_r*math.cos(angle_now), angle_ctr[1] - angle_r*math.sin(angle_now)), fill = "red", width = 3)

    tank_img = Image.open("C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_1\\tank.png")
    tank_img = tank_img.resize((tank_w, tank_h), Image.ANTIALIAS)
    tank_img = tank_img.rotate(angle_now * 180 / math.pi - 10)
    tank_img = ImageTk.PhotoImage(tank_img, master = win)
    tank = cvs.create_image(tank_cx, tank_cy, image = tank_img)
    
    win.update()