import numpy as np
import TrainSet_TestSet as ts

input_arr = np.array(ts.fish_data)
target_arr = np.array(ts.fish_target)
# print(input_arr)
# print(input_arr.shape)

np.random.seed(42)
index = np.arange(49)
np.random.shuffle(index)
# print(index)
# print(input_arr[[1,3]])   # 배열 인덱싱 : 여러 개의 인덱스로 한 번에 여러 개의 원소를 선택할 수 있다.

train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]
# print(input_arr[13], train_input[0])
test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]


#############################################################################


import matplotlib.pyplot as plt
plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(test_input[:,0], test_input[:,1])
plt.xlabel('length')
plt.ylabel('weight')
# plt.show()


from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()

second_kn_fit = kn.fit(train_input, train_target)
second_kn_score = kn.score(test_input, test_target)
# print(Second_kn_score)
second_kn_pre = kn.predict(test_input)
print(second_kn_pre)
print(test_target)