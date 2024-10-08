from collections.abc import Callable
from functools import wraps
from typing import Any


def log(filename: Any = None) -> Any:
    """Логирует вызов функции и её результат в файл или в консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok\n")
            except Exception as e:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__}\n error: {e}. Input: {args}, {kwargs}")
                else:
                    print(f"{func.__name__}\n error: {e}. Input: {args}, {kwargs}")
            return result

        return wrapper

    return decorator


@log(filename=None)
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
