from typing import  Any

def filter_by_state(list_of_dict: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    """Принимаем список словарей и значение ключа и возвращаем те словари,
                у которых ключ содержит переданное значение"""
    return [d for d in list_of_dict if d.get("state") == state]
