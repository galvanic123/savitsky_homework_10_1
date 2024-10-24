import json
from typing import Any


def data_transactions(my_data: str) -> Any:
    """Функция, принимающая путь до файла в формате json и возвращающая список словарей"""
    try:
        with open(my_data, "r", encoding="utf-8") as f:
            list_transaction = json.load(f)
        if isinstance(list_transaction, list):
            return list_transaction
        else:
            return []
    except Exception as e:
        print(f"Ошибка {e}")
        return []


if __name__ == "__main__":
    my_path = "..\\data\\operations.json"
    transactions_list = data_transactions(my_path)
    print(transactions_list)
