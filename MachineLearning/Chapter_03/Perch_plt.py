import Perch_data as pd
import matplotlib.pyplot as plt

plt.scatter(pd.perch_length, pd.perch_weight)
plt.xlabel('length')
plt.ylabel('weight')
# plt.show()



from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(
    pd.perch_length, pd.perch_weight, random_state=42)

test_array = pd.np.array([1,2,3,4])
# print(test_array.shape)   # test_array의 배열이 4인 것을 확인

test_array = test_array.reshape(2,2)    # (2,2) 크기로 바꿈.
# print(test_array.shape)

train_input = train_input.reshape(-1,1)
test_input = test_input.reshape(-1,1)
# print(train_input.shape, test_input.shape)