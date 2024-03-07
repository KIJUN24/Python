from sklearn.linear_model import Ridge
from Regularization import *
import numpy as np

ridge = Ridge()
ridge.fit(train_scaled, train_target)
# print(ridge.score(train_scaled, train_target))
# print(ridge.score(test_scaled, test_target))

# 훈련 세트에 잘 맞던 것을 억지로 막아서 테스트 세트에서도 높은 점수를 나오게끔 함.
# 가중치의 제곱을 벌칙으로 사용한다.
# L2규제

import matplotlib.pyplot as plt

train_score = []
test_score = []

alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
for alpha in alpha_list:
    # 릿지 모델을 만든다.
    ridge = Ridge(alpha=alpha)
    # 릿지 모델을 훈련한다
    ridge.fit(train_scaled, train_target)
    # 훈련 점수와 테스트 점수를 저장한다.
    train_score.append(ridge.score(train_scaled, train_target))
    test_score.append(ridge.score(test_scaled, test_target))

# 그래프 그리기

# plt.plot(np.log10(alpha_list), train_score)
# plt.plot(np.log10(alpha_list), test_score)
plt.xlabel('alpha')
plt.ylabel('R^2')
# plt.show()

ridge = Ridge(alpha=0.1)
ridge.fit(train_scaled, train_target)

# print(ridge.score(train_scaled, train_target))
# print(ridge.score(test_scaled, test_target))