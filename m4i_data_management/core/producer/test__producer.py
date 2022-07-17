import pytest
from pandas import DataFrame
from vox_data_management.test import assert_has_method_been_called

from .producer import Producer


def get_new():
    return DataFrame({"id": [1], "abc": ["def"], "ghi": ["jkl"]}).set_index("id")
# END get_new


def get_old():
    return DataFrame({"id": [1], "abc": ["def"], "ghi": ["mno"]}).set_index("id")
# END get_old


def transform(data: DataFrame):
    data["abc"] = "test"
    return data
# END transform


def propagate(data: DataFrame):
    pass
# END _propagate


@pytest.fixture
def producer():
    return Producer(
        get_new=get_new,
        get_old=get_old,
        propagate=propagate
    )
# END producer


@pytest.fixture
def producer_transform():
    return Producer(
        get_new=get_new,
        get_old=get_old,
        transform=transform,
        propagate=propagate
    )
# END producer_transform


def test__producer_calls_workflow_steps(producer: Producer):
    with assert_has_method_been_called(producer, "get_old"), assert_has_method_been_called(producer, "get_new"), assert_has_method_been_called(producer, "transform"), assert_has_method_been_called(producer, "propagate"):
        producer.run()
    # END WITH
# END test__producer_calls_workflow_steps


def test__producer_calls_custom_transform(producer_transform: Producer):
    with assert_has_method_been_called(producer_transform, "transform"):
        producer_transform.run()
    # END WITH
# END test__producer_calls_custom_transform
