from .config_store import ConfigStore, MissingRequiredConfigException
import pytest

@pytest.fixture()
def get_store():
    store = ConfigStore.get_instance()
    config = {
        "value_1": "one",
        "value_2": "two"
    }
    store.load(config)


def test_config_get(get_store):
    store = ConfigStore.get_instance()
    assert store.get('value_1') == "one"
    assert store.get('value_2', required=False) == "two"
# END test_config_get

def test_config_get_None(get_store):
    store = ConfigStore.get_instance()
    assert store.get('value_3') is None
# END test_config_get_None

def test_config_get_Required_no_default(get_store):
    store = ConfigStore.get_instance()
    with pytest.raises(MissingRequiredConfigException):
        store.get('value_3', required=True)
    # END WITH
# END test_config_get_Required_no_default

def test_config_get_Required_with_default(get_store):
    store = ConfigStore.get_instance()
    assert store.get('value_3', default="three", required=True) == "three"
# END test_config_get_Required_with_default

def test_config_get_many(get_store):
    store = ConfigStore.get_instance()
    a, b, c = store.get_many('value_1', 'value_2', 'value_3')
    assert a == "one"
    assert b == "two"
    assert c is None
# END test_config_get_many


def test_config_get_many_Required_no_default(get_store):
    store = ConfigStore.get_instance()
    with pytest.raises(MissingRequiredConfigException):
        a, b = store.get_many('value_1', 'value_3', required={'value_3':True})
    # END WITH
# END test_config_get_many_Required_no_default

def test_config_get_many_Required_existing(get_store):
    store = ConfigStore.get_instance()
    a, b = store.get_many('value_1', 'value_3', required={'value_1':True})
    assert a == "one"
    assert b is None
# END test_config_get_many_Required_no_default

def test_config_get_many_Required_with_default(get_store):
    store = ConfigStore.get_instance()
    a, b = store.get_many('value_1', 'value_3', defaults={'value_3':'three'}, required={'value_3':True})
    assert a == 'one'
    assert b == 'three'
# END test_config_get_many_Required_with_default


def test_config_get_many_all_required_no_default(get_store):
    store = ConfigStore.get_instance()
    with pytest.raises(MissingRequiredConfigException):
        a, b = store.get_many('value_1', 'value_3', all_required=True)
    # END WITH
# END test_config_get_many_all_required_no_default

def test_config_get_many_all_Required_with_default(get_store):
    store = ConfigStore.get_instance()
    a, b = store.get_many('value_1', 'value_3', defaults={'value_3':'three'}, all_required=True)
    assert a == 'one'
    assert b == 'three'
# END test_config_get_many_all_Required_with_default

def test_config_get_many_all_required(get_store):
    store = ConfigStore.get_instance()
    a, b = store.get_many('value_1', 'value_2', all_required=True)
    assert a == "one"
    assert b == "two"
# END test_config_get_many_all_required
