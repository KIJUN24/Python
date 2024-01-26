# shuffle 활용 예제
# from random import *
# lst = [1, 2, 3, 4, 5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

from random import *
print("-- 당첨자 발표 --")
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lst = range(1, 21) # 1부터 20까지 숫자 생성
print(type(lst))
lst = list(lst)
print(type(lst))
shuffle(lst)
print(lst)
# print("치킨 당첨자 : " + str(sample(lst, 1)))
# print("커피 당첨자 : " + str(sample(lst, 3)))

winner = sample(lst, 4)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winner[0]))
print("커피 당첨자 : {0}".format(winner[1:]))
print(" -- 축하드립니다! -- ")