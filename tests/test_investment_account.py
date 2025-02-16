"""
Description: Unit tests for the InvestmentAccount class.
Author: Sahil Choudhary
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_investment_account.py
"""

import unittest
from bank_account.Investment_account import InvestmentAccount
from bank_account.bank_account import BankAccount
from datetime import date, time, timedelta

class TestInvestmentAccount(unittest.TestCase):

    def test_initialization_valid_arguments_attributes_set(self):
        account = InvestmentAccount(350, 350, 350, date(2024, 5, 10), 3)
        self.assertEqual(350, account._BankAccount__account_number)
        self.assertEqual(350, account._BankAccount__client_number)
        self.assertEqual(350, account._BankAccount__balance)
        self.assertEqual(date(2024, 5, 10), account._date_created)
        self.assertEqual(3, account._InvestmentAccount__management_fee)

    def test_initialization_invalid_management_fee_sets_to_default_value(self):
        account = InvestmentAccount(350, 350, 350, date(2024, 5, 10), 'three')
        self.assertEqual(2.55, account._InvestmentAccount__management_fee)

    def test_service_charge_account_older_than_ten_years_calculates_service_charge(self):
        account = InvestmentAccount(350, 350, 350, date(2014, 5, 10), 3)
        self.assertEqual(0.50, account.get_service_charges())

    def test_service_charge_account_exactly_ten_years_old_calculates_service_charges(self):
        account = InvestmentAccount(350, 350, 350, InvestmentAccount.TEN_YEARS_AGO, 3)
        self.assertEqual(3.50, account.get_service_charges())

    def test_service_charge_account_younger_than_ten_years_calculates_service_charge(self):
        account = InvestmentAccount(350, 350, 350, date(2024, 5, 10), 3)
        self.assertEqual(3.50, account.get_service_charges())

    def test_string_representation_date_created_more_than_ten_years_ago_returns_string(self):
        account = InvestmentAccount(350, 350, 350, date(2014, 5, 10), 3)
        self.assertEqual("Account Number: 350 Balance: $350.00\nDate Created: "
                         "2014-05-10 Management Fee: Waived Account Type: "
                         "Investment", str(account))

    def test_string_representation_date_created_less_than_ten_years_ago_returns_string(self):
        account = InvestmentAccount(350, 350, 350, date(2024, 5, 10), 3)
        self.assertEqual("Account Number: 350 Balance: $350.00\nDate Created: "
                         "2024-05-10 Management Fee: $3.00 Account Type: "
                         "Investment", str(account))
