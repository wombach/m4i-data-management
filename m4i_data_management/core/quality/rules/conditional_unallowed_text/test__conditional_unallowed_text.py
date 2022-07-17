from numpy import NaN
from pandas import DataFrame

from .conditional_unallowed_text import conditional_unallowed_text


def test__conditional_unallowed_text_condition_met_with_allowed_value():

    values = ['.TMP', '.FREE']

    unallowed_text_item = "("

    data = DataFrame([
        {
            "value": "Something",
            "conditional": "xx.FREE.eur"
        }
    ])

    result = conditional_unallowed_text(data, "conditional", "value", values, unallowed_text_item)

    assert result.sum() == 1
# END test__conditional_unallowed_text_condition_met_with_allowed_value

def test__conditional_unallowed_text_condition_met_with_unallowed_value():

    values = ['.TMP', '.FREE']

    unallowed_text_item = "(1)"

    data = DataFrame([
        {
            "value": "Something(1)",
            "conditional": "xx.FREE.eur"
        }
    ])

    result = conditional_unallowed_text(data, "conditional", "value", values, unallowed_text_item)

    assert result.sum() == 0
# END test__conditional_unallowed_text_condition_met_with_unallowed_value

def test__conditional_unallowed_text_condition_met_without_value():

    values = ['.TMP', '.FREE']

    unallowed_text_item = "(1)"

    data = DataFrame([
        {
            "value": NaN,
            "conditional": "xx.FREE.eur"
        }
    ])

    result = conditional_unallowed_text(data, "conditional", "value", values, unallowed_text_item)

    assert result.sum() == 1
# END test__conditional_unallowed_text_condition_met_without_value



def test__conditional_unallowed_text_condition_no_data():
    values = ['.TMP', '.FREE']

    unallowed_text_item = "(1)"

    data = DataFrame([
        {
            "value": NaN,
            "conditional": NaN
        }
    ])
    result = conditional_unallowed_text(data, "conditional", "value", values, unallowed_text_item)
    assert sum(result) == 0


# END test__conditional_unallowed_text_condition_no_data


def test__conditional_unallowed_text_condition_no_conditonal():
    values = ['.TMP', '.FREE']

    unallowed_text_item = "(1)"

    data = DataFrame([
        {
            "value": "something()",
            "conditional": NaN
        }
    ])
    result = conditional_unallowed_text(data, "conditional", "value", values, unallowed_text_item)
    assert sum(result) == 0
# END test__conditional_unallowed_text_condition_no_conditonal

def test__conditional_unallowed_text_condition_collection():
    values = ['.TMP', '.FREE']

    unallowed_text_item = "(1)"

    data = DataFrame([
        {
            "value": "something()",
            "conditional": NaN
        },
        {
            "value": "something(1)",
            "conditional": NaN
        },
        {
            "value": "something()",
            "conditional": "xx.FREE.eur"
        },
        {
            "value": "something(1)",
            "conditional": "xx.FREE.eur"
        }
    ])
    result = conditional_unallowed_text(data, "conditional", "value", values, unallowed_text_item)
    assert sum(result) == 1
# END test__conditional_unallowed_text_condition_collection
