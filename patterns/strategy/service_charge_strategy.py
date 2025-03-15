from abc import ABC, abstractmethod
from datetime import date, timedelta

from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    Abstract base class for calculating service charges for different types of bank accounts.
    This class defines the base service charge and requires subclasses to implement the
    `calculate_service_charges` method.
    """
    BASE_SERVICE_CHARGE: float = 0.50

    @abstractmethod
    def calculate_service_charges(self, account: 'BankAccount') -> float:
        """
        Abstract method to calculate service charges for a given bank account.

        Args:
            account (BankAccount): The bank account for which to calculate service charges.

        Returns:
            float: The calculated service charges.
        """
        pass