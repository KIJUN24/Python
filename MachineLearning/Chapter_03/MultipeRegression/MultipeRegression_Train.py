# P.156

from sklearn.linear_model import LinearRegression
from Perch_data import *
from Transformer import *

lr = LinearRegression()
lr.fit(train_poly, train_target)
# print(lr.score(train_poly, train_target))
# print(lr.score(test_poly, test_target))


poly = PolynomialFeatures(degree=5, include_bias=False)
# 1의 값을 빼주기 위해 False를 해준다.
poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)
# print(train_poly.shape)

lr.fit(train_poly, train_target)
# print(lr.score(train_poly, train_target))

# print(lr.score(test_poly, test_target))
# 값이 음수가 나왔음.
# 특성의 개수를 크게 늘리면 선형 모델은 아주 강력해진다.
# 하지만 이런 모델은 훈련 세트에 너무 과대적합되므로 테스트 세트에서 형편없는 점수를 만든다.