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

    def _handle_client_lookup(self):
        """
        Handles the event when the lookup button is clicked.
        Retrieves the client number from the input, validates it,
        and displays the client's information and associated accounts.
        """
        client_id_input = self.client_number_edit.text()

        try:
            client_id = int(client_id_input)
        except ValueError:
            QMessageBox.information(
                self, "Input Error", "The client number must be a numeric value."
            )
            self._reset_display()
            return

        if client_id not in self._clients:
            QMessageBox.information(
                self, "Not Found", f"Client number: {client_id} not found."
            )
            self._reset_display()
            return

        client = self._clients[client_id]
        self.client_info_label.setText(f"Client Name: {client.first_name} {client.last_name}")

        self.account_table.setRowCount(0)
        row_index = 0

        print(f"[DEBUG] Loaded {len(self._accounts)} accounts")
        for account in self._accounts.values():
            print(f"[DEBUG] Account {account.account_number} → Client: {account.client_number}")

        for account_obj in self._accounts.values():
            if int(account_obj.client_number) == client_id:
                print(f"[MATCH] Adding account {account_obj.account_number} for client {client_id}")

                self.account_table.insertRow(row_index)

                account_number_widget = QTableWidgetItem(str(account_obj.account_number))
                balance_widget = QTableWidgetItem(f"${account_obj.balance:,.2f}")
                creation_date_widget = QTableWidgetItem(str(account_obj.date_created))
                account_type_widget = QTableWidgetItem(account_obj.__class__.__name__)

                account_number_widget.setTextAlignment(Qt.AlignCenter)
                balance_widget.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                creation_date_widget.setTextAlignment(Qt.AlignCenter)
                account_type_widget.setTextAlignment(Qt.AlignCenter)

                self.account_table.setItem(row_index, 0, account_number_widget)
                self.account_table.setItem(row_index, 1, balance_widget)
                self.account_table.setItem(row_index, 2, creation_date_widget)
                self.account_table.setItem(row_index, 3, account_type_widget)

                row_index += 1

        self.account_table.resizeColumnsToContents()

    def _handle_text_change(self):
        """
        Handles the event when the text in the client number edit field changes.
        Resets the display if the input field is empty.
        """
        if not self.client_number_edit.text().strip():
            self._reset_display()
            self.account_table.setRowCount(0)

