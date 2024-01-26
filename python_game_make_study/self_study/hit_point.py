import tkinter as tk

def hit_point():
    dx = abs((x1+w1/2) - (x2+w2/2))
    dy = abs((y1+h1/2) - (y2+h2/2))
    if(dx <= w1/2 + w2/2 and dy <= h1/2 + h2/2):
        return True
    return False

def mouse_move(e):
    global x1, y1
    x1 = e.x - w1/2
    y1 = e.y - h1/2
    col = "red"
    if(hit_point() == True):
        col = "yellow"
    
    canvas.delete("RECT1")
    canvas.create_rectangle(x1, y1, x1+w1, y1+h1, fill=col, tags="RECT1")

win = tk.Tk()
win.title("혼자 히트 포인트 공부")
canvas = tk.Canvas(width=600, height=400)
canvas.pack()

canvas.bind("<Motion>", mouse_move)


x1 = 50
y1 = 50
w1 = 100
h1 = 80
canvas.create_rectangle(x1, y1, x1+w1, y1+h1, fill="red", tag="RECT1")

x2 = 300
y2 = 150
w2 = 150
h2 = 180
canvas.create_rectangle(x2, y2, x2+w2, y2+h2, fill="green")


win.mainloop()