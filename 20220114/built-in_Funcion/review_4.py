# # id 객체를 입력받아 객체의 고유 주소 값(레퍼런스)를 돌려주는 함수.
# a = 3
# b = a
# print(id(a), id(3), id(b))


# # input([prompt]) 사용자 입력을 받는 함수.
# # 매개변수로 문자열을 주면 그 문자열은 프롬포트가 됨.
# a = input()
# print(a)
# b = input("Enter : ")


# # int 문자열 형태의 숫자나 소수점이 있는 숫자를 정수 형태로 돌려주는 함수
# print(int('3'))
# print(int(3.2))
# print(int("11", 2))
# print(int('1A', 16))



# # isinstance 첫 번째 인수 : 인스턴스  //  두 번째 인수 : 클래스 이름.
# # 입력으로 받은 인스턴스가 클래스의 인스턴스인지 판단
# # 참이면 True, 거짓이면 Flase
# class Person:
#     pass
# a = Person()
# print(isinstance(a, Person))
# b = 3
# print(isinstance(b, Person))