import pandas as pd
df = pd.read_excel("C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\drink_order2.xlsx",
sheet_name = "order_program")
# ,skiprows = 1) 위에 한 칸 없애는 함수
# print(df.dropna())
# .dropna() : NaN 하나라도 있으면 삭제 시켜서 보여줌.
df.to_excel("C:\\Users\\lkjun\\OneDrive\\바탕 화면\\PythonWorkspace\\python_study\\Python_practice\\drink_order2_resave.xlsx"
, sheet_name = "order")