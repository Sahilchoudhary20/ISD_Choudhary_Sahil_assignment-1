"""
Description: This file contains the definition of the SavingsAccount class, 
which is used to manage the records of savings bank accounts.

"""

__author__ = "Sahil Choudhary"
__version__ = "1.0.0"
__credits__ = "Sahil Choudhary"

from bank_account.bank_account import BankAccount
from datetime import date

class SavingsAccount(BankAccount):
    """
    The SavingsAccount class is responsible for managing the savings accounts of clients.
    """

    SERVICE_CHARGE_PREMIUM: float = 2.0  

    def __init__(self, account_number: int, client_number: int, balance: float,
                date_created: date, minimum_balance: float) -> None:
        """
        Initializes the SavingsAccount with the given parameters.

        Args:
            account_number (int): The unique identifier for the bank account.
            client_number (int): The client’s unique identifier associated with the account.
            balance (float): The current balance in the account.
            date_created (date): The date when the account was opened.
            minimum_balance (float): The minimum balance required to avoid additional service charges.

        Returns:
            None

        Raises:
            ValueError: If the account_number or client_number cannot be interpreted as integers.
            ValueError: If the balance cannot be interpreted as a float.
        
        """
        super().__init__(account_number, client_number, balance, date_created)
        try:
            self.__minimum_balance = float(minimum_balance)
        except:
            self.__minimum_balance = 50  

    def __str__(self) -> str:
        """
        Returns a formatted string that represents the details of the savings account.

        Args:
            None

        Returns:
            str: A string containing the savings account’s information, including minimum balance and account type.
        """
        return (super().__str__() 
                + f'Minimum Balance: ${self.__minimum_balance:,.2f} ' 
                + f'Account Type: Savings')

    def get_service_charges(self) -> float:
        """
        Determines and returns the service charge for this savings account.

        Args:
            None

        Returns:
            float: The applicable service charge, which is either the base charge or a premium charge, depending on the balance.
        """
        if self._BankAccount__balance >= self.__minimum_balance:
            # Apply the base service charge if the balance meets the minimum requirement.
            service_charge = BankAccount.BASE_SERVICE_CHARGE
        else:
            # Apply a premium service charge if the balance is lower than the minimum.
            service_charge = BankAccount.BASE_SERVICE_CHARGE * SavingsAccount.SERVICE_CHARGE_PREMIUM

        return service_charge
