from sklearn.neighbors import KNeighborsRegressor
import Perch_plt as pp

knr = KNeighborsRegressor()

# K-최근접 이웃 회귀 모델을 훈련한다.
knr.fit(pp.train_input, pp.train_target)

# print(knr.score(pp.test_input, pp.test_target))




from sklearn.metrics import mean_absolute_error

# 테스트 세트에 대한 예측을 만듭니다.
test_prediction = knr.predict(pp.test_input)

# 테스트 세트에 대한 평균 절댓값 오차를 계산합니다.
mae = mean_absolute_error(pp.test_target, test_prediction)
# print(mae)