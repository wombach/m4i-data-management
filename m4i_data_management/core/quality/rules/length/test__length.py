from numpy import NaN
from pandas import DataFrame

from .length import length


def test__length_with_equal_length():

    data = DataFrame([
        {
            "id": 1234
        }
    ])

    result = length(data, "id", 4)

    assert result.sum() == 1
# END test__length_with_equal_length_single_value


def test__length_with_non_equal_length():

    data = DataFrame([
        {
            "id": 12345
        }
    ])

    result = length(data, "id", 4)

    assert result.sum() == 0
# END test__length_with_non_equal_length_single_value


def test__length_without_value():

    data = DataFrame([
        {
            "id": NaN
        }
    ])

    result = length(data, "id", 4)

    assert result.sum() == 1
# END test__length_without_value
