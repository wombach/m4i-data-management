import pytest
from pandas import Series
from m4i_data_management import ConfigStore
from .get_auth import get_auth

store = ConfigStore.get_instance()


def test__get_auth():
    config_check = {
        "auth_fields": "a"
    }
    store.load({**config_check})
    data = Series({
        "a": "a_value",
        "b": "b_value"
    })
    result = get_auth(data, data)
    expected = Series({
        "auth": {
            "a_auth": ["a_value", "a_value"]
        }
    })
    assert (result == expected).all()
# END test__get_auth

def test__get_auth_field_missing():
    config_check = {
        "auth_fields": "c"
    }
    store.load({**config_check})
    data = Series({
        "a": "a_value",
        "b": "b_value"
    })
    with pytest.raises(KeyError) as e:
        assert get_auth(data, data) == e
# END test__get_auth_field_missing
