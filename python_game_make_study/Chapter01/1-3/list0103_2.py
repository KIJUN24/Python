import tkinter

x = 0   # 스크롤 위치 관리 변수

def scroll_bg():
    global x        # x를 스크롤 변수로 취급
    x = x + 1       
    if(x == 480):   # x가 480이 되면
        x = 0       # x에 0 대입
    
    # 먼저 배경 이미지 삭제
    canvas.delete("BG")     

    # 배경 이미지 그리기(왼쪽)
    canvas.create_image(x-240, 150, image=img_bg, tag="BG")

    # 배경 이미지 그리기(오른쪽)
    canvas.create_image(x+240, 150, image=img_bg, tag="BG")

    # 50밀리 초 후 함수 재실행_실시간 처리
    root.after(50, scroll_bg)

root = tkinter.Tk()
root.title("화면 스크롤")
canvas = tkinter.Canvas(width=480, height=300)
canvas.pack()
img_bg = tkinter.PhotoImage(file="C:\\Users\\lkjun\\OneDrive\\바탕 화면\\Programing_Workspace\\PythonWorkspace\\python_game_make_study\\Chapter01\\1-3\\park.png")
scroll_bg()
root.mainloop()