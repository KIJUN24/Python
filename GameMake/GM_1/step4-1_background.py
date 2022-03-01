from tkinter import *

win = Tk()

win.title("Game")
# window size -> 800, 800
win_w, win_h = (800, 800)
# win.geometry("{0}x{1}".format(win_w, win_h))
win.geometry(f"{win_w}x{win_h}")


cvs = Canvas(win)
cvs.config(width=win_w, height=win_h, bd = 0, highlightthickness=0)
cvs.pack()


bot_h = round(win_h * 1/5)
bot_c = "#b3b3b3"
cvs.create_rectangle((0,win_h - bot_h), (win_w, win_h), fill=bot_c, outline=bot_c)


mid_h = round((win_h - bot_h) * 1/8)
mid_c = "#993333"
cvs.create_rectangle((0,win_h - bot_h - mid_h), (win_w, win_h - bot_h), fill=mid_c, outline=mid_c)


top_h = win_h - bot_h - mid_h
top_c = "#00ccff"
cvs.create_rectangle((0,0), (win_w, top_h), fill=top_c, outline=top_c)

win.mainloop()