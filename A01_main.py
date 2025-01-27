""""
Description: A client program written to verify correctness of 
the BankAccount and Client classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Sahil Choudhary"

from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """Test the methods and functionality of the BankAccount and Client classes."""
    
    # Ensure that any statement which may raise an exception is properly handled
    # and display the exception message when caught.
    
    # 1. Create a valid Client instance with unique, valid input values.
    try:
        client = Client(10, "Sahil", "Choudhary", "cholamola@academic.rrc.ca")
    except ValueError as error:
        print("ERROR:", error)
    
    # 2. Declare a BankAccount instance with initial values set to None.
    try:
        bank_account = BankAccount(None, None, None)
    except ValueError as error:
        print("ERROR:", error)    
    
    # 3. Create a valid BankAccount instance using valid values, 
    # including the client_number from the client created in step 1, 
    # an account number, and a floating-point balance.
    try:
        valid_bank_account = BankAccount(350, client.client_number, 350.00)
    except ValueError as error:
        print("error:", error)
    
    # 4. Attempt to create a BankAccount with an invalid balance (non-float).
    try:
        invalid_bank_account = BankAccount(350, client.client_number, "twenty")
    except ValueError as error:
        print("error:", error)
    
    # 5. Print the Client instance and the BankAccount instance created in step 3.
    print(str(client))
    print(str(valid_bank_account))

    # 6. Try to deposit a non-numeric value into the valid BankAccount instance.
    try:
        valid_bank_account.deposit("three hundred fifty")
    except ValueError as error:
        print("error:", error)

    # 7. Try to deposit a negative value into the valid BankAccount instance.
    try:
        valid_bank_account.deposit(-100)
    except ValueError as error:
        print("error:", error)
    
    # 8. Try to withdraw a valid amount from the valid BankAccount instance.
    try:
        valid_bank_account.withdraw(50)
    except ValueError as error:
        print("error:", error)

    # 9. Try to withdraw a non-numeric value from the valid BankAccount instance.
    try:
        valid_bank_account.withdraw("twenty")
    except ValueError as error:
        print("error:", error)

    # 10. Try to withdraw a negative value from the valid BankAccount instance.
    try:
        valid_bank_account.withdraw(-30)
    except ValueError as error:
        print("error:", error)

    # 11. Try to withdraw an amount exceeding the current balance of the valid BankAccount instance.
    try:
        valid_bank_account.withdraw(6490)
    except ValueError as error:
        print("error:", error)

    # 12. Print the current status of the BankAccount instance created in step 3.
    print(str(valid_bank_account))
    

if __name__ == "__main__":
    main()
