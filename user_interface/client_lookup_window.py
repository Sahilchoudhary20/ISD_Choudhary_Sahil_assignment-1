__author__ = "ACE Faculty"
__version__ = "5.0.0"
__credits__ = "Sahil Choudhary"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data, update_account_data
from bank_account.bank_account import BankAccount


class ClientLookupWindow(LookupWindow):
    """
    A window for looking up client information and displaying their bank accounts.
    """

    def __init__(self):
        """
        Initializes the ClientLookupWindow.
        Loads client and account data and connects UI signals to slots.
        """
        super().__init__()

        self._clients, self._accounts = load_data()

        self.lookup_button.clicked.connect(self._handle_client_lookup)
        self.client_number_edit.textChanged.connect(self._handle_text_change)
        self.account_table.cellClicked.connect(self._handle_account_selection)

