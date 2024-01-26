import tkinter as tk
import math

root = tk.Tk()
root.title("삼각함수를 활용한 도형 그리기")

canvas = tk.Canvas(width=600, height=600, bg="black")
canvas.pack()

# 8개 색상을 리스트로 정의
COL = ["greenyellow", "limegreen", "aquamarine", "cyan", "deepskyblue", "blue", "blueviolet", "violet"]

for d in range(0, 360):     # d 값이 0에서 360까지 1씩 증가
    x = 250 * math.cos(math.radians(d))     # 선의 끝 x좌표를 cos으로 계산
    y = 250 * math.sin(math.radians(d))     # 선의 끝 y좌표를 sin으로 계산
    # 이와 같이 함수를 다른 함수의 인수로 사용할 수 있다.

    # 캔버스 중심(300, 300)에서 삼각함수로 계산한 좌표까지 선 그음
    canvas.create_line(300, 300, 300+x, 300+y, fill=COL[d%8], width=2)

root.mainloop()