from tkinter import *
from datetime import datetime

right_go = False

def press(event):
    global right_go, t_0
    if event.keysym == "space" and right_go != True:
        right_go = True
        t_0 = datetime.now()


win = Tk()

win.title = ("Game")
win.geometry("1000x500")


win.bind("<KeyPress>", press)


cvs = Canvas(win)
cvs.config(width = 1000, height = 500, bd = 0, highlightthickness = 0)
p1 = (0, 200)
p2 = (100, 300)
sqr = cvs.create_rectangle(p1, p2, fill = "green")

velo = 1000 / 10

cvs.pack()

win.update()


while True:
    cvs.delete(sqr)
    if(right_go == True):
        t_now = datetime.now()
        t_delta = (t_now - t_0).total_seconds()
        p1_x = round(0 + velo * t_delta)
        p2_x = p1_x + 100
        p1 = (p1_x, 200)
        p2 = (p2_x, 300)
    sqr = cvs.create_rectangle(p1, p2, fill = "green")
    win.update()