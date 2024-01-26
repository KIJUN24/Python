from tkinter import *
from datetime import date, datetime
import time

win = Tk()

win.title("Game")
win.geometry("500x500")

cvs = Canvas(win)
cvs.config(width = 500, height = 500, bd = 0, highlightthickness = 0)

disp_total = 500
t_total = 5
velo = disp_total / t_total

p1 = (0, 200)
p2 = (0, 300)

rec = cvs.create_rectangle(p1, p2, fill = "green")

cvs.pack()

win.update()

t_0 = datetime.now()
while True:
    cvs.delete(rec)
    t_now = datetime.now()
    t_delta = (t_now - t_0).total_seconds()
    p2_x = round(velo * t_delta)
    p2 = (p2_x, 300)
    rec = cvs.create_rectangle(p1, p2, fill = "green")


    win.update()