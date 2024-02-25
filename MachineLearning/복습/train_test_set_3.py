import fish_data_list
import train_test_set_2
import numpy as np

## 넘파이로 데이터 준비
fish_data = np.column_stack((fish_data_list.fish_length, fish_data_list.fish_weight))
# print(fish_data)
fish_target = np.concatenate((np.ones(35), np.zeros(14)))
# print(fish_target)


## 사이킷런으로 데이터 나누기
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(
    fish_data, fish_target, stratify=fish_target, random_state=42)
## random_state:실전에서는 사용할 일 거의 없음


## 수상한 도미
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()
kn.fit(train_input, train_target)
# print(kn.score(test_input, test_target))

# print(kn.predict([[25, 150]]))

distances, indexes = kn.kneighbors([[25, 150]])

import matplotlib.pylab as plt
# plt.scatter(train_input[:,0], train_input[:,1])
# plt.scatter(25, 150, marker='^')
# plt.scatter(train_input[indexes,0], train_input[indexes,1], marker='D')
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()


## 기준을 맞춰라
# plt.scatter(train_input[:,0], train_input[:,1])
# plt.scatter(25, 150, marker='^')
# plt.scatter(train_input[indexes,0], train_input[indexes,1], marker='D')
# plt.xlim((0, 1000))
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()


## 표준 점수로 바꾸기
mean = np.mean(train_input, axis=0)
std = np.std(train_input, axis=0)
## mean:평균  std:표준편차  axis=0->행을 따라 계산함
# print(mean, std)
train_scaled = (train_input - mean) / std


## 수상한 도미 다시 표시하기
new = ([25, 150] - mean) / std
# plt.scatter(train_scaled[:,0], train_scaled[:,1])
# plt.scatter(new[0], new[1], marker='^')
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()


## 전처리 데이터에서 모델 훈련
kn.fit(train_scaled, train_target)
test_scaled = (test_input - mean) / std
# print(kn.score(test_scaled, test_target))
# print(kn.predict([new]))
distances, indexes = kn.kneighbors([new])
plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(new[0], new[1], marker='^')
plt.scatter(train_scaled[indexes,0], train_scaled[indexes,1], marker='D')
plt.xlabel('length')
plt.ylabel('weight')
# plt.show()