import pandas as pd

def df_maker(col_num, ind_num, fill):
    col = []
    ind = []
    con = []
    for i in range(0, col_num):
        col.append(fill)
    for i in range(0, ind_num):
        ind.append(fill)
    for i in range(0, ind_num):
        con.append(col)

    return pd.DataFrame(con, columns=col, index=ind)


df = df_maker(2,2,0)
df.columns = ["국어", "수학"]
df.index = ['철수','영희']
print(df)

# 가로
# a = df.loc['철수'] = [70, 90]
# # df.loc["철수"][0] = 100
# print(df)
# print(a)

# b = df.iloc[1] = [80, 80]
# print(df)
# print(b)



# 세로
a = df['국어'] = [10, 20]
# df['국어'][1] = 80
print(df)
print(a)

b = df.columns[1]
c = df[b] = [30, 20]
print(df)
print(c)