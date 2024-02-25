import fish_data_list as fdl

# 공부) 1 : 훈련 세트와 테스트 세트
fish_data = [[l, w] for l, w in zip(fdl.fish_length, fdl.fish_weight)]
fish_target = [1]*35 + [0]*14

from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()

# print(fish_data[4])
# print(fish_data[0:5])
# print(fish_data[:5])    # 위 코드와 동일
# print(fish_data[44:])

train_input = fish_data[:35]
train_target = fish_target[:35]
test_input = fish_data[35:]
test_target = fish_target[35:]


kn_fit = kn.fit(train_input, train_target)
kn_score = kn.score(test_input, test_target)
# print(kn_score)
