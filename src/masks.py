from typing import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция для приёма и маскировки номера карты"""
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return "неверный ввод"


print(get_mask_card_number("1596837868705199"))


def get_mask_account(account_number: Union[str]) -> str:
    """Функция которая маскирует номер счёта"""
    if len(account_number) == 20 and account_number.isdigit():
        return f"**{account_number[-4:]}"
    return "неверный ввод"


print(get_mask_account("64686473678894779589"))
print(get_mask_account("64686473678894722589"))
