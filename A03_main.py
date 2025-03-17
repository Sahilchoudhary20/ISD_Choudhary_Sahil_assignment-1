"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Sahil Choudhary"


# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import *
from datetime import date, timedelta
from client.client import Client


# 2. Create a Client object with data of your choice.
instance1 = Client(200, 'Sahil', 'Choudhary', 'schoudhary4@academic.rrc.ca')


# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.

instance2 = ChequingAccount(10000, 200, 30000, date(2014, 4, 15), -20, 0.06)
instance3 = SavingsAccount(200, 200, 20000, date(2014, 5, 13), 6)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).

instance2.attach(instance1)
instance3.attach(instance1)


# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.

client2 = Client(200, 'Tejpreet', 'Kaur', 'blehh@academic.rrc.ca')
sample4 = SavingsAccount(3000, 200, 35000, date(2011, 7, 25), 3)
sample4.attach(client2)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.


try:
    instance2.deposit(500)
    print("Deposit successful. New Balance:", instance2.balance)

    instance2.withdraw(1000)
    print("Withdrawal successful. New Balance:", instance2.balance)

    instance2.withdraw(35000)

except ValueError as e:
    print(f"Error during transaction on ChequingAccount: {e}")


try:
    instance3.deposit(1000)
    print("Deposit successful. New Balance:", instance3.balance)

    instance3.withdraw(2000)
    print("Withdrawal successful. New Balance:", instance3.balance)

    instance3.withdraw(30000)

except ValueError as e:
    print(f"Error during transaction on SavingsAccount: {e}")


try:
    sample4.deposit(2000)
    print("Deposit successful. New Balance:", sample4.balance)

    sample4.withdraw(5000)
    print("Withdrawal successful. New Balance:", sample4.balance)

    sample4.withdraw(40000)

except ValueError as e:
    print(f"Error during transaction on client2's SavingsAccount: {e}")