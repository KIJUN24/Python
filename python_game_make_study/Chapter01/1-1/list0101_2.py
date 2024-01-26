import tkinter

# 함수 정의
def key_down(e):
    
    # 변수 key_c에 keycode 값 대입
    key_c = e.keycode
    # label1에 해당 값 표시
    label1["text"] = "keycode " + str(key_c)
    
    # 변수 key_s에 keysym 값 대입
    key_s = e.keysym
    # label2에 해당 값 표시
    label2["text"] = "keysym " + str(key_s)

root = tkinter.Tk()
root.geometry("400x200")
root.title("키 입력")
fnt = ("Times New Raman", 30)

# 키르 눌렀을 때 실행할 함수 지정
root.bind("<KeyPress>", key_down)

label1 = tkinter.Label(text="keycode", font=fnt)
label1.place(x=0, y=0)

label2 = tkinter.Label(text="keysym", font=fnt)
label2.place(x=0, y=80)
root.mainloop()