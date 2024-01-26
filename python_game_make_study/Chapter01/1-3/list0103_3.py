import tkinter as tk

x = 0       # 스크롤 위치 관리 변수
ani = 0     # 개 애니메이션용 변수
def animation():
    global x, ani
    x += 4
    if(x == 480):
        x = 0
    canvas.delete("BG")
    canvas.create_image(x-240, 150,image = img_bg , tag="BG")
    canvas.create_image(x+240, 150,image = img_bg , tag="BG")
    ani = (ani + 1) % 4
    canvas.create_image(240, 200, image=img_dog[ani], tag = "BG")
    root.after(200, animation)


root = tk.Tk()
root.title("애니메이션")
canvas = tk.Canvas(width=480, height=300)
canvas.pack()
img_bg = tk.PhotoImage(file="C:\\Users\\lkjun\\OneDrive\\바탕 화면\\Programing_Workspace\\PythonWorkspace\\python_game_make_study\\Chapter01\\1-3\\park.png")

# 리스트 img_dog에 개 이미지 로딩 애니메이션용 이미지 4장
img_dog = [
    tk.PhotoImage(file="C:\\Users\\lkjun\\OneDrive\\바탕 화면\\Programing_Workspace\\PythonWorkspace\\python_game_make_study\\Chapter01\\1-3\\dog0.png"),
    tk.PhotoImage(file="C:\\Users\\lkjun\\OneDrive\\바탕 화면\\Programing_Workspace\\PythonWorkspace\\python_game_make_study\\Chapter01\\1-3\\dog1.png"),
    tk.PhotoImage(file="C:\\Users\\lkjun\\OneDrive\\바탕 화면\\Programing_Workspace\\PythonWorkspace\\python_game_make_study\\Chapter01\\1-3\\dog2.png"),
    tk.PhotoImage(file="C:\\Users\\lkjun\\OneDrive\\바탕 화면\\Programing_Workspace\\PythonWorkspace\\python_game_make_study\\Chapter01\\1-3\\dog3.png")
    ]
animation()
root.mainloop()