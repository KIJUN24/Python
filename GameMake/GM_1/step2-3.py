from tkinter import *
from datetime import date, datetime
import time

win = Tk()

win.title("Game")
win.geometry("500x500")

cvs = Canvas(win)
cvs.config(width = 500, height = 500, bd = 0, highlightthickness = 0)

disp_total = 1000
t_total = 5
velo = disp_total / t_total
acc = 100 # 가속도
p1 = (250, 400)
p2 = (350, 500)

rec = cvs.create_rectangle(p1, p2, fill = "green")

cvs.pack()

win.update()

t_0 = datetime.now()
while True:
    cvs.delete(rec)
    t_now = datetime.now()
    t_delta = (t_now - t_0).total_seconds()
    p1_y = 400 - velo * t_delta + acc * t_delta ** 2
    p2_y = 500 - velo * t_delta + acc * t_delta ** 2
    p1 = (250, p1_y)
    p2 = (350, p2_y)
    rec = cvs.create_rectangle(p1, p2, fill = "green")


    win.update()