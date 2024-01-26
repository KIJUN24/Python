import tkinter as tk

fnt1 = ("times New Roman", 20)
fnt2 = ("times New Roman", 40)
index = 0
timer = 0

key = ""        # 키 값을 대입할 변수

def key_down(e):        
    global key      # key를 전역변수로 선언
    key = e.keysym  # key에 keysym 값 대입

def main():
    global index, timer
    canvas.delete("STATUS")     # 먼저 index와 timer 표시 삭제
    timer += 1
    canvas.create_text(200, 30, text="index " + str(index), fill="white", font=fnt1, tag="STATUS")
    canvas.create_text(400, 30, text="timer " + str(timer), fill="cyan", font=fnt1, tag="STATUS")

    if(index == 0):         # index 0일 경우(타이틀 화면)
        if(timer == 1):     # timer 값이 1이면
            canvas.create_text(300, 150, text="타이틀", fill="white", font=fnt2, tags="TITLE")          # 타이틀 문자 표시
            canvas.create_text(300, 300, text="Press[SPACE]Key", fill="lime", font=fnt1, tag="TITEL")   # 'Press [Space] Key' 문자열 표시

        if(key == "space"):             # 스페이스 키를 눌렀다면
            canvas.delete("TITLE")      # 타이틀 문자 삭제
            canvas.create_rectangle(0, 0, 600, 400, fill="blue", tag="GAME")                        # 캔버스를 파란색으로 칠함
            canvas.create_text(300, 150, text="게임중", fill="white", font=fnt2, tag="GAME")        # '게임 중' 문자열 표시
            canvas.create_text(300, 300, text="[E] 종료", fill="yellow", font=fnt1, tag="GAME")     # '[E] 종료' 문자열 표시
            index = 1   # index 값 1로 변경
            timer = 0   # timer 값 0으로 변경

    if(index == 1):         # index 1처리(플레이 중 화면)
        if(key == "e"):     # E 키를 눌렀다면
            canvas.delete("GAME")   # '게임 중' 문자열 삭제
            canvas.create_rectangle(0, 0, 600, 400, fill="maroon", tag="OVER")          # 캔버스를 갈색으로 칠함
            canvas.create_text(300, 150, text="GAME OVER", fill="black", tag="OVER")    # 'GAME OVER' 문자열 표시
            index = 2   # index 값 2로 변경
            timer = 0   # timer 값 0으로 변경

    if(index == 2):         # index 2 처리(게임 오버 화면)
        if(timer== 30):     # timer가 30이 되었다면
            canvas.delete("OVER")       # 'GAME OVER' 문자열 삭제
            index = 0       # index 값 0로 변경
            timer = 0       # timer 값 0으로 변경
    
    root.after(100, main)   # 100밀리초 이후 다시 main() 함수 실행



root = tk.Tk()
root.title("인덱스와 타이머")
root.bind("<KeyPress>", key_down)
canvas = tk.Canvas(width=600, height=400, bg="black")
canvas.pack()
main()
root.mainloop()