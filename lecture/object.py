class Account:
    interest_rate = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.deposit(400)

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            return 'Insufficient Funds'
        else:
            self.balance -= amount
            return self.balance


# inheretence happened when a class came from a base class
# self bound to the instance that created by calling class
class smurf_account(Account):
    interest_rate = 0.01
    withdraw_fee = 1

    def withdraw(self, amount):
        return Account.withdraw(self, amount+self.withdraw_fee)


class Bank:
    """A bank *has* accounts.
    >>> bank = Bank()
    >>> john = bank.open_account('John',10)
    >>> jack = bank.open_account('Jack',5,smurf_account)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    """

    def __init__(self):
        self.accounts = []

    # there could be different types of account
    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)  # add opened account to list of accounts
        return account

    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance*a.interest)

    def too_big_to_fail(self):
        return len(self.accounts) > 1
