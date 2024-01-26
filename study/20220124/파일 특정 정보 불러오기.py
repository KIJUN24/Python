import openpyxl
from openpyxl import load_workbook
import tkinter as tk
from tkinter import Button, Entry, Frame, Label, Spinbox, messagebox
from datetime import datetime
import os.path
import pandas as pd
from tkinter.ttk import *

df1 = pd.read_excel(io = "C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\test_order.xlsx", sheet_name='order', usecols='D:L')
df2 = pd.read_excel(io = "C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\test_order.xlsx", sheet_name='order', usecols='D:G')
df3 = pd.read_excel(io = "C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\test_order.xlsx", sheet_name='order', usecols='H:K')
df4 = pd.read_excel(io = "C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\test_order.xlsx", sheet_name='order', usecols='L')


win2 = tk.Tk()
win2.geometry("500x600")
win2.title("settlemnt window")


frame_sw1 = tk.Frame(win2)
frame_sw1.pack()
frame_sw2 = tk.Frame(win2)
frame_sw2.pack()
frame_sw3 = tk.Frame(win2)
frame_sw3.pack()

label_sw1 = tk.Label(frame_sw1)
label_sw1.pack()
label_sw2 = tk.Label(frame_sw2, text = "정산 선택")
label_sw2.pack()
label_sw3 = tk.Label(win2)
label_sw3.pack()

cb_list = ["총합", "음료", "디저트", "총금액"]
cb = Combobox(win2)
cb.config(values = cb_list)
cb.pack()


def click():
    lab_text = cb.get()
    if(lab_text == '총합'):
        # df2 = pd.read_excel(io = "C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\test_order.xlsx", sheet_name='order', usecols='D:L', index = False)
        label_sw3.config(text = df1)
        # textarea2.insert(tk.INSERT, df2 + " ")
        print(df1)
    elif(lab_text == '음료'):
        label_sw3.config(text = df2)
        print(df2)
    elif(lab_text == '디저트'):
        label_sw3.config(text = df3)
        print(df3)
    elif(lab_text == '총금액'):
        label_sw3.config(text = df4)
        print(df4)
    # label_sw1.config(text = df1)
    # label_sw1.config(text = df2)
    # label_sw1.config(text = df3)
    # label_sw1.config(text = df4)

but_sw1 = tk.Button(win2)
but_sw1.config(text = "선택")
but_sw1.config(command=click)
but_sw1.pack()

textarea2 = tk.Text(win2)
textarea2.pack(padx = 10, pady = 10)


# read_xlsx()


win2.mainloop()