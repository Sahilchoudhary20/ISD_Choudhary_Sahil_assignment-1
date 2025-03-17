"""This module defines the ServiceChargeStrategy class."""

__author__ = "Sahil Choudhary"
__version__ = "1.0.0"
__Credit__ = "Sahil Choudhary"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount


class ServiceChargeStrategy(ABC):
    """
    Abstract base class for different service charge strategies.

    This class defines the interface for calculating service charges on bank accounts
    and provides a base service charge constant.

    Attributes:
        BASE_SERVICE_CHARGE (float): A constant representing the basic service charge for an account.
                                      The default value is set to 0.5.
    """
    BASE_SERVICE_CHARGE = 0.5

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Abstract method for calculating the service charge for a given bank account.

        This method must be implemented by subclasses to define the specific logic for calculating
        the service charge based on the bank account.

        Args:
            account (BankAccount): The bank account for which the service charge is to be calculated.

        Returns:
            float: The calculated service charge for the given account.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        pass
