class JSS:
    def __init__(self):
        self.name = input("이름 : ")
        self.age = input('나이 : ')

    def show(self):
        print("이름은 {}입니다. 나이는 {}세입니다.".format(self.name, self.age))


# # 실행
# a = JSS()
# print(a.name)
# print(a.age)
# a.show() 

class JSS2(JSS):
    def __init__(self):
        super().__init__()
        self.gender = input('성별 : ')

    def show(self):
        print("이름은 {}입니다. 나이는 {}세이며 성별은 {}입니다.".format(self.name, self.age, self.gender))


# # 실행
# a = JSS2()
# a.show()