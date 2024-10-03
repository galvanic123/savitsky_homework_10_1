import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 12345678901234567890", "Счет **7890"),
    ],
)
def test_mask_account_card(string, expected_result):    # type: ignore[no-untyped-def]
    """Тест на верный номер карты"""
    assert mask_account_card(string) == expected_result


@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000792289606361", "неверный ввод данных"),
        ("Счет", "неверный ввод данных"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("MasterCard 7000792289606361", "MasterCard 7000 79** **** 6361"),
        ("Visa Classic 7000792289606361", "Visa Classic 7000 79** **** 6361"),
        ("MasterCard 7000792289606361", "MasterCard 7000 79** **** 6361"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Gold 7000792289606361", "Visa Gold 7000 79** **** 6361"),
        ("Visa Gold 700079228960636", "неверный ввод данных"),
    ],
)
def test_mask_account_card_various_input_data(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


def test_get_date_basic() -> None:
    """Срабатывание с данными '2018-10-14T08:21:33.419441'"""
    assert get_date("2018-10-14T08:21:33.419441") == "14.10.2018"
