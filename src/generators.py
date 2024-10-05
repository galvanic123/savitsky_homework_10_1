def filter_by_currency():
    """Функция возвращает итератор, который поочередно
     выдает транзакции, где валюта операции соответствует заданной"""
    pass

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

def transaction_description():
    """Генератор, который принимает список словарей с транзакциями
     и возвращает описание каждой операции по очереди"""
    pass

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

   # Перевод организации
   # Перевод со счета на счет
   # Перевод со счета на счет
   # Перевод с карты на карту
   # Перевод организации

card_number_generator = ()
for card_number in card_number_generator(1, 5):
    print(card_number)

