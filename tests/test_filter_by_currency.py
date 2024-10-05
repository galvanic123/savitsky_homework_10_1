import pytest

from src.generators import filter_by_currency
from tests.conftest import result_rub, result_usd, transactions

"""Параметризация для filter_by_currency"""


@pytest.mark.parametrize(
    "value, currency, expected",
    [
        ([], "USD", [[]]),
        ([], "RUB", [[]]),
        (transactions, "USD", result_usd),
        (transactions, "RUB", result_rub),
        (result_rub, "USD", []),
        (result_usd, "RUB", []),
    ],
)
def test_filter_by_currency_various_input_data(value: list, currency: str, expected: list) -> None:
    result = list(filter_by_currency(value, currency))
    assert result == expected
