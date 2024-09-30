from typing import Any

list_of_dicts = [
    {'id': 41428829, 'state': 'EXECUTED',
     'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED',
     'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED',
     'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED',
     'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(list_of_dict: list[dict[str, Any]],
                    state: str = "EXECUTED") -> Any:
    """Принимаем список словарей и значение ключа и возвращаем те словари,
                у которых ключ содержит переданное значение"""
    return [d for d in list_of_dict if d.get("state") == state]


def sort_by_date(list_of_dict: list[dict[str, Any]],
                 revers: bool = True) -> list[dict[str, Any]]:
    """Сортируем список словарей по убыванию по дате"""
    sorted_state = sorted(
        list_of_dict,
        key=lambda x : x["date"],
        reverse=revers
    )
    return sorted_state
