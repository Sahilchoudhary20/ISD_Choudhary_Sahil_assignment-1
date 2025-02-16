__author__ = "Sahil Choudhary"
__version__ = "1.0.0"
__credits__ = "Sahil Choudhary"

from abc import ABC, abstractmethod
from datetime import date

class BankAccount(ABC):
    """
    BankAccount class: Manages the records and details of a bank account.
    """
    BASE_SERVICE_CHARGE: float = 0.50

    def __init__(self, account_number: int, client_number: int, balance: float, 
                date_created: date) -> None:
        """
        Initializes the bank account attributes.

        Args:
            account_number (int): The unique identifier for the bank account.
            client_number (int): The unique identifier for the account holder.
            balance (float): The current balance of the account.
            date_created (date): The date when the account was opened.

        Returns:
            None

        Raises:
            ValueError: If account_number or client_number are not integers.
            ValueError: If balance cannot be converted to a float.
        """
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be an integer.")

        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an integer.")

        try:
            balance = float(balance)
            self.__balance = balance
        except ValueError:
            self.__balance = 0

        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()

   