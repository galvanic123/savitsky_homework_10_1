import os

import pytest

from src.utils import data_transactions


@pytest.fixture
def path():  # type: ignore[no-untyped-def]
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operation_2.json")
    return PATH_TO_FILE


@pytest.fixture
def path_empty_list():  # type: ignore[no-untyped-def]
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operation_1.json")
    return PATH_TO_FILE


@pytest.fixture
def path_mistake_json():  # type: ignore[no-untyped-def]
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operation_3.json")
    return PATH_TO_FILE


@pytest.fixture
def trans():  # type: ignore[no-untyped-def]
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def trans_1():  # type: ignore[no-untyped-def]
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_data_transactions_nofile():  # type: ignore[no-untyped-def]
    assert data_transactions("nofile") == []


def test_data_transactions(path):  # type: ignore[no-untyped-def]
    assert data_transactions(path)[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_data_transactions_empty_list(path_empty_list):  # type: ignore[no-untyped-def]
    assert data_transactions(path_empty_list) == []


def test_data_transactions_mistake_json(path_mistake_json):  # type: ignore[no-untyped-def]
    assert data_transactions(path_mistake_json) == []
