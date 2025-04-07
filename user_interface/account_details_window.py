__author__ = "ACE Faculty"
__version__ = "5.0.0"
__credits__ = "Sahil Choudhary"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy


class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account
    transactions.
    """
    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount, parent=None) -> None:
        """
        Initializes the AccountDetailsWindow.

        Args:
            account (BankAccount): The BankAccount object to display.
            parent (QWidget, optional): The parent widget for this window. Defaults to None.
        """
        super().__init__(parent)

        if not isinstance(account, BankAccount):
            QMessageBox.critical(self, "Initialization Error", "Invalid account type provided.")
            self.reject()
            return

        self._account = copy.deepcopy(account)

        self.account_number_label.setText(str(self._account.account_number))
        self.balance_label.setText(f"${self._account.balance:,.2f}")

        self.deposit_button.clicked.connect(self._handle_transaction)
        self.withdraw_button.clicked.connect(self._handle_transaction)
        self.exit_button.clicked.connect(self._close_window)

    def _handle_transaction(self):
        """
        Handles deposit and withdrawal transactions.
        """
        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.warning(
                self, "Invalid Input", "Transaction amount must be a numeric value."
            )
            self.transaction_amount_edit.setFocus()
            return

        operation_source = self.sender()
        transaction_type = ""

        try:
            if operation_source == self.deposit_button:
                transaction_type = "Deposit"
                self._account.deposit(amount)
            elif operation_source == self.withdraw_button:
                transaction_type = "Withdraw"
                self._account.withdraw(amount)
            else:
                return  # Should not happen

            self.balance_label.setText(f"${self._account.balance:,.2f}")
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()

            self.balance_updated.emit(self._account)

        except Exception as transaction_error:
            QMessageBox.critical(
                self, f"{transaction_type} Failed", str(transaction_error)
            )
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()

    def _close_window(self):
        """
        Closes the account details window.
        """
        self.close()