import matplotlib.pyplot as plt
import MachineLearning.Chapter_01.fish_data_list as fdl


# # 공부) 1
# plt.scatter(fdl.bream_length, fdl.bream_weight)
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()



# # 공부) 2
# plt.scatter(fdl.bream_length, fdl.bream_weight)
# plt.scatter(fdl.smelt_length, fdl.smelt_weight)
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()



# 공부) 3
length = fdl.bream_length + fdl.smelt_length
weight = fdl.bream_weight + fdl.smelt_weight
fish_data = [[l, w] for l, w in zip(length, weight)]
# print(fish_data)

fish_target = [1]*35 + [0]*14
# print(fish_target)
# 찾으려는 대상을 1로 놓고 그 외에는 0으로 놓는다.
# 위 예제는 도미를 찾는 대상으로 정의했기 때문에 도미를 1로 설정.



# 공부) 4
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()
fish_training = kn.fit(fish_data, fish_target)      # fit() 메서드 : 주어진 데이터로 알고리즘을 훈련한다.
# print(fith_training)
fish_accuracy = kn.score(fish_data, fish_target)
# print(fish_accuracy)



# 공부) 5
# plt.scatter(fdl.bream_length, fdl.bream_weight)
# plt.scatter(fdl.smelt_length, fdl.smelt_weight)
# plt.scatter(30, 600, marker='^')
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

fish_pre = kn.predict([[30, 600]])  # predict() : 새로운 데이터의 정답을 예측한다.
# print(fish_pre)

# print(kn._fit_X)    # fish_data
# print(kn._y)        # fish_target

kn49 = KNeighborsClassifier(n_neighbors=49)     # 참고 데이터를 49개로 한 kn49 모델
kn49_training = kn49.fit(fish_data, fish_target)
kn49_accuracy = kn49.score(fish_data, fish_target)
print(kn49_accuracy)
print(35/49)