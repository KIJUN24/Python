# 클래스
# 메서드들을 하나로 묶어 관리하는 방법
# 코드의 재사용성을 높이고, 코드의 구조를 더욱 명확하게 만들 수 있다.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"이름 : {self.name}, 나이 : {self.age}")

# 클래서 인스턴스(객체) 생성
person1 = Person("John", 30)
person2 = Person("Emma", 25)

# 메서드 호출
# person1.print_info()
# person2.print_info()



class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print(f"{self.owner}님 계좌가 개설되었습니다.\n")

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}님의 계좌에는 {amount}원이 입금되었습니다")
        print(f"잔액 : {self.balance}원.")
        print("\n")
    
    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
            print(f"{self.owner}님의 계좌에서 {amount}원이 출금되었습니다.")
            print(f"잔액 : {self.balance}원.")
            print("\n")
        else:
            print("잔액이 부족합니다.")
            print("\n")

    def display_balance(self):
        print(f"{self.owner}님의 현재 잔액은 {self.balance}원입니다.")

account1 = BankAccount("James", 1000)
account1.deposit(300)
account1.withdraw(800)
account1.display_balance()