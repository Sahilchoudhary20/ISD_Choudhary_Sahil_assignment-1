from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Strategy class for calculating service charges for investment accounts with a management fee.
    This class implements the `calculate_service_charges` method based on the account's creation date
    and management fee.
    """

    TEN_YEARS_AGO: date = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        Initializes the ManagementFeeStrategy with the account's creation date and management fee.

        Args:
            date_created (date): The date the account was created.
            management_fee (float): The management fee for the account.
        """
        self._date_created = date_created
        self._management_fee = management_fee

    def calculate_service_charges(self, account: 'BankAccount') -> float:
        """
        Calculates service charges for an investment account with a management fee.
        If the account is older than 10 years, the management fee is waived.

        Args:
            account (BankAccount): The bank account for which to calculate service charges.

        Returns:
            float: The total service charges, including the management fee if applicable.
        """
        if self._date_created < self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        return self.BASE_SERVICE_CHARGE + self._management_fee