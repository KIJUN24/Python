import tkinter as tk
import math

root = tk.Tk()
root.title("삼각함수를 활용한 선 그리기")

canvas = tk.Canvas(width=400, height=400, bg="white")
canvas.pack()

for d in range(0, 90, 10):      # d값이 0에서 90까지 10씩 증가
    a = math.radians(d)
    x = 300 * math.cos(a)       # 선의 끝 x좌표를 cos으로 계산
    y = 300 * math.sin(a)       # 선의 끝 y좌표를 sin으로 계산 
    canvas.create_line(0, 0, x, y, fill="blue") # (0,0)에서 (x,y)까지 선 그음

root.mainloop()