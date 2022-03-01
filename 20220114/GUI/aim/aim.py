#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
import random
from datetime import datetime

k = 1

def cc():
    global k
    if(k < num_t):
        k += 1
        but.destroy()
        ran_but()
    else:
        fin = datetime.now()
        dif_sec = (fin - start).total_seconds()
        but.destroy()
        lab = Label(win)
        lab.config(text = "Clear " + str(dif_sec) + "초")
        lab.pack(pady = 230)


def ran_but():
    global but
    but = Button(win)
    but.config(bg = "red")
    but.config(command = cc)
    but.config(text = k)
    but.place(relx = random.random(), rely = random.random())


def but_f():
    global num_t
    global start
    global g_win_w, g_win_h
    g_win_w, g_win_h = (500, 500)
    num_t = int(ent.get())
    for wg in win.grid_slaves(): # [label, entry, button]
        wg.destroy()
    win.geometry(f"{g_win_w}x{g_win_h}")
    # 랜덤한 위치에서 버튼이 생성
    ran_but()
    # 시작할 때 시간 저장
    start = datetime.now()


win = Tk()

win.title("AIM_GAME")
win.geometry("550x150")
win.option_add("*Font", "궁서 20")

# Label
lab = Label(win)
lab.config(text = "표적 개수")
lab.grid(column=0, row=0, padx = 20, pady = 20)


# Entry
ent = Entry(win)
ent.grid(column=1, row=0, padx = 20, pady = 20)


# Button
but = Button(win)
but.config(text = "시작")
but.config(command = but_f)
but.grid(column=0, row=1, columnspan=2)


win.mainloop()

