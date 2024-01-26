import tkinter as tk

def mouse_click(e):
    px = e.x        # px에 마우스 포인터 x 좌표 대입
    py = e.y        # py에 마우스 포인터 y 좌표 대입
    print("마우스 포인터 좌표 : {}, {}".format(px, py))
    mx = int(px / 48)
    my = int(py / 48)
    if(0 <= mx and mx <= 6 and 0 <= my and my <= 4):        # mx와 my가 데이터 범위 안이면
        n = map_data[my][mx]                                   # n에 맵 칩 번호 대입
        print("여기에 있는 맵 칩은 " + CHIP_NAME[n])             # 맵 칩 이름 출력

root = tk.Tk()
root.title("맵 데이터")
canvas = tk.Canvas(width=336, height=240)
canvas.pack()
canvas.bind("<Button>", mouse_click)        # 캔버스 클릭 시 실행할 함수 지정
CHIP_NAME = ["풀", "꽃", "숲", "바다"]

img = [
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
        canvas.create_image(x*48+24, y*48+24, image=img[map_data[y][x]])

'''
for문 설명
반복 : y 값은 0~4에서 1씩 증가
    반복 : x 값은 0~6에서 1씩 증가
        변수 n에 리스트 값 대입
'''

root.mainloop()