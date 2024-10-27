import json
import logging
from typing import Any

# from src.setup_logger import setup_logger

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def data_transactions(my_data: str) -> Any:
    """Функция, принимающая путь до файла в формате json и возвращающая список словарей"""
    try:
        logger.info(f"Открытие json файла {my_data}")
        with open(my_data, "r", encoding="utf-8") as f:
            list_transaction = json.load(f)
            logger.info(f"Проверяем, что файл {my_data} не пустой")
        if isinstance(list_transaction, list):
            return list_transaction
        else:
            return []
    except Exception as ex:
        logger.error(f"Ошибка {ex}")
        return []


if __name__ == "__main__":
    my_path = "..\\data\\operations.json"
    transactions_list = data_transactions(my_path)
    print(transactions_list)
