import tkinter as tk
from tkinter import messagebox

price = {'coffee' : 350, 'latte' : 400, 'smoothie' : 450, 'tea' : 300}
order = []
sum = 0


def add(item):
    global sum
    if item not in price:
        print("No Drink")
    this_price = price.get(item)
    sum += this_price
    order.append(item)
    textarea.insert(tk.INSERT, item+" ")
    label1['text'] = "price : " + str(sum) + "$"

def but_exit():
    msgbox = tk.messagebox.askquestion('check', "The End??")
    if msgbox == 'yes':
        exit()

win = tk.Tk()
win.title("Order Program")
win.geometry("300x400")


frame1 = tk.Frame(win)
frame1.pack()

tk.Button(frame1, text = "coffee", command = lambda : add('coffee'), width = 10, height = 2).grid(row=0, column = 0)
tk.Button(frame1, text = "latte", command = lambda : add('latte'), width = 10, height = 2).grid(row=1, column = 0)
tk.Button(frame1, text = "smoothie", command = lambda : add('smoothie'), width = 10, height = 2).grid(row=2, column = 0)
tk.Button(frame1, text = "tea", command = lambda : add('tea'), width = 10, height = 2).grid(row=3, column = 0)
tk.Button(frame1, text = "exit", command = but_exit, width = 10, height = 2).grid(row=4, column = 0)

label1 = tk.Label(win, text="price : 0", width = 100, height = 2, fg="blue")
label1.pack()

textarea = tk.Text(win)
textarea.pack()

win.mainloop()