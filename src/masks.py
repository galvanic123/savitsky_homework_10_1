import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция для приёма и маскировки номера карты"""
    logger.info(f"Задаём формат маски для номера банковской карты {card_number}")
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return "неверный ввод"


print(get_mask_card_number("1596837868705199"))


def get_mask_account(account_number: Union[str]) -> str:
    """Функция, которая маскирует номер счёта"""
    logger.info(f"Задаём формат маски для номера счёта {account_number}")
    if len(account_number) == 20 and account_number.isdigit():
        return f"**{account_number[-4:]}"
    return "неверный ввод"


print(get_mask_account("64686473678894779589"))
print(get_mask_account("64686473678894722589"))
