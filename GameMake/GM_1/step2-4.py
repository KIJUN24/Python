from tkinter import *
from datetime import date, datetime
import time
import random

win = Tk()

win.title("Game")
win.geometry("500x500")

cvs = Canvas(win)
cvs.config(width = 500, height = 500, bd = 0, highlightthickness = 0)
alpha_max = 10
p1 = (250, 200)
p2 = (250, 300)
p2_x = 250
rec = cvs.create_rectangle(p1, p2, fill = "green")
cvs.pack()

win.update()

while True:
    time.sleep(0.01)
    cvs.delete(rec)
    p2_x += random.randrange(-alpha_max, alpha_max + 1)
    p2 = (p2_x, 300)
    rec = cvs.create_rectangle(p1, p2, fill = "green")


    win.update() 