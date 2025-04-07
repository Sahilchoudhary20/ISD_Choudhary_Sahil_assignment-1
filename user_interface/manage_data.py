__author__ = "ACE Faculty"
__version__ = "2.1.0"
__credits__ = "Sahil Choudhary"

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import csv
import logging
from datetime import datetime
from bank_account.chequing_account import ChequingAccount
from bank_account.Investment_account import InvestmentAccount
from bank_account.savings_account import SavingsAccount
from bank_account.bank_account import BankAccount
from client.client import Client

# *******************************************************************************
# SETTING UP LOGGING CONFIGURATION AND FILE PATHS

root_dir = os.path.dirname(os.path.dirname(__file__))
log_folder = os.path.join(root_dir, 'logs')
os.makedirs(log_folder, exist_ok=True)

log_file = os.path.join(log_folder, 'data_management.log')
logging.basicConfig(
        filename=log_file,
        filemode='a',
        format='%(name)s - %(levelname)s - %(message)s\n\n'
)

data_folder = os.path.join(root_dir, 'data')
accounts_file_path = os.path.join(data_folder, 'accounts.csv')
clients_file_path = os.path.join(data_folder, 'clients.csv')

# *******************************************************************************

def load_data() -> tuple[dict, dict]:
    """
    Reads data from CSV files for clients and bank accounts, creates corresponding 
    objects, and returns them in dictionaries.

    The function loads client information from the `clients.csv` file and account data 
    from the `accounts.csv` file. The client data is used to create `Client` objects, 
    and account data is used to create different types of `BankAccount` objects.

    Returns:
        tuple[dict, dict]: A tuple containing:
            - clients_dict: Dictionary of `Client` objects, keyed by `client_number`.
            - accounts_dict: Dictionary of `BankAccount` objects, keyed by `account_number`.

    Raises:
        FileNotFoundError: If the CSV files cannot be found.
        ValueError: If any data conversion or validation fails.
    """
    clients_dict = {}
    accounts_dict = {}

    # READING CLIENT DATA :
    with open(clients_file_path, newline='') as client_file:
        reader = csv.DictReader(client_file)
        for record in reader:
            try:
                client_number = int(record["client_number"])
                first_name = record["first_name"].strip()
                last_name = record["last_name"].strip()
                email = record["email_address"].strip()

                if not first_name:
                    raise ValueError("First name cannot be empty.")
                if not last_name:
                    raise ValueError("Last name cannot be empty.")
                if not email:
                    raise ValueError("Email address cannot be empty.")

                client = Client(client_number, first_name, last_name, email)
                clients_dict[client_number] = client

            except Exception as error:
                logging.error(f"Error creating client: {error}")

    # READING ACCOUNT DATA :
    with open(accounts_file_path, newline='') as account_file:
        reader = csv.DictReader(account_file)
        for record in reader:
            try:
                account_number = int(record["account_number"])
                client_number = int(record["client_number"])
                account_type = record["account_type"].strip().lower()
                balance = float(record["balance"])
                date_created = datetime.strptime(record["date_created"], "%Y-%m-%d").date()

                if client_number not in clients_dict:
                    logging.error(f"Account {account_number} references an invalid client number {client_number}.")
                    continue

            
                if account_type == "chequingaccount":
                    overdraft_limit = float(record["overdraft_limit"])
                    overdraft_rate = float(record["overdraft_rate"])
                    account = ChequingAccount(
                        account_number, client_number, balance, date_created, overdraft_limit, overdraft_rate
                    )
                elif account_type == "savingsaccount":
                    minimum_balance = float(record["minimum_balance"])
                    account = SavingsAccount(account_number, client_number, balance, date_created, minimum_balance)
                elif account_type == "investmentaccount":
                    management_fee = float(record["management_fee"])
                    account = InvestmentAccount(account_number, client_number, balance, date_created, management_fee)
                else:
                    logging.error(f"Account {account_number} has an invalid account type: {account_type}")
                    continue

                accounts_dict[account_number] = account
                print(f"[DEBUG] Loaded account: {account}")

            except Exception as error:
                logging.error(f"Error creating account: {error}")

    return clients_dict, accounts_dict



