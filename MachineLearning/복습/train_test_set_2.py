import fish_data_list
import market_fish_1


## 훈련 세트와 테스트 세트
train_input = market_fish_1.fish_data[:35]
train_target = market_fish_1.fish_target[:35]
test_input = market_fish_1.fish_data[35:]
test_target = market_fish_1.fish_target[35:]


## 테스트 세트에서 평가하기
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()
kn = kn.fit(train_input, train_target)
# print(kn.score(test_input, test_target))
## 훈련했을 때 사용한 데이터와 테스트했을 때 사용했던 데이터와 다름 -> 공정하게 평가를 했다
## 현재 당연히 정확도는 0이 나옴


## 샘플링 편향
## 한쪽으로 너무 치우친 것을 말함


## 넘파이 사용하가ㅣ
import numpy as np
input_arr = np.array(market_fish_1.fish_data)
target_arr = np.array(market_fish_1.fish_target)
# print(input_arr)
# print(input_arr.shape)


## 데이터 섞기
## 입력 데이터 특성값과 타겟값이 쌍으로 잘 따라서 섞이도록 만들어야 함
## 인덱스를 섞어서 만드는 방법 사용
np.random.seed(42)
index = np.arange(49)
## 0~48까지 1씩 증가하는 정수배열을 만듬->인덱스와 동일하게 사용할 수 있음
np.random.shuffle(index)
# print(index)
train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]
test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]


## 데이터 나누고 확인하기
# import matplotlib.pylab as plt
# plt.scatter(train_input[:, 0], train_input[:, 1])
# plt.scatter(test_input[:, 0], test_input[:, 1])
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()


## 두 번째 머신러닝 프로그램
kn = kn.fit(train_input, train_target)
# print(kn.score(test_input, test_target))