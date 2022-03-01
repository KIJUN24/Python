# # abs 절댓값
# a = abs(3)
# print(a)

# print(abs(-4))


# # all 반복 가능한 자료형 x를 입력 인수로 받으며 이 x의 요소가 모두 참이면  True, 거짓이 하나라도 있으면 False를 돌려준다.
# a = all([1, 2, 3])
# print(a)
# b = all([1, 2, 3, 0])
# print(b)
# print(all([]))


# any 반복 가능한 자료형 x를 입력 인수로 받으며 x의 요소 중 하나라도 있으면 True x가 모두 거짓일 때 False
#     all과 반대
a = any([1, 2, 3, 0])
print(a)
print(any([0,""]))