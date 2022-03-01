from tkinter import *
# from tkinter
# tkinter.Tk()

win = Tk() # 창 생성

win.geometry("1000x500") # 500 픽셀(문자열)
win.title("temp")
win.option_add("*Font", "맑은고딕 25")

btn = Button(win, text = "버튼")
btn.pack()

win.configure(bg = 'green')

win.mainloop() # 창 실행