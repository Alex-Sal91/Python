class Account:

    def __init__(self, account_num, opening_deposit):
        self.account_num = account_num
        self.balance = opening_deposit

    def __str__(self):
        return  "{}".format(self.balance)

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount
            self.balance -= withdraw_amount
        else:
            return "Insufficient Funds"


