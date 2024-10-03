import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import list_of_dict_sort_res_true, list_of_dict_sorted_1


@pytest.fixture
def list_of_dict_fixture() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dict_ident_dates_fixture() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_basic(list_of_dict_fixture: list) -> None:
    """Тест на срабатывание функции со списком словарей list_of_dict по дефолтным условиям"""
    assert filter_by_state(list_of_dict_fixture) == list_of_dict_sorted_1


def test_sort_by_date_basic(list_of_dict_fixture: list) -> None:
    """Тестирование сортировки списка словарей в порядке убывания."""
    assert sort_by_date(list_of_dict_fixture) == list_of_dict_sort_res_true
