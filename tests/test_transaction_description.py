import pytest

from src.generators import transaction_descriptions
from tests.conftest import (description_res, exp_with_result_rub, exp_with_result_usd, result_rub, result_usd,
                            transactions)

"""Параметризация для transaction_descriptions"""


@pytest.mark.parametrize(
    "value, expected",
    [
        (transactions, description_res),
        (result_usd, exp_with_result_usd),
        (result_rub, exp_with_result_rub),
        ([], [[]]),
    ],
)
def test_transaction_descriptions(value: list, expected: list) -> None:
    result = list(transaction_descriptions(value))
    assert result == expected
