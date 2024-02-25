class BankAccount:
    next_account_number = 1

    def __init__(self, owner, balance=0):
        self.account_number = BankAccount.next_account_number
        self.owner = owner
        self.balance = balance
        BankAccount.next_account_number += 1

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}님의 계좌에 {amount}원이 입금되었습니다.")
        print(f"잔액 : {self.balance}")

    def withdraw(self, amount):
        if(amount <= self.balance):
            self.balance -= amount
            print(f"{self.owner}님의 계좌에서 {amount}원이 출금되었습니다.")
            print(f"잔액 : {self.balance}")
        else:
            print("잔액이 부족합니다.")

    def display_balance(self):
        print(f"{self.owner}님의 현재 잔액은 {self.balance}원입니다.")


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, owner, balance=0):
        account = BankAccount(owner, balance)
        self.accounts[account.account_number] = account
        return account
    
    def get_account(self, account_number):
        return self.accounts.get(account_number)
    
    def transfer(self, from_account, to_account_number, amount):
        from_account = self.get_account(to_account_number)
        to_account = self.get_account(to_account_number)
        if from_account and to_account:
            if from_account.balance >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"{amount}원을 송금했습니다.")
            else:
                print("잔액이 부족합니다.")
        else:
            print("계좌 번호가 잘못되었습니다.")

bank = Bank()

account1 = bank.add_account("James", 1000)
account2 = bank.add_account("Emma", 800)

account1.deposit(500)

account1.withdraw(200)

bank.transfer(account1.account_number, account2.account_number, 300)

account1.display_balance()
account2.display_balance()