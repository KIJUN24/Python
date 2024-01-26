# # len len(s)는 입력 값 s의 길이(요소의 전체 개수)를 돌려주는 함수이다.
# print(len("python"))
# print(len([1,2,3]))
# print(len((2,1, 'a')))



# # list 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수.
# # list 함수에 리스트를 입력으로 주면 똑같은 리스트를 복사하여 돌려준다.
# print(list('python'))
# print(list((1,2,3)))

# a = [1,2,3]
# print(a)
# b = list(a)
# print(b)



# # map map(f, iterable)은 함수 f와 반복가능한 iterable 자료형을 입력으로 받는다.
# # map은 입력 받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수.
# def two_tiems(numberList):
#     result = []
#     for number in numberList:
#         result.append(number*2)
#     return result

# result = two_tiems([1,2,3,4])
# print(result)


# def two_times(x):
#     return x*2
# a = list(map(two_times, [1,2,3,4]))
# print(a)

# a = list(map(lambda a : a*2, [1,2,3,4]))
# print(a)