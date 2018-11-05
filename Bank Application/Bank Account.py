class Account:

    def __init__(self, account_num, opening_deposit):
        self.account_num = account_num
        self.balance = opening_deposit

    def __str__(self):
        return  "{}".format(self.balance)

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
        else:
            return 'Insufficient Funds'

class Current(Account):
    def __int__(self, account_num, opening_deposit):

        super(account_num, opening_deposit).__init__()

    #Define a __str__ method that returns a string specific to Current accounts
    def __str__(self):
        return 'Current Account: {}\n Balance: {}'.format(self.account_num, Account.__str__(self))


x = Current(44556, 17556)
print(x)


print(x.withdraw(15000))
print(x.balance)

class Savings(Account):
    def __int__(self, account_num, opening_deposit):

        super(account_num, opening_deposit).__init__()

    def __str__(self):
        return 'Savings Account: {}\n Balance: {}'.format(self.account_num, Account.__str__(self))


class Business(Account):
    def __int__(self, account_num, opening_deposit):

        super(account_num, opening_deposit).__init__()

    def __str__(self):
        return 'Business Account: {}\n Balance: {}'.format(self.account_num, Account.__str__(self))