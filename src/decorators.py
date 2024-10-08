from collections.abc import Callable
from functools import wraps
from typing import Any


def log(filename: str | None = None):
    """Логирует вызов функции и её результат в файл или в консоль"""

    def my_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok ")
            except Exception as e:
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f"{func.__name__} error: {e}. Input: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e}. Input: {args}, {kwargs}")
            return result
        return wrapper
    return my_decorator

@log(filename='my_log.txt')
def my_function(x: int, y: int) -> int:
    return x + y

print(my_function(1, 2))

