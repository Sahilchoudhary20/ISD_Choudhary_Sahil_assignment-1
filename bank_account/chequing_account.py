"""
Description: This file defines the ChequingAccount class, which is responsible 
for managing bank account details and transactions specific to chequing accounts.
"""

__author__ = "Sahil Choudhary"
__version__ = "1.0.0"
__credits__ = "Sahil Choudhary"

from bank_account.bank_account import BankAccount
from datetime import date, time, timedelta

class ChequingAccount(BankAccount):
    """
    ChequingAccount class: Manages chequing account transactions and related 
    banking activities.
    """

    def __init__(self, account_number: int, client_number: int, balance: float,
            date_created: date, overdraft_limit: float, overdraft_rate: float) -> None:
        """
        Initializes attributes for a ChequingAccount.

        Args:
            account_number (int): The unique number assigned to the bank account.
            client_number (int): The unique identifier of the client holding the account.
            balance (float): The current balance of the bank account.
            date_created (date): The date on which the bank account was created.
            overdraft_limit (float): The threshold below which the account balance can 
                                     fall before overdraft fees are charged.
            overdraft_rate (float): The rate at which overdraft charges are applied.

        Raises:
            ValueError: If account_number or client_number is not an integer.
            ValueError: If balance, overdraft_limit, or overdraft_rate can't be converted to a float.

        Returns:
            None
        """
        super().__init__(account_number, client_number, balance, date_created)
        
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except:
            self.__overdraft_limit = -100  # Default overdraft limit if invalid input
        
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except:
            self.__overdraft_rate = 0.05  # Default overdraft rate if invalid input

    def __str__(self) -> str:
        """
        Returns a string that represents the information of the chequing account.
        
        Args:
            None

        Returns:
            str: A detailed string representation of the chequing account.
        """
        return (super().__str__()
            + f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
            + f"Overdraft Rate: {self.__overdraft_rate * 100:,.0f}% "
            + f"Account Type: Chequing")
    
    def get_service_charges(self) -> float:
        """
        Computes the service charge for the chequing account.

        Args:
            None

        Returns:
            float: The calculated service charge based on account balance and overdraft.
        """
        if self._BankAccount__balance >= self.__overdraft_limit:
            service_charge = BankAccount.BASE_SERVICE_CHARGE
        else:
            service_charge = (BankAccount.BASE_SERVICE_CHARGE + 
                            (self.__overdraft_limit - self._BankAccount__balance) * self.__overdraft_rate)
        return service_charge
