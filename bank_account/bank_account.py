__author__ = "Sahil Choudhary"
__version__ = "1.0.0"
__credits__ = "Sahil Choudhary"


from abc import ABC, abstractmethod
from datetime import date
from patterns.observer.observer import Observer
from patterns.observer.Subject import Subject 

class BankAccount(Subject, ABC):
    """
    BankAccount class: Manages and tracks bank account details.
    """
    LARGE_TRANSACTION_THRESHOLD = 9999.99
    LOW_BALANCE_LEVEL = 50.00

    def __init__(self, account_number: int, client_number: int, balance: float, 
                 date_created: date) -> None:
        """
        Initializes the bank account's attributes.

        Args:
            account_number (int): The bank account number.
            client_number (int): The client's unique identification number.
            balance (float): The initial balance of the account.
            date_created (date): The account creation date.

        Raises:
            ValueError: If account_number or client_number are not integers.
            ValueError: If balance is not convertible to a float.
        """
        super().__init__()
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be an integer.")
        
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be an integer.")
        
        try:
            self.__balance = float(balance)
        except ValueError:
            self.__balance = 0.0
        
        if isinstance(date_created, date):
            self.__date_created = date_created
        else:
            self.__date_created = date.today()

    @property
    def account_number(self) -> int:
        """
        Returns the account number.

        Returns:
            int: The account number.
        """
        return self.__account_number

    @property
    def client_number(self) -> int:
        """
        Returns the client number.

        Returns:
            int: The client's unique number.
        """
        return self.__client_number

    @property
    def balance(self) -> float:
        """
        Returns the current account balance.

        Returns:
            float: The current balance of the account.
        """
        return self.__balance

    @property
    def date_created(self) -> date:
        """
        Returns the account creation date.

        Returns:
            date: The date the account was created.
        """
        return self.__date_created

    def update_balance(self, amount: float) -> None:
        """
        Updates the account balance with the given amount.

        Args:
            amount (float): The transaction amount (could be deposit or withdrawal).

        Raises:
            ValueError: If the amount is not a float.
        """
        try:
            amount = float(amount)
            self.__balance += amount
        except ValueError as e:
            print("ERROR:", e)
        
        if self.__balance < BankAccount.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance alert: ${self.__balance:,.2f} on account {self.__account_number}.")

        if amount > BankAccount.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction alert: ${amount:,.2f} on account {self.__account_number}.")

    def deposit(self, amount: float) -> None:
        """
        Handles deposit transactions for the account.

        Args:
            amount (float): The deposit amount.

        Raises:
            ValueError: If the deposit amount is not positive or is not a float.
        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} must be a numeric value.")
        
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        """
        Processes withdrawal transactions for the account.

        Args:
            amount (float): The amount to be withdrawn.

        Raises:
            ValueError: If the withdrawal amount exceeds the current balance,
                        is not a positive number, or is not a float.
        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Withdrawal amount: {amount} must be numeric.")

        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must be positive.")

        if amount > self.__balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} exceeds account balance: ${self.__balance:,.2f}")

        self.update_balance(-amount)

    def __str__(self) -> str:
        """
        Returns the string representation of the bank account.

        Returns:
            str: The formatted account number and balance.
        """
        return f"Account Number: {self.__account_number} | Balance: ${self.__balance:,.2f}"

    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Abstract method for calculating service charges on the account.

        Must be implemented in subclasses.
        """
        pass

    def attach(self, observer: Observer) -> None:
        """
        Adds an observer to the account's notification list.

        Args:
            observer (Observer): The observer to be added.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Removes an observer from the account's notification list.

        Args:
            observer (Observer): The observer to be removed.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """
        Sends a notification message to all observers.

        Args:
            message (str): The message to be sent to observers.
        """
        for observer in self._observers:
            observer.update(message)
