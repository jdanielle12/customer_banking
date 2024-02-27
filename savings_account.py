from Account import Account

def create_savings_account(balance, interest_rate, months):
    savings_account = Account(balance, interest_rate)

    interest_earned = savings_account.get_balance() * (interest_rate / 100)

    updated_balance = savings_account.get_balance() + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    # Return the updated balance and interest earned.
    return  # ADD YOUR CODE HERE
