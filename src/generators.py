from typing import Generator


def filter_by_currency(transaction_list: list, currency: str) -> Generator:
    """Функция возвращает итератор, который поочередно выдает транзакции,
     где валюта операции соответствует заданной """
    if len(transaction_list) > 0:
        for transaction in transaction_list:
            if transaction.get("operationAmount", [{}]).get("currency", [{}]).get("code", [{}]) == currency:
                yield transaction
    else:
        yield []


def transaction_descriptions(transaction_list: list) -> Generator:
    """Генератор, который принимает список словарей с транзакциями
         и возвращает описание каждой операции по очереди"""
    if len(transaction_list) > 0:
        for transaction in transaction_list:
            yield transaction.get("description")
    else:
        yield []


def card_number_generator(start: int, stop: int) -> Generator:
    """Создаём генератор , который выдает номера банковских карт в
    формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    if start == 0 and stop > 0:
        start += 1
    for number in range(start, stop):
        card_number = str(number)
        while len(card_number) < 16:
            if start < 1000000000000000:
                card_number = '0' + card_number
        formatted_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        yield formatted_card_number
