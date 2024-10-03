import pytest

from src.processing import filter_by_state, list_of_dicts, sort_by_


@pytest.fixture
def test_filter_by_state(test_list_of_dict):     # type: ignore[no-untyped-def]
    assert filter_by_state(list_of_dicts, state=test_list_of_dict)


@pytest.fixture
def test_filter_by_state_1(test_list_of_dict):  # type: ignore[no-untyped-def]
    assert filter_by_state(list_of_dicts) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def test_filter_by_state_sort(test_list_of_dicts):    # type: ignore[no-untyped-def]
    assert sort_by_date(list_of_dicts) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
