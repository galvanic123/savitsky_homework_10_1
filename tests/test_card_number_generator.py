import pytest

from src.generators import card_number_generator
from tests.conftest import (card_number_generator_exp_result_0_5, card_number_generator_exp_result_1_5,
                            card_number_generator_exp_result_2_2050)

"""Параметризация для card_number_generator"""


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 5, card_number_generator_exp_result_1_5),
        (2000000000000000, 2000000000000010, card_number_generator_exp_result_2_2050),
        (0, 5, card_number_generator_exp_result_0_5),
        (0, 0, []),
        (1, 0, []),
        (8, 5, []),
        (5, 5, []),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: list) -> None:
    result = list(card_number_generator(start, stop))
    assert result == expected
