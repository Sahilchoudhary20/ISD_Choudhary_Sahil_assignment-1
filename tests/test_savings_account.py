"""
Description: Unit tests for the SavingsAccount class.
Author: Sahil Choudhary
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_savings_account.py
"""

import unittest
from bank_account.bank_account import BankAccount
from bank_account.savings_account import SavingsAccount
from datetime import date

class TestSavingsAccount(unittest.TestCase):

    def test_init_valid_arguments_attributes_set(self):
        account = SavingsAccount(350, 350, 350, date(2024, 5, 10), 30)
        self.assertEqual(350, account._BankAccount__account_number)
        self.assertEqual(350, account._BankAccount__client_number)
        self.assertEqual(350, account._BankAccount__balance)
        self.assertEqual(date(2024, 5, 10), account._date_created)
        self.assertEqual(30, account._SavingsAccount__minimum_balance)

    def test_init_invalid_minimum_balance_set_to_hundred(self):
        account = SavingsAccount(350, 350, 350, date(2024, 5, 10), 'thirty')
        self.assertEqual(100, account._SavingsAccount__minimum_balance)

    def test_get_service_charges_balance_greater_than_minimum_balance_service_charge_set_to_base(self):
        account = SavingsAccount(350, 350, 350, date(2024, 5, 10), 30)
        self.assertEqual(0.50, account.get_service_charges())

    def test_get_service_charges_balance_equal_to_minimum_balance_service_charge_set_to_base(self):
        account = SavingsAccount(350, 350, 30, date(2024, 5, 10), 30)
        self.assertEqual(0.50, account.get_service_charges())

    def test_get_service_charges_balance_less_than_minimum_balance_service_charge_calculated(self):
        account = SavingsAccount(350, 350, 15, date(2024, 5, 10), 30)
        self.assertEqual(1, account.get_service_charges())

    def test_str_valid_arguments_returns_formatted_string(self):
        account = SavingsAccount(350, 350, 350, date(2024, 5, 10), 30)
        self.assertEqual('Account Number: 350 Balance: $350.00\n'
                         'Minimum Balance: $30.00 Account Type: Savings', str(account))
