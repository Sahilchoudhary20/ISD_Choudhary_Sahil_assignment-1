"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.bank_account = BankAccount(350, 350, 350)
    
    def test_init_valid_arguments_attributes_set(self):
        expected = BankAccount(350, 350, 350)

        self.assertEqual(100, expected._BankAccount__account_number)
        self.assertEqual(100, expected._BankAccount__client_number)
        self.assertEqual(100, expected._BankAccount__balance)

    def test_init_non_numeric_balance_argument_balance_set_to_zero(self):
        expected = BankAccount(350, 350, "Three hundred fifty")

        self.assertEqual(0, expected._BankAccount__balance)

    def test_init_non_numeric_account_number_raises_valueerror(self):
        with self.assertRaises(ValueError):
            BankAccount("Three hundred fifty", 350, 350)

    def test_init_non_numeric_client_number_raises_valueerror(self):
        with self.assertRaises(ValueError):
            BankAccount(350, "Three hundred fifty", 350)

    def test_account_number_accessor_returns_account_number_attribute(self):
        self.assertEqual(350, self.bank_account.account_number)

    def test_client_number_accessor_returns_client_number_attribute(self):
        self.assertEqual(350, self.bank_account.client_number)

    def test_balance_accessor_returns_balance_attribute(self):
        self.assertEqual(350, self.bank_account.balance)

    def test_update_balance_positive_amount_updates_balance(self):
        self.bank_account.update_balance(100)

        self.assertEqual(self.bank_account.balance, 300)

    def test_update_balance_negative_amount_updates_balance(self):
        self.bank_account.update_balance(-100)

        self.assertEqual(self.bank_account.balance, 100)

    def test_update_balance_non_numeric_amount_balance_unchanged(self):
        self.bank_account.update_balance("Hundred")

        self.assertEqual(self.bank_account.balance, 100)

    def test_deposit_valid_amount_balance_updated(self):
        self.bank_account.deposit(100)

        self.assertEqual(self.bank_account.balance, 100)

    def test_deposit_negative_amount_raises_valueerror(self):
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-100)

    def test_withdraw_valid_amount_balance_updated(self):
        self.bank_account.withdraw(100)

        self.assertEqual(self.bank_account.balance, 100)

    def test_withdraw_negative_amount_raises_valueerror(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-100)

    def test_withdraw_amount_exceeds_balance_raises_valueerror(self):
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(300)

    def test_str_valid_inputs_returns_string_representation(self):
        expected = "Account Number: 350 Balance: $350.00\n"

        self.assertEqual(expected, str(self.bank_account))