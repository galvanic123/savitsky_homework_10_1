import os

import pytest

from src.decorators import log


def test_log_file():              # type: ignore[no-untyped-def]
    @log(filename="mylog.txt")
    def function(x, y):             # type: ignore[no-untyped-def]
        return x * y

    function(5, 2)
    with open(os.path.join(r"logs", "mylog.txt"), "rt") as file:
        for line in file:
            log_str = line

    assert log_str == "function ok\n"


def test_log_console(capsys):              # type: ignore[no-untyped-def]

    @log()
    def function(x, y):          # type: ignore[no-untyped-def]
        return x * y

    result = function(5, 2)
    captured = capsys.readouterr()

    assert captured.out == "function ok\n"
    assert result == 10


def test_log_file_error():              # type: ignore[no-untyped-def]               # type: ignore[no-untyped-def]
    @log(filename="mylog.txt")
    def function(x, y):          # type: ignore[no-untyped-def]
        raise TypeError("division by zero")

    with pytest.raises(TypeError, match="division by zero"):
        function(5, 0)

    with open(os.path.join(r"logs", "mylog.txt"), "rt") as file:
        for line in file:
            log_str = line

    assert log_str == "function error: division by zero. Inputs: (5, 0), {}\n"


def test_log_console_error(capsys):                       # type: ignore[no-untyped-def]

    @log()
    def function(x, y):               # type: ignore[no-untyped-def]
        raise ValueError("division by zero")

    with pytest.raises(ValueError, match="division by zero"):
        function(5, 0)

    captured = capsys.readouterr()

    assert captured.out == "function error: division by zero. Inputs: (5, 0), {}\n"
