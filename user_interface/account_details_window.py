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

   