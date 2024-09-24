def mask_account_card(values: str) -> str:
    """Функция, которая обрабатывает информацию о картах и счетах"""

    bill_info = values.split()
    number = bill_info[-1]
    if len(number) == 16:
        result = f"{number[:4]}{number[4:6]}** **** {number[12:]}"
    elif len(number) == 20:
        result = f"**{number[-4:]}"
    print(values.split()[0], result)


mask_account_card('Maestro 1596837868705199')
mask_account_card('Счет 64686473678894779589')
mask_account_card('MasterCard 7158300734726758')
mask_account_card('Счет 35383033474447895560')
mask_account_card('Visa Classic 6831982476737658')
mask_account_card('Visa Platinum 8990922113665229')
mask_account_card('Visa Gold 5999414228426353')
mask_account_card('Счет 73654108430135874305')

def get_date(user_date: str) -> str:
 """Функция получения даты в определенном формате и
          возвращения в формате ДД.ММ.ГГГГ"""

 return f"'ДД.ММ.ГГГГ'{user_date[8:10]}.{user_date[5:7]}.{user_date[0:4]}"
print(get_date("2024-03-11T02:26:18.671407"))
