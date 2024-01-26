from tkinter import *
from datetime import datetime

def what_time():
    dnow = (datetime.now())
    btn.config(text = dnow)

win = Tk()

win.geometry("600x100")
win.title("What time?")
win.option_add("*Font", "궁서체, 20")

btn = Button(win)
btn.config(text = "현재 시각")
btn.config(width = 30)
btn.config(command = what_time)
btn.pack()

win.mainloop()