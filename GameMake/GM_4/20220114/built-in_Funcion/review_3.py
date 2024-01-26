# enumerate 열거하다. 순서가 있는 자료형을 입력으로 받아 인데스 값을 포함하는 enumerate 객체를 돌려줌.
# 순서가 있는 자료형 : 리스트, 튜플, 문자열
# enumerate 함수는 랙문과 함께 자주 사용
# for i, name in enumerate(['body', 'foo', 'bar']):
#     print(i, name)


# # eval expression은 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결괏값으로 돌려주는 함수.
# a = eval('1+2')
# print(a, type(a))
# b = eval(" 'hi' + 'a' ")
# print(b, type(b))
# c = eval("divmod(5, 2)")
# print(c, type(c))


# filter 걸러낸다는 뜻. 첫 번째 인수 : 함수 이름  //  두 번째 인수 : 함수에 차례로 들어갈 반복 가능한 자료형
# 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 겂이 참인 것만 묶어서, 걸러 내서 돌려줌.
# def positive(l):
#     result = []
#     for i in l:
#         if i > 0:
#             result.append(i)
#     return result
# print(positive([1, -3, 2, 0, -5, 6]))

# def positive(x):
#     return x > 0
# print(list(filter(positive, [1, -3, 2, 0, -5, 6])))


# # hex 정수 값을 입력받아 16진수로 변환하여 돌려주는 함수.
# print(hex(234))
# print(hex(3))