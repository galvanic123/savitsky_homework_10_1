import tempfile

from src.decorators import log

# Тестируемая функция
# noinspection SpellCheckingInspection


def test_log_good(capsys):  # type: ignore[no-untyped-def]
    """Тестирует выполнение декорированной функции"""

    @log()
    def func(x, y):  # type: ignore[no-untyped-def]
        return x + y

    result = func(1, 2)
    assert result == 3


# noinspection SpellCheckingInspection
def test_log_good_file_log(capsys):  # type: ignore[no-untyped-def]
    """Тестирует запись в файл после успешного выполнения"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def func(x, y):  # type: ignore[no-untyped-def]
        return x + y

    func(1, 2)
    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()
    assert "func ok\n" in logs


# noinspection SpellCheckingInspection
def test_log_exception(capsys):  # type: ignore[no-untyped-def]
    """Тестирует вывод после ошибки в консоль"""

    @log()
    def func(x, y):  # type: ignore[no-untyped-def]
        return x + y

    func(1, 2)
    captured = capsys.readouterr()
    assert "func ok\n\n" in captured.out


# noinspection SpellCheckingInspection
def test_log_exception_file_log(capsys):  # type: ignore[no-untyped-def]
    """Тестирует запись в файл после ошибки"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def func(x, y):  # type: ignore[no-untyped-def]
        return x + y

    func(1, 2)
    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()
    assert "func ok\n" in logs
