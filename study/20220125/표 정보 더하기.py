import pandas as pd

df = pd.DataFrame({'x' : [1, 2, 3, 4, 5]
, 'y' : [10, 20, 30, 40, 50]
, 'z' : [100, 200, 300, 400, 500]})

print("DataFrame : ")
print(df)

# sums = df.sum(axis = 1)
# print(sums)

# sums = df.sum()
# # print("Column-wise Sun : ")
# print(sums)

sum_3 = df.iloc[[3]].sum(axis=1)
print("Sum of value od 3rd Row: ")
print(sum_3)

# df = pd.DataFrame({'x' : [1, 2, 3, 4, None], 'y' : [10, None, 30, 40, 50], 'z' : [100, 200, 300, 400, 500]})

# print("DataFrame : ")
# print(df)

# sums = df.sum()


# print("Column-wise Sum : ")
# print(sums)