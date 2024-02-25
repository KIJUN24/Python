import matplotlib.pyplot as plt
import fish_data_list


## ***** bream과 smelt의 길이, 무게 그래프 그리기 *****
plt.scatter(fish_data_list.bream_length, fish_data_list.bream_weight)
plt.scatter(fish_data_list.smelt_length, fish_data_list.smelt_weight)
plt.xlabel('length')
plt.ylabel('weight')
# plt.show()


## ***** length와 weight에 두 물고기의 정보를 저장 후 리스트 안에 넣음 *****
length = fish_data_list.bream_length + fish_data_list.smelt_length
weight = fish_data_list.bream_weight + fish_data_list.smelt_weight
fish_data = [[l,w] for l, w in zip(length, weight)]
## 리스트 안에 for문이 있는 형식, length, weight를 묶고 끝날 때까지 반복함
# print(fish_data)


## ***** 정답 준비 *****
## [1]:bream   [0]:smelt (찾으려는 물고기를 '1'로 지정한다)
fish_target = [1]*35 + [0]*14
# print(fish_target)


# ***** k-최근접 이웃 *****
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()  
## 클래스의 인스턴스를 만든다 / 클래스의 객체를 만든다
## 클래스의 객체를 kn이라고 지정한다
kn.fit(fish_data, fish_target)
## fish_data와 fish_target 만든 두개의 데이터를 kn객체 fit메서드에 전달한다 -> 머신러닝 구현
## kn:머신러닝 모델이라고 부른다
## 훈련할 때는 fit메서드
# print(kn.score(fish_data, fish_target))
## 테스트할 때는 score 메서드 사용
## 얼마나 잘 학습했는지 확인


## 새로운 생선 예측
# plt.scatter(fish_data_list.bream_length, fish_data_list.bream_weight)
# plt.scatter(fish_data_list.smelt_length, fish_data_list.smelt_weight)
# plt.scatter(30, 600, marker='^')
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()
# print(kn.predict([[30, 600]]))
## 길이:30cm, 무게:600g 있다고 가정
## 결과:[1]->도미라고 정확하게 예측함
## 예측할 떄 predict사용
# print(kn._fit_X)
# print(kn._y)


## 무조건 도미
kn49 = KNeighborsClassifier(n_neighbors=49) # 참고 데이터를 49개로 한 kn49 모델
## 어떠한 데이터가 오더라도 도미로 예측함(전체적으로 도미가 더 많기 떄문)
kn49.fit(fish_data, fish_target)
# print(kn49.score(fish_data, fish_target))
# print(35/49)


# for n in range(5, 50):
#     # 최근접 이웃 개수 설정
#     kn.n_neighbors = n
#     # 점수 계산
#     score = kn.score(fish_data, fish_target)
#     # 100% 정확도에 미치지 못하는 이웃 개수 출력
#     if score < 1:
#         print(n, score)
#         break