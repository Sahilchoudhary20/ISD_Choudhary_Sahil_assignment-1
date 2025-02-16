"""
Description: Unit tests for the ChequingAccount class.
Author: Sahil Choudhary
Usage: To run all tests from the terminal, execute the following command:
    python -m unittest tests/test_chequing_account.py
"""

import unittest
from bank_account.chequing_account import ChequingAccount
from bank_account.bank_account import BankAccount
from datetime import date, time, timedelta

class TestChequingAccount(unittest.TestCase):

    def test_initialization_with_valid_arguments(self):
        # Test initialization of attributes with valid inputs
        expected_account = ChequingAccount(350, 350, 350, date(2024, 3, 25), -10, 0.08)
        
        # Checking if all attributes are correctly set
        self.assertEqual(350, expected_account._BankAccount__account_number)
        self.assertEqual(350, expected_account._BankAccount__client_number)
        self.assertEqual(350, expected_account._BankAccount__balance)
        self.assertEqual(date(2024, 3, 25), expected_account._date_created)
        self.assertEqual(-10, expected_account._ChequingAccount__overdraft_limit)
        self.assertEqual(0.08, expected_account._ChequingAccount__overdraft_rate)

    def test_initialization_with_invalid_overdraft_limit(self):
        # Testing an invalid overdraft limit
        expected_account = ChequingAccount(350, 350, 350, date(2024, 3, 25), '-ten', 0.08)
        # If invalid, it should set the overdraft limit to -100
        self.assertEqual(-100, expected_account._ChequingAccount__overdraft_limit)

    def test_initialization_with_invalid_overdraft_rate(self):
        # Testing an invalid overdraft rate
        expected_account = ChequingAccount(350, 350, 350, date(2024, 3, 25), -10, '8 percent')
        # If invalid, it should set the overdraft rate to 5%
        self.assertEqual(0.05, expected_account._ChequingAccount__overdraft_rate)

    def test_initialization_with_invalid_date_created(self):
        # Testing an invalid date format
        expected_account = ChequingAccount(350, 350, 350, "25 March, 2024", -10, 0.08)
        # Invalid date should be set to the current date (2025, 2, 15)
        self.assertEqual(date(2025, 2, 15), expected_account._date_created)

    def test_calculation_of_service_charges_when_balance_is_greater_than_overdraft_limit(self):
        # Testing service charge when balance is greater than overdraft limit
        expected_account = ChequingAccount(350, 350, 350, date(2024, 3, 25), -10, 0.08)
        # The expected service charge in this case should be $0.50
        self.assertEqual(0.50, expected_account.get_service_charges())

    def test_calculation_of_service_charges_when_balance_is_less_than_overdraft_limit(self):
        # Testing service charge when balance is less than overdraft limit
        expected_account = ChequingAccount(350, 350, -100, date(2024, 3, 25), -10, 0.08)
        # The expected service charge should be $7.70
        self.assertEqual(7.7, expected_account.get_service_charges())

    def test_calculation_of_service_charges_when_balance_is_equal_to_overdraft_limit(self):
        # Testing service charge when balance is equal to overdraft limit
        expected_account = ChequingAccount(350, 350, -10, date(2024, 3, 25), -10, 0.08)
        # The expected service charge should be $0.50
        self.assertEqual(0.50, expected_account.get_service_charges())

    def test_string_representation_of_account_with_valid_values(self):
        # Testing the string representation of a valid account
        expected_account = ChequingAccount(350, 350, 350, date(2024, 3, 25), -10, 0.08)
        self.assertEqual("Account Number: 350 Balance: $350.00\nOverdraft "
                         "Limit: $-10.00 Overdraft Rate: 8% Account Type: Chequing", str(expected_account))

