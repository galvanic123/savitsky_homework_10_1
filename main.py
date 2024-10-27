import os.path

from src.utils import data_transactions
from src.external_api import get_rub_amount











current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "data", "operations.json")
transactions1 = data_transactions(file_path)

for transaction in transactions1:
    rub_amount = get_rub_amount(transaction)
    print(f"Transaction amount in RUB: {rub_amount}")
