class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    # Public methods to access private attributes
    def get_account_number(self):
        return self.__account_number
    

    @staticmethod
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Withdrawal amount is invalid or exceeds the balance.")

# Create a BankAccount object
account = BankAccount("12345", 1000)

# Access and modify private attributes through public methods
print("Account Number:", account.get_account_number())
print("Initial Balance:", account.get_balance())

account.deposit(500)
print("After Deposit:", account.get_balance())

account.withdraw(300)
print("After Withdrawal:", account.get_balance())
