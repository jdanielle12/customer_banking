from Account import Account

def create_cd_account(balance, interest_rate, months):
    cd_account = Account(balance, interest_rate)
    
    interest_earned = balance * (interest_rate / 100) * (months / 12)
    
    updated_balance = balance + interest_earned
    
    cd_account.set_balance(updated_balance)
    cd_account.set_interest(interest_earned)
    
    return "{:,.2f}".format(updated_balance), "{:,.2f}".format(interest_earned)
