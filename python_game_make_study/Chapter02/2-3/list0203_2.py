import tkinter as tk
import math

def trigo():
    try:
        d = float(entry.get())
        a = math.radians(d)
        s = math.sin(a)
        c = math.cos(a)
        t = math.tan(a)
        label_s["text"] = "sin" + str(s)
        label_c["text"] = "cos" + str(c)
        label_t["text"] = "tan" + str(t)
    except:
        print("각도를 도 값으로 입력해주세요 : ")

root = tk.Tk()
root.geometry("300x200")
root.title("삼각함수 값")

entry = tk.Entry(width=10)
entry.place(x=20, y=20)

button = tk.Button(text="계산", command=trigo)
button.place(x=110, y=20)

label_s = tk.Label(text="sin")
label_s.place(x=20, y=60)

label_c = tk.Label(text="cos")
label_c.place(x=20, y=100)

label_t = tk.Label(text="tan")
label_t.place(x=20, y=140)

root.mainloop()