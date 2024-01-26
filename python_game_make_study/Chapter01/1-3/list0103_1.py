import tkinter

root = tkinter.Tk()
root.title("Canvas에 화면 그리기")
canvas = tkinter.Canvas(width=480, height=300)
canvas.pack()   # pack() : 윈도우 안에 GUI를 쌓고 배치하는 명령

img_bg = tkinter.PhotoImage(file="C:\\Users\\lkjun\\OneDrive\\바탕 화면\\Programing_Workspace\\PythonWorkspace\\python_game_make_study\\Chapter01\\1-3\\park.png")
# 이처럼 이미지 파일을 못 찾겠다, 못 가져온다고 에러가 발생할 경우 사진이 있는 경로를 찾아서 넣어준다.

canvas.create_image(240, 150, image=img_bg)

root.mainloop()