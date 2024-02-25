from sklearn.model_selection import train_test_split
import Numpy_data_prepare as fd


# train_input, test_input, train_target, test_target = train_test_split(fd.fish_data, fd.fish_target, random_state=42)
# print(train_input.shape, test_input.shape)
# print(train_target.shape, test_target.shape)
# print(test_target)

train_input, test_input, train_target, test_target = train_test_split(fd.fish_data, fd.fish_target, stratify=fd.fish_target, random_state=42)
# print(test_target)

# stratify : 매개변수에 타깃 데이터를 전달하면 클래스 비율에 맞게 데이터를 나눔.(튜토리얼, 공부할 때만 쓰이고 실전에서는 거의 안 쓰임)

from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()
kn.fit(train_input, train_target)
# print(kn.score(train_input, train_target))

# print(kn.predict([[25,150]]))   # 예측한 값이 이상함.

import matplotlib.pyplot as plt
plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25, 150, marker='^')
plt.xlabel("length")
plt.ylabel("weight")
# plt.show()

distances, indexes = kn.kneighbors([[25,150]])

plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25, 150, marker='^')
plt.scatter(train_input[indexes,0], train_input[indexes,1], marker='D')
# plt.show()

# print(train_input[indexes])
# print(train_target[indexes])
# print(distances)