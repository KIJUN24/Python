# class Fourcal():
#     def setdata(self, First, Second):
#         self.first = First
#         self.second = Second

#     def add(self):
#         result = self.first + self.second
#         return result

#     def sub(self):
#         result = self.first - self.second
#         return result

#     def mul(self):
#         result = self.first * self.second
#         return result

#     def div(self):
#         result = self.first / self.second
#         return result


# a = Fourcal()
# a.setdata(3, 6)
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())

# print(type(a))


# class Fourcal():
#     def __init__(self, First, Second):
#         self.first = First
#         self.second = Second

#     def setdata(self, First, Second):
#         self.first = First
#         self.second = Second

#     def add(self):
#         result = self.first + self.second
#         return result

#     def sub(self):
#         result = self.first - self.second
#         return result

#     def mul(self):
#         result = self.first * self.second
#         return result

#     def div(self):
#         result = self.first / self.second
#         return result


# a = Fourcal(3,6)
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())




class Fourcal():
    def __init__(self):
        self.first = int(input("첫 번째 숫자 입력 : "))
        self.second = int(input("두 번째 숫자 입력 : "))

    # def setdata(self, First, Second):
    #     self.first = First
    #     self.second = Second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


# a = Fourcal()
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())


# class MoreFourCal(Fourcal):
#     pass









# a = MoreFourCal()
# print(a.add())



class MoreFourCal(Fourcal):
    def pow(self):
        result = self.first ** self.second
        return result

# a = MoreFourCal()
# print(a.pow())


class SafeMoreFourCal(MoreFourCal):
    def safe_div(self):
        if(self.second == 0):
            return 0
        else:
            return self.first / self.second


a = SafeMoreFourCal()
print(a.safe_div())