import pandas as pd

# col = ['A', 'B', 'C']
# ind = [1,2,3]
# con = [[0,0,0], [0,0,0], [0,0,0]]
# a = pd.DataFrame(con, columns=col, index=ind)
# print(a)

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


a = df_maker(10, 10, "blank")
print(a)