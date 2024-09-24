from typing import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция для приёма и маскировки номера карты"""
    return f"{card_number[:4]}{card_number[4:6]}** **** {card_number[12:]}"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: Union[str]) -> str:
    """Функцияб которая маскирует номер счёта"""
    return f"**{account_number[-4:]}"


print(get_mask_account("73654108430135874305"))
