class Account:
    def __init__(self,bank_Account,bank_balance):
        self.bank_Account=bank_Account
        self.bank_balance=bank_balance
        print(f"Your bank account number is {self.bank_Account} and bank balance is {self.bank_balance}")

    def credit(self,amount):
        self.bank_balance=self.bank_balance+amount
        print(f"{amount} was credited in your account {self.bank_Account}")
        print(f"your new bank balance is {self.bank_balance}")

    def debit(self,amount):
        self.bank_balance=self.bank_balance-amount
        print(f"{amount} was debited from  your account {self.bank_Account}")
        print(f"your new bank balance is {self.bank_balance}")

    def print_balance(self):
        print(f"Your bank balance is {self.bank_balance}")

Account1=Account("AB01",1000)
Account1.debit(10)