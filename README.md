# customer_banking

This is a simple Python application for managing savings and CD(Certificate of Deposit) accounts for customers. It allows users to input account details such as balance, interest rate, and duration, and then calculates the interest earned and updates the account balance accordingly. 

## Installation

### Requirements
* Python3.x

## Instructions

1. Clone the repository:
https://github.com/jdanielle12/customer_banking.git

2. Navigate to the project directory:
cd customer_banking

3. Run the main Python file:
python3 customer_banking.py

4. Follow the prompts to input savings and CD account details.

## Usage 

* The `customer_banking.py` file is the main en try point of the application. Run this file to interact with the banking application. 
* Follow the on-screen prompts to input account details such as balance, interest rate, and duration. 
* The application will calculat ethe interest earned and display the updated account balances.

## Files  

* `customer_banking.py`: Main file where user interations are handled.
* `savings_account.py`: Contains the `create_savings_account` function to handle savings account operations. 
* `cd_account.py`: Contains the `create_cd_account` function to hande CD account operations.
* `Account.py`: Defines the `Account` class with methods to set the balance and interest. 

## Functionality

* The `create_savings_account` function calculates interest earned for a savings account based on user input.
* The `create_cd_account` function calculates interest earned for a CD account based on user input.
* The `Account` class provides methods to set the balance and interest for an account. 