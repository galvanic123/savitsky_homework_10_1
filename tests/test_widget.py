import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("string, expected_result", [
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 12345678901234567890", "Счет **7890"),
])
def test_mask_account_card(string, expected_result):
    assert mask_account_card(string) == expected_result


@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"


def test_get_data(date):
    assert get_date(date) == "11.03.2024"
