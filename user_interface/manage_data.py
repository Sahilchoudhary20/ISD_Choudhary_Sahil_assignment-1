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

