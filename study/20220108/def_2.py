# # 매개변수 지정하여 호출하기
# def add(a, b):
#     return a+b

# result = add(a=3, b=7)
# print(result)



# # -- 입력 값이 몇 개가 될지 모를 때는 어떻게 해야 하는가?
# # 여러 개의 입력값을 받는 함수
# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result

# # result = add_many(1, 2, 3)
# # print(result)
# result = add_many()



# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result

# result = add_mul('add', 1,2,3,4,5)
# print(result)
# result = add_mul('mul', 1,2,3,4,5)
# print(result)



# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(a=1)
# print_kwargs(name = 'foo', age = 3)



# def add_and_mul_1(a1,b1):
#     return a1+b1, a1*b1
# result = add_and_mul_1(3,4)
# print(result)



# def say_nick(nick):
#     if nick == '바보':
#         return
#     print("나의 별명은 %s입니다." % nick)
#     print("나의 별명은 {0}입니다.".format(nick))

# # say_nick('야호')
# say_nick('바보')




# # 매개벼수에 초깃값 미리 설정하기
# def say_myself(name, old, man=True):
#     print("나의 이름은 {0}입니다.".format(name))
#     print("나의 이름은 %s입니다." % name)
#     print("나이는 {0}살입니다.".format(old))
#     print("나이는 %d살입니다." % old)
#     if(man):
#         print("남자입니다.")
#     else:
#         print("여자입니다.")
# say_myself("이기준", 22)
# say_myself("이기준", 22, True)
# say_myself("이기준", 22, False)


# # 순서 오류
# def say_myself(name, man=True, old):
#     print("나의 이름은 {0}입니다.".format(name))
#     print("나의 이름은 %s입니다." % name)
#     print("나이는 {0}살입니다.".format(old))
#     print("나이는 %d살입니다." % old)
#     if(man):
#         print("남자입니다.")
#     else:
#         print("여자입니다.")
# say_myself("이기준", 27)



# # vartest.py
# a = 1
# def vartest(a):
#     a = a + 1

# vartest(a)
# print(a)
# vartest(3)
# print(a)


# hello = 1
# def vartest(hello):
#     hello = hello + 1

# vartest(hello)
# print(hello)



# # vartest_return.py
# a = 1
# def vartest(a):
#     a = a + 1
#     return a

# a = vartest(a)
# print(a)



# # vartest_global.py
# a = 1
# def vartest():
#     global a
#     a = a + 1
# vartest()
# print(a)


# # lambda
# add = lambda a,b: a+b
# result = add(3, 4)
# print(result)

# # def : lambda = add
# def add(a,b):
#     return a+b
# result = add(3, 4)
# print(result)