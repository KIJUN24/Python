from tkinter import *

win = Tk()

''' pack_study{
win.geometry("400x200")
win.title("pack")
win.option_add("*Font","궁서 20")

ent = Entry(win)
ent.pack()

but1 = Button(win)
but1.config(text = "Button")
def aa():
    but1.pack(pady = ent.get())
but1.config(command = aa)
but1.pack()

but2 = Button()
but2.config(text = "temp  ")
but2.pack()
}
'''

'''
{ grid
win.geometry("400x200")
win.title("grid")
win.option_add("*Font","궁서 20")

but1 = Button(win)
but1.config(text = "(0,0)")
but1.grid(column = 0, row = 0)

but2 = Button(win)
but2.config(text = "(1,0)")
but2.grid(column = 1, row = 0)

but3 = Button(win)
but3.config(text = "(0,1)")
but3.grid(column = 0, row = 1)

# (0,3)을 해도 (0,1)에 붙어서 생성
but4 = Button(win)
but4.config(text = "(0,3)")
but4.grid(column = 0, row = 3)
}
'''

''' grid_for + 병합
win.geometry("600x400")
win.title("grid")
win.option_add("*Font","궁서 20")


but_list = []
col_num = 4
row_num = 3
for i in range(0, col_num):
    for j in range(0, row_num):
        but = Button(win)
        but.config(text = "({0},{1})".format(i, j))
        but.grid(column = i, row = j, padx = 10, pady = 10)
        but_list.append(but)

but1 = Button(win)
but1.config(text = "new1")
but1.grid(column=3, row=0, rowspan=2)

but2 = Button(win)
but2.config(text = "new2")
but2.grid(column=1, row=2, columnspan=2)
'''

win.geometry("600x300")
win.title("place")
win.option_add("*Font","궁서 20")

xx1 = 80
yy1 = 50
but1 = Button(win)
but1.config(text = "({0},{1})".format(xx1,yy1))
but1.place(x=xx1, y=yy1)

xx2 = 0.3
yy2 = 0.5
but2 = Button(win)
but2.config(text = "({0},{1})".format(xx2,yy2))
but2.place(relx=xx2, rely=yy2)

win.mainloop()