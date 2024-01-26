import tkinter
import datetime

def time_now():
    # 변수 d에 현재 일시 대입
    d = datetime.datetime.now()
    # 변수 t에 시, 분, 초 대입
    t = "{0}:{1}:{2}".format(d.hour, d.minute, d.second)
    # label 문자열로 변환
    label["text"] = t
    # 1초 후 다시 함수 실행
    root.after(1000, time_now)

    # root.after(1000, time_now) : 1초 후에 다시 동일 함수 실행

root = tkinter.Tk()
root.geometry("400x200")
root.title("간이 계산")

label = tkinter.Label(font=("Times New Roman", 60))
label.pack()
time_now()
root.mainloop()



# 함수 실행 순서
# 1. 가장 먼저 time_now()함수 실행
# 2. 시각을 언은 후 라벨 업데이트
# 3. 1초 후에 다시 동일 함수 실행