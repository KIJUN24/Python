from tkinter import *
from PIL import Image, ImageTk

win = Tk()

win.geometry("500x500")
win.title("Game")

cvs = Canvas(win)
cvs.config(width = 500, height = 500, bd = 0, highlightthickness = 0)
# cvs.configure(background="green")
# p1 = (200, 200)
# p2 = (300, 300)
p3 = (250, 250)
# cvs.create_line(p1, p2, fill = "#6EB0D7", width = 10)
# cvs.create_rectangle(p1, p2, fill = "green", width = 5, outline = 'red')
# cvs.create_oval(p1, p2, fill = 'yellow')
# cvs.create_arc(p1, p2, extent = 60)
# cvs.create_text(p3, text = "GAME", font = ("Arial", 20), fill = "gray")

img = Image.open("C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\GameMake\\GM_1\\tank.png")
img = img.resize((50, 50), Image.ANTIALIAS)
img = img.rotate(20) # 마이너스 방향도 가능.
img = ImageTk.PhotoImage(img, master = win)
cvs.create_image(p3, image = img)

cvs.pack()


win.mainloop()