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

    @property
    def account_number(self) -> int:
        """
        Getter for account number.

        Args:
            None

        Returns:
            int: The account number of the bank account.
        """
        return self.__account_number

    @property
    def client_number(self) -> int:
        """
        Getter for client number.

        Args:
            None

        Returns:
            int: The client number associated with the bank account holder.
        """
        return self.__client_number

    @property
    def balance(self) -> float:
        """
        Getter for balance.

        Args:
            None

        Returns:
            float: The current balance in the bank account.
        """
        return self.__balance

    def update_balance(self, amount: float) -> None:
        """
        Updates the balance by applying a transaction amount.

        Args:
            amount (float): The transaction amount to modify the balance.

        Returns:
            None

        Raises:
            ValueError: If the amount cannot be converted to a float.
        """
        try:
            amount = float(amount)
            self.__balance += amount
        except ValueError as e:
            print(f"ERROR: {e}")

    def deposit(self, amount: float) -> None:
        """
        Deposits an amount into the bank account.

        Args:
            amount (float): The amount to deposit into the account.

        Returns:
            None

        Raises:
            ValueError: If the deposit amount is not numeric or is non-positive.
        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")

        if amount <= 0:
            formatted_amount = f"${amount:,.2f}"
            raise ValueError(f"Deposit amount: {formatted_amount} must be positive.")

        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        """
        Withdraws an amount from the bank account.

        Args:
            amount (float): The amount to withdraw from the account.

        Returns:
            None

        Raises:
            ValueError: If the withdrawal amount is non-numeric, non-positive, or exceeds the balance.
        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Withdrawal amount: {amount} must be numeric.")

        if amount <= 0:
            formatted_amount = f"${amount:,.2f}"
            raise ValueError(f"Withdrawal amount: {formatted_amount} must be positive.")

        if amount > self.__balance:
            formatted_amount = f"${amount:,.2f}"
            formatted_balance = f"${self.__balance:,.2f}"
            raise ValueError(f"Withdrawal amount: {formatted_amount} cannot exceed the current balance: "
                             + f"{formatted_balance}.")

        self.update_balance(-amount)

   

