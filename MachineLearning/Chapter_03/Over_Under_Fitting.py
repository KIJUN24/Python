import Perch_plt as pp
import CoefficientOfDetermination as cod
from sklearn.neighbors import KNeighborsRegressor

# print(cod.knr.score(pp.train_input, pp.train_target))

# 이웃의 개수를 줄임으로서 모델을 조금 더 복잡하게 만듦.
# 이웃의 개수를 3으로 설정.
cod.knr.n_neighbors = 3

# 모델을 다시 훈련함.
cod.knr.fit(pp.train_input, pp.train_target)
print(cod.knr.score(pp.train_input, pp.train_target))
print(cod.knr.score(pp.test_input, pp.test_target))