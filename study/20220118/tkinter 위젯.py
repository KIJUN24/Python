from tkinter import *
from tkinter.ttk import *  # Combobox일 때만 사용


# # Listbox
# def click():
#     text = lb.curselection()[0] 
#     print(text)



# # Check Button
# def click():
#     text = cv.get()
#     print(text)


# # Radio Button
# def click():
#     lab_text = rv.get()
#     lab.config(text = lab_text)


# Combobox Button
def click():
    lab_text = cb.get()
    lab.config(text = lab_text)


# # Spinbox Button
# def click():
#     lab_text = sb.get()
#     lab.config(text = lab_text)


# # Spinbox Button
# def click():
#     lab_text = scale.get()
#     lab.config(text = lab_text)
#     print(lab_text)


win = Tk()

win.geometry("500x500")

win.option_add("*Font", "Arial 20")

# # Listbox
# lb = Listbox(win)
# # lb.config(selectmode = "multiple") # 여러 개 선택할 때 사용
# lb.insert(0, "1번")
# lb.insert(1, "2번")
# lb.insert(2, "3번")
# lb.insert(3, "4번")
# lb.pack()


# # Check Button
# cv = IntVar()
# cb1 = Checkbutton(win, text = "1번", variable = cv)
# cb1.pack()


# # Radio Button
# rv = IntVar()
# rb1 = Radiobutton(win, text = "1번", value=0, variable = rv)
# rb2 = Radiobutton(win, text = "2번", value=1, variable = rv)
# rb3 = Radiobutton(win, text = "3번", value=2, variable = rv)
# rb1.pack()
# rb2.pack()
# rb3.pack()


# Combobox
cb_list = ["1번", "2번", "3번"]
cb = Combobox(win)
cb.config(values = cb_list)
cb.pack()


# # Spinbox
# sb = Spinbox(win)
# sb.config(from_=-3, to=3)
# sb.pack()


# # Scale
# scale = Scale(win)
# scale.config(length = 1000,tickinterval = 20, from_=0, to=100, orient="horizontal")
# # orient="horizontal" : 가로
# scale.pack()


# Button
but = Button(win)
but.config(text = "옵션 선택")
but.config(command = click)
but.pack()


# Label
lab = Label(win)
lab.pack()

win.mainloop()