from sklearn.linear_model import LinearRegression
import perch_train_test_div as PerchData
lr = LinearRegression()

# 선형 회귀 모델을 훈련합니다.
lr.fit(PerchData.train_input, PerchData.train_target)

# 50cm 농어에 대해 예측합니다.
# print(lr.predict([[50]]))

# print(lr.coef_, lr.intercept_)

# P.137
import matplotlib.pyplot as plt

# 훈련 세트의 산점도를 그립니다
plt.scatter(PerchData.train_input, PerchData.train_target)

# 15에서 50까지 1차 방정식 그래프를 그립니다
plt.plot([15, 50], [15*lr.coef_+lr.intercept_, 50*lr.coef_+lr.intercept_])

# 50cm 농어 데이터
plt.scatter(50, 1241.8, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
# plt.show()

print(lr.score(PerchData.train_input, PerchData.train_target))
print(lr.score(PerchData.test_input, PerchData.test_target))