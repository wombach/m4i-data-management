import pytest
from pandas import DataFrame, Series
from vox_data_management.test.functions import track_has_been_called

from .find_changed_rows import find_changed_rows


@pytest.fixture
def old_data():
    return DataFrame([
        {
            "id": 1,
            "abc": "def"
        },
        {
            "id": 2,
            "abc": "def"
        }
    ]).set_index("id")
# END old_data


@pytest.fixture
def new_data():
    return DataFrame([
        {
            "id": 1,
            "abc": "ghi"
        },
        {
            "id": 3,
            "abc": "def"
        }
    ]).set_index("id")
# END new_data


def test__find_changed_rows_calls_comparator_function(old_data: DataFrame, new_data: DataFrame):
    is_equal = track_has_been_called(Series.equals)

    next(find_changed_rows(old_data, new_data, is_equal))

    assert is_equal.has_been_called
# END test__find_changed_rows_calls_comparator_function


def test__find_changed_rows_finds_mutations(old_data: DataFrame, new_data: DataFrame):
    mutations = list(find_changed_rows(old_data, new_data, Series.equals))

    assert len(mutations) == 1
# END test__find_changed_rows_calls_comparator_function
