import tkinter as tk
from tkinter import Entry, messagebox
from openpyxl import load_workbook
import openpyxl
from datetime import datetime
import os.path
import pandas as pd

source = {'날짜', '이름'
, '커피', '라떼', '스무디', '차'
, '케이크', '쿠키', '아이스크림', '타르트'
, '총금액'
}

make_wb = openpyxl.Workbook()
new_filename = 'C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\test_order.xlsx'
make_wb.active.title = "order"
DataA = pd.DataFrame(source)
make_wb.save(new_filename)

print(DataA)