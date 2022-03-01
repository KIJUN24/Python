from platform import release
from tkinter import *

from matplotlib.pyplot import text

def press(event):
    global txt
    txt = event

def release(event):
    global txt
    txt = event    

win = Tk()

win.title = ("Game")
win.geometry("1000x500")

win.bind("<KeyPress>", press)
win.bind("<KeyRelease>", release)

cvs = Canvas(win)
cvs.config(width = 1000, height = 500, bd = 0, highlightthickness = 0)
p1 = (500, 250)
txt = ""
event_txt = cvs.create_text(p1, text = txt, font = ("Arial", 20))
cvs.pack()

win.update()

while True:
    cvs.delete(event_txt)
    event_txt = cvs.create_text(p1, text = txt, font = ("Arial", 20))

    win.update()