"""
Description: This file defines the InvestmentAccount class, which is designed to manage records 
for investment accounts in the banking system.
"""

__author__ = "Sahil Choudhary"
__version__ = "1.0.0"
__credits__ = "Sahil Choudhary"

from bank_account.bank_account import BankAccount
from datetime import date, timedelta

class InvestmentAccount(BankAccount):
    """
    InvestmentAccount class: Responsible for handling investment accounts within the bank.

    """
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, account_number: int, client_number: int, balance: float,
                date_created: date, management_fee: float) -> None:
        """
        Initializes the attributes for an InvestmentAccount instance.

        Args:
            account_number (int): Unique identifier for the account.
            client_number (int): Identifier for the client associated with the account.
            balance (float): The current balance of the account.
            date_created (date): The date when the account was established.
            management_fee (float): The fee charged by the bank for managing the account.

        Returns:
            None

        Raises:
            ValueError: If account_number or client_number are not integers.
            ValueError: If balance cannot be converted into a float.
                
        """
        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__management_fee = float(management_fee)
        except:
            self.__management_fee = 2.55

    def __str__(self) -> str:
        """
        Returns a formatted string with account details.

        Args:
            None
        
        Returns:
            str: The string representation of the investment account's information.

        """
        if self._date_created < InvestmentAccount.TEN_YEARS_AGO:
            return (super().__str__()
                + f'Date Created: {self._date_created} '
                + f'Management Fee: Waived '
                + f'Account Type: Investment')
        
        else:
            return (super().__str__()
                + f'Date Created: {self._date_created} '
                + f'Management Fee: ${self.__management_fee:,.2f} '
                + f'Account Type: Investment')
        
    def get_service_charges(self) -> float:
        """
        Computes the service charge for an investment account.

        Args:
            None

        Returns:
            float: The calculated service charge for the investment account.
        
        """
        if self._date_created < InvestmentAccount.TEN_YEARS_AGO:  
            service_charge = BankAccount.BASE_SERVICE_CHARGE
        else:
            service_charge = BankAccount.BASE_SERVICE_CHARGE + self.__management_fee

        return service_charge
