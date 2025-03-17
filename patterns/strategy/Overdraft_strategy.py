"""This module defines the OverdraftStrategy class, which applies service charges based on an overdraft policy."""

__author__ = "Sahil Choudhary"
__version__ = "1.0.0"
__Credit__ = "Sahil Choudhary"

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount



class OverdraftStrategy(ServiceChargeStrategy):
    """
    OverdraftStrategy class: Implements a strategy for calculating service charges
    based on overdraft limits and rates.
    """
    
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Sets up the OverdraftStrategy with the specified overdraft limit and rate.

        Args:
            overdraft_limit (float): The maximum allowable overdraft amount before 
                                      additional fees are incurred. This value is typically
                                      negative (below 0.00).
            overdraft_rate (float): The fee rate applied to the overdraft amount beyond
                                     the specified limit.
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Computes the total service charges for an account, considering any overdraft fees.

        Args:
            account (BankAccount): The bank account for which the service charge is being computed.

        Returns:
            float: The total service charge, which includes any applicable overdraft fees.

        """
        if account.balance >= self.__overdraft_limit:
            service_charge = ServiceChargeStrategy.BASE_SERVICE_CHARGE
        else:
            service_charge = (ServiceChargeStrategy.BASE_SERVICE_CHARGE + 
                            (self.__overdraft_limit - account.balance) * self.__overdraft_rate)       
        return service_charge
        
