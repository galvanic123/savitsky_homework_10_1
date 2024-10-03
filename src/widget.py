from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(values: str) -> str:
    """Функция, которая обрабатывает информацию о картах и счетах"""
    account_type_card_num_list = values.split(" ")
    if len(account_type_card_num_list[-1]) < 20 and len(values) > 16:
        mask_card_number = get_mask_card_number(account_type_card_num_list[-1])
        account_type_card_num_list[-1] = mask_card_number
        if mask_card_number == 'неверный ввод':
            return "неверный ввод данных"
        return " ".join(account_type_card_num_list)
    if len(account_type_card_num_list[-1]) == 20 and len(values) == 25:
        mask_account = get_mask_account(account_type_card_num_list[-1])
        account_type_card_num_list[-1] = mask_account
        return " ".join(account_type_card_num_list)
    return "неверный ввод данных"


print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(user_date: str) -> str:
    """Функция получения даты в определенном формате и
    возвращения в формате ДД.ММ.ГГГГ"""

    return f"{user_date[8:10]}.{user_date[5:7]}.{user_date[0:4]}"


print(get_date("2024-03-11T02:26:18.671407"))
