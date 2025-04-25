__author__ = "ACE Faculty"
__version__ = "5.1.0"
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
        self.filter_button.clicked.connect(self.on_filter_clicked)

    def on_filter_clicked(self):
        """
        Handles the filter button click event to apply or reset filtering.
        """
        if self.filter_button.text() == "Apply Filter":
            column_index = self.filter_combo_box.currentIndex()
            filter_text = self.filter_edit.text().lower()
            
            for i in range(self.account_table.rowCount()):
                item = self.account_table.item(i, column_index)
                if item and filter_text in item.text().lower():
                    self.account_table.setRowHidden(i, False)
                else:
                    self.account_table.setRowHidden(i, True)
            
            self.toggle_filter(True)
        else:
            self.toggle_filter(False)

    def toggle_filter(self, filter_on: bool):
        """
        Toggles the display of filter widgets based on the filter state.
        
        Args:
            filter_on (bool): True if filtering is active, False otherwise
        """
        self.filter_button.setEnabled(True)
        
        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)
            self.filter_label.setText("Data is Not Currently Filtered")
            
            for i in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(i, False)

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

        for account_obj in self._accounts.values():
            if int(account_obj.client_number) == client_id:
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
        self.toggle_filter(False)

    def _handle_text_change(self):
        """
        Handles the event when the text in the client number edit field changes.
        Resets the display if the input field is empty.
        """
        if not self.client_number_edit.text().strip():
            self._reset_display()
            self.account_table.setRowCount(0)

    def _handle_account_selection(self, row_index, column_index):
        """
        Handles the event when a cell in the account table is clicked.
        Opens the AccountDetailsWindow for the selected account.
        """
        try:
            selected_item = self.account_table.item(row_index, 0)
            if selected_item is None:
                QMessageBox.informativeText(
                    self, "Invalid Selection", "Please select a valid record."
                )
                return

            account_number_str = selected_item.text().strip()

            if not account_number_str:
                QMessageBox.informativeText(
                    self, "Invalid Selection", "Please select a valid record."
                )
                return

            account_number = int(account_number_str)

            if account_number in self._accounts:
                selected_account = self._accounts[account_number]
                details_window = AccountDetailsWindow(selected_account)
                details_window.balance_updated.connect(self._update_account_display)
                details_window.exec()
            else:
                QMessageBox.informativeText(
                    self, "No Bank Account", "Bank Account selected does not exist."
                )

        except Exception as error:
            QMessageBox.warning(
                self, "Error", f"Could not open account details.\n{error}"
            )

    def _update_account_display(self, updated_account: BankAccount):
        """
        Updates the account table display with the new balance of the updated account.
        Also updates the internal account data and saves it.
        """
        for row in range(self.account_table.rowCount()):
            item = self.account_table.item(row, 0)
            if item and int(item.text()) == updated_account.account_number:
                self.account_table.item(row, 1).setText(f"${updated_account.balance:,.2f}")
                break

        self._accounts[updated_account.account_number] = updated_account
        update_account_data(updated_account)

    def _show_message(self, title: str, message: str):
        """
        Displays an information message box.
        """
        QMessageBox.information(self, title, message)

    def _show_warning(self, title: str, message: str):
        """
        Displays a warning message box.
        """
        QMessageBox.warning(self, title, message)

    def _reset_display(self):
        """
        Resets the client information label.
        """
        self.client_info_label.setText("")