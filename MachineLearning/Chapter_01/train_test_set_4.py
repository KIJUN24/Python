import fish_data_list
import numpy as np

## 농어의 길이만 사용
import matplotlib.pyplot as plt
plt.scatter(fish_data_list.perch_length, fish_data_list.perch_weight)
## perch_weight:타깃
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


## 훈련 세트 준비
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(
    fish_data_list.perch_length, fish_data_list.perch_weight, random_state=42)
train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)