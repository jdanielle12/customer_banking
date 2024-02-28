from Account import Account

def create_savings_account(balance, interest_rate, months):
    savings_account = Account(balance, interest_rate)

    interest_earned = savings_account.balance * (interest_rate / 100) * (months / 12)

    updated_balance = savings_account.balance + interest_earned

    savings_account.set_balance(updated_balance)
    savings_account.set_interest(interest_earned)

    return updated_balance, interest_earned
