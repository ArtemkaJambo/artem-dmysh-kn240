# інкапсуляція
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  
        self.__balance = balance  

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance

account = BankAccount("Artem", 1000)
account.deposit(500)
print(account.get_balance())  # 1500