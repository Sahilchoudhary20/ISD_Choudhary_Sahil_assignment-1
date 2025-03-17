"""This module defines the MinimumBalanceStrategy class, which applies service charges based on a minimum balance requirement."""

__author__ = "Sahil Choudhary"
__version__ = "1.0.0"
__Credit__ = "Sahil Choudhary"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount


class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Employed to compute service charges for savings accounts.
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
            float: The service charge for a bank account.
        """

        if account.balance >= self.__minimum_balance:

            service_charge = ServiceChargeStrategy.BASE_SERVICE_CHARGE

        else:

            service_charge = (BankAccount.BASE_SERVICE_CHARGE * MinimumBalanceStrategy.SERVICE_CHARGE_PREMIUM)

        return service_charge
