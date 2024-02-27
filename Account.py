class Account:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        self.interest = interest
