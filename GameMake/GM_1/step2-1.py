from tkinter import *
from datetime import datetime
import time

win = Tk()

win.title("Game")
win.geometry("500x500")

cvs = Canvas(win)

cvs.config(width = 500, height = 500, bd = 0, highlightthickness = 0)
# p1 = (200, 200)
# p2 = (300, 300)
p3 = (250, 250)
# sqr = cvs.create_rectangle(p1, p2, fill = 'green')
num = cvs.create_text(p3, text = 0, font = ("Arial", 50))

cvs.pack()

win.update()

# k = 0

t_0 = datetime.now()

while True:
    time.sleep(1)
    # k += 1
    # cvs.delete(sqr)
    # p1 = (200 + k, 200 + k)
    # p2 = (300 + k, 300 + k)
    # sqr = cvs.create_rectangle(p1, p2, fill = 'green')

    cvs.delete(num)
    t_now = datetime.now()
    t_delta = round((t_now - t_0).total_seconds(), 1)
    num = cvs.create_text(p3, text = str(t_delta), font = ("Arial", 50))


    win.update()