class JSS():
    def __init__(self):
        print("JSS class 선언!")
        self.name = input("이름 : ")
        self.age = input("나이 : ")

    def show(self):
        print("show 실행!")
        print("나의 이름은 {0}, 나이는 {1}세입니다.".format(self.name, self.age))

# a = JSS()
# a.show()
# a.name
# a.age

class JSS2(JSS):
    def __init__(self):
        super().__init__() # self.name, self.age 가져옴
        self.gender = input("성별 : ")

    def show(self):
        print("나의 이름은 {0}, 성별은 {2}자, 나이는 {1}세입니다.".format(self.name, self.age, self.gender))
        
a = JSS2()
a.show()