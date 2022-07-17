from .environment_config import remove_prefix, load_config_from_env
from .config_store import ConfigStore


def test_remove_prefix():
    config = {
        "prefix_value_1": "one",
        "value_2": "two"
    }
    prefix = 'prefix_'
    expected = {
        "value_1": "one",
        "value_2": "two"
    }
    result = remove_prefix(config, prefix)
    assert expected == result


# END test_remove_prefix

def test_load_config_from_env_local_file():
    path = "config/config_env_test"

    load_config_from_env(filename=path)

    store = ConfigStore.get_instance()
    assert store.get("value_1", required=True) == 'one'
    assert store.get("value_2", required=True) == 'two'
    assert store.get("value_3", required=True) == ['list_item_one', 'list_item_two']
    assert store.get("value_4", required=True) == {'value_5': 'four_five_dict'}
# END test_load_config_from_env_local_file
