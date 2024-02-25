# P.97 - 101

import SklearnSetDiv as sd
import matplotlib.pyplot as plt
import numpy as np

plt.scatter(sd.train_input[:,0], sd.train_input[:,1])
plt.scatter(25, 150, marker='^')
plt.scatter(sd.train_input[sd.indexes,0], sd.train_input[sd.indexes,1], marker='D')
plt.xlim((0, 1000))
plt.xlabel('length')
plt.ylabel('weight')
# plt.show()

mean = np.mean(sd.train_input, axis=0)  # 평균 계산
std = np.std(sd.train_input, axis=0)    # 표준편차 계산
# sd.train_input : (36,2) 크기의 배열
# 특성마다 값의 스케일이 다르므로 평균과 표준편차는 각 특성별로 계산해야 한다.
# 위 글 : axis=0를 한 이유
print(mean, std)
# 각 특성마다 평균과 표준편차가 구해짐

# 표준점수 = (원본 데이터 - 평균) / 표준편차
train_scaled = (sd.train_input - mean) / std
# '브로드캐스팅'으로 인해 모든 행에서 mean에 있는 두 평균값을 빼준다.
# 표준편차도 마찬가지로 모든 행에 적용한다.
# P.101