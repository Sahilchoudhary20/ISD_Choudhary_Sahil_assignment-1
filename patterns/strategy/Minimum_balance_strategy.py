from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Strategy class for calculating service charges for savings accounts with a minimum balance requirement.
    This class implements the `calculate_service_charges` method based on the account's balance and
    minimum balance requirement.
    """

    SERVICE_CHARGE_PREMIUM: float = 2.0

    def __init__(self, minimum_balance: float):
        """
        Initializes the MinimumBalanceStrategy with the minimum balance requirement.

        Args:
            minimum_balance (float): The minimum balance required for the account.
        """
        self._minimum_balance = minimum_balance

    def calculate_service_charges(self, account: 'BankAccount') -> float: 
        """
        Calculates service charges for a savings account with a minimum balance requirement.
        If the account balance falls below the minimum, a premium service charge is applied.

        Args:
            account (BankAccount): The bank account for which to calculate service charges.

        Returns:
            float: The total service charges, including the premium charge if applicable.
        """
        if account.balance < self._minimum_balance:
            return self.BASE_SERVICE_CHARGE + self.SERVICE_CHARGE_PREMIUM
        return self.BASE_SERVICE_CHARGE