# P. 131

import Perch_data as pd
from sklearn.model_selection import train_test_split

# 훈련 세트와 테스트 세트로 나눕니다.
train_input, test_input, train_target, test_target = train_test_split(pd.perch_length, pd.perch_weight, random_state=42)

# 훈련 세트와 테스트 세트를 2차원 배열로 바꿉니다.
train_input = train_input.reshape(-1,1)
test_input = test_input.reshape(-1,1)

from sklearn.neighbors import KNeighborsRegressor

knr = KNeighborsRegressor(n_neighbors=3)

# k-최근접 이웃 회귀 모델을 훈련합니다.
knr.fit(train_input, train_target)
# print(knr.predict([[50]]))


import matplotlib.pyplot as plt

# 50cm 농어의 이웃을 구합니다.
# distances, indexes  = knr.kneighbors([[50]])
# print(distances)
# print(indexes)


# # 훈련 세트의 산점도를 그립니다.
# plt.scatter(train_input, train_target)

# # 훈련 세트 중에서 이웃 샘플만 다시 그립니다.
# plt.scatter(train_input[indexes], train_target[indexes], marker='D')

# # 50cm 농어 데이터
# plt.scatter(50, 1033, marker='^')
# plt.xlabel('length')
# plt.ylabel('weight')
# # plt.show()

# import numpy as np

# print(np.mean(train_target[indexes]))

# print(knr.predict([[100]]))

# 100cm 농어의 이웃을 구합니다.
# distances, indexes = knr.kneighbors([[100]])
# print(indexes)

# 훈련 세트의 산점도를 그립니다.
# plt.scatter(train_input, train_target)

# 훈련 세트 중에서 이웃 샘플만 다시 그립니다.
# plt.scatter(train_input[indexes], train_target[indexes], marker='D')

# 100cm 농어 데이터
# plt.scatter(100, 1033, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
# plt.show()

# P. 134