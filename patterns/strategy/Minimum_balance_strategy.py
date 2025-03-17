"""This module defines the MinimumBalanceStrategy class, which applies service charges based on a minimum balance requirement."""

__author__ = "Sahil Choudhary"
__version__ = "1.0.0"
__Credit__ = "Sahil Choudhary"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    MinimumBalanceStrategy class: Implements a strategy for calculating service charges
    based on whether an account's balance meets a minimum threshold.

    Attributes:
        SERVICE_CHARGE_PREMIUM (float): A constant multiplier for the service charge when the 
                                         balance is below the minimum required threshold.
    """
    
    SERVICE_CHARGE_PREMIUM = 2.0
    
    def __init__(self, minimum_balance: float):
        """
        Initializes the MinimumBalanceStrategy with a specified minimum balance requirement.

        Args:
            minimum_balance (float): The threshold below which a higher service charge 
                                      will be applied to the account.
        """
        self.__minimum_balance = float(minimum_balance)

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Computes the total service charges based on the account balance and minimum balance requirement.

        If the balance is below the minimum threshold, a premium service charge is applied.

        Args:
            account (BankAccount): The bank account for which the service charge is being calculated.

        Returns:
            float: The calculated service charge, which may include a premium if the balance is low.
        """
        total_service_charge = self.BASE_SERVICE_CHARGE
        if account.balance < self.__minimum_balance:
            total_service_charge *= self.SERVICE_CHARGE_PREMIUM
        return total_service_charge
