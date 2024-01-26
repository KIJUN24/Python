import tkinter as tk

root = tk.Tk()
root.title("앱 데이터")
canvas = tk.Canvas(width=366, height=240)
canvas.pack()
img = [
    tk.PhotoImage(file="C:\\Users\\lkjun\\OneDrive\\바탕 화면\\Programing_Workspace\\PythonWorkspace\\python_game_make_study\\Chapter01\\1-4\\chip0.png"),
    tk.PhotoImage(file="C:\\Users\\lkjun\\OneDrive\\바탕 화면\\Programing_Workspace\\PythonWorkspace\\python_game_make_study\\Chapter01\\1-4\\chip0.png"),
    tk.PhotoImage(file="C:\\Users\\lkjun\\OneDrive\\바탕 화면\\Programing_Workspace\\PythonWorkspace\\python_game_make_study\\Chapter01\\1-4\\chip1.png"),
    tk.PhotoImage(file="C:\\Users\\lkjun\\OneDrive\\바탕 화면\\Programing_Workspace\\PythonWorkspace\\python_game_make_study\\Chapter01\\1-4\\chip2.png"),
    tk.PhotoImage(file="C:\\Users\\lkjun\\OneDrive\\바탕 화면\\Programing_Workspace\\PythonWorkspace\\python_game_make_study\\Chapter01\\1-4\\chip3.png")
    ]   
map_data = [
    [0,1,0,2,2,2,2],
    [3,0,0,0,2,2,2],
    [3,0,0,1,0,0,0],
    [3,3,0,0,0,0,1],
    [3,3,3,3,0,0,0]
]

for y in range(5):
    for x in range(7):
        n = map_data[y][x]
        canvas.create_image(x*48+24, y*48+24, image=img[n])

root.mainloop()