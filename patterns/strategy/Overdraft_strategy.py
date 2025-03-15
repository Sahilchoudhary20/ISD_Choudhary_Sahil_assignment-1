from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy


class OverdraftStrategy(ServiceChargeStrategy):
    """
    Strategy class for calculating service charges for accounts with overdraft functionality.
    This class implements the `calculate_service_charges` method based on the overdraft limit
    and rate.
    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the OverdraftStrategy with the given overdraft limit and rate.

        Args:
            overdraft_limit (float): The maximum allowed overdraft limit for the account.
            overdraft_rate (float): The rate at which overdraft charges are calculated.
        """
        self._overdraft_limit = overdraft_limit
        self._overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: 'BankAccount') -> float:
        """
        Calculates service charges for an account with overdraft functionality.
        If the account balance is below zero, additional overdraft charges are applied.

        Args:
            account (BankAccount): The bank account for which to calculate service charges.

        Returns:
            float: The total service charges, including overdraft charges if applicable.
        """
        if account.balance < 0:
            return self.BASE_SERVICE_CHARGE + abs(account.balance) * self._overdraft_rate
        return self.BASE_SERVICE_CHARGE