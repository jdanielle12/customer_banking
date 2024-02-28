from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter savings account balance: "))
    savings_interest = float(input("Enter savings account interest rate (%): "))
    savings_maturity = int(input("Enter savings account maturity: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Savings account interest earned: {interest_earned:.2f}")
    print(f"Updated savings account balance: {updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Enter CD account balance: "))
    cd_interest = float(input(f"Enter CD account interest rate (%): "))
    cd_maturity = int(input("Enter CD account maturity: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"CD account interest earned: {cd_balance:.2f}")
    print(f"Updated CD account balance: {updated_cd_balance:.2f}")

if __name__ == "__main__":
    main()