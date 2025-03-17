"""This module defines the ManagementFeeStrategy class, which calculates service charges based on account creation date and management fees."""

__author__ = "Sahil Choudhary"
__version__ = "1.0.0"
__Credit__ = "Sahil Choudhary"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    ManagementFeeStrategy class: Implements a strategy for applying service charges based on
    account creation date and additional management fees.

    Attributes:
        TEN_YEARS_AGO (date): A constant representing the date exactly ten years ago from today.
        SERVICE_CHARGE_PREMIUM (float): A constant used for additional service charges under certain conditions (though it's not explicitly used here).
    """
    
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        Initializes the ManagementFeeStrategy with the account creation date and the management fee.

        Args:
            date_created (date): The date when the account was created.
            management_fee (float): The management fee that is charged for managing the account.
        """
        self.__date_created = date_created
        self.__management_fee = management_fee

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Computes the service charge for the given bank account. If the account was created
        within the last 10 years, the management fee is added to the base service charge.

        Args:
            account (BankAccount): The bank account for which the service charge is being calculated.

        Returns:
            float: The computed service charge, which may include an additional management fee if applicable.
        """
        total_service_charge = self.BASE_SERVICE_CHARGE
        if self.__date_created >= self.TEN_YEARS_AGO:
            total_service_charge += self.__management_fee
        return total_service_charge
