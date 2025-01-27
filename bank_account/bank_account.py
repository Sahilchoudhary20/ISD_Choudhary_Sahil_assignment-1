__author__ = "Sahil Choudhary"
__version__ = "1.0.0"
__credits__ = "Sahil Choudhary"

class BankAccount:
    """
    BankAccount class: Manages the details of a bank account.
    """

    def __init__(self, account_number: int, client_number: int, balance: float = None) -> None:
        """
        Initializes the bank account with provided values.

        Args:
            account_number (int): The unique identifier for the bank account.
            client_number (int): The unique identifier for the account holder.
            balance (float): The starting balance of the account, default is None.

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
            self.__balance = float(balance) if balance is not None else 0
        except ValueError:
            self.__balance = 0

    @property
    def account_number(self) -> int:
        """
        Retrieves the account number.

        Args:
            None

        Returns:
            int: The account number.
        """
        return self.__account_number

    @property
    def client_number(self) -> int:
        """
        Retrieves the client number.

        Args:
            None

        Returns:
            int: The client number.
        """
        return self.__client_number

    @property
    def balance(self) -> float:
        """
        Retrieves the current balance of the account.

        Args:
            None

        Returns:
            float: The current account balance.
        """
        return self.__balance
