# tkinter 모듈 임포트
import tkinter

# 윈도우 객체 생성
root = tkinter.Tk()

# 윈도우 크기 지정
root.geometry("400x200")

# 윈도우 타이틀 지정
root.title("파이썬에서 GUI 다루기")

# 라벨 컴포넌트 생성
label = tkinter.Label(root, text="게임 개발 첫걸음", font=("Times New Roman", 20))

# 라벨 배치
label.place(x=80, y=60) # 윈도우 좌표에서는 왼쪼 위 모서리가 원점(0,0)이다.

# 윈도우 표시
root.mainloop()