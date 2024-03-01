import numpy as np
import perch_train_test_div as perchdata
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

train_poly = np.column_stack((perchdata.train_input ** 2, perchdata.train_input))
test_poly = np.column_stack((perchdata.test_input ** 2, perchdata.test_input))
# print(train_poly.shape, test_poly.shape)

lr = LinearRegression()
lr.fit(train_poly, perchdata.train_target)
# 목표하는 값은 어떤 그래프를 훈련하든지 바꿀 필요가 없다.
# 50cm 농어에 대해 무게를 예측하기 위해 길이의 제곱과 원래 길이를 함께 넣어줘야 한다.
# print(lr.predict([[50**2, 50]]))

# print(lr.coef_, lr.intercept_)  # 기울기와 y절편

# P.141
# 구간별 직선을 그리기 위해 15에서 49까지 정수 배열을 만든다.
# 곡선을 그리기 위해 직선을 쪼개서 그려야 하므로 15에서 49까지 1개 단위로 끊어 배열을 만든다.
point = np.arange(15, 50)

# 훈련 세트의 산점도를 그립니다.
# plt.scatter(perchdata.train_input, perchdata.train_target)

# 15에서 49까지 2차 방정식 그래프를 그립니다.
plt.plot(point, 1.01*point**2 - 21.6*point, + 116.05)

# 50cm 농어 데이터
# plt.scatter(50, 1574, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
# plt.show()

print(lr.score(train_poly, perchdata.train_target))
print(lr.score(test_poly, perchdata.test_target))
# 테스트 점수가 조금 더 높기에 과소적합이 아직 남아있다.
# 조금 더 복잡한 모델이 필요하다.