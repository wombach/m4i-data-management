from pandas import Series
from .get_properties import get_properties
from vox_data_management import ConfigStore

store = ConfigStore.get_instance()

def test__get_properties():
    wanted_properties = {"property_keys": ["a", "b"]}
    store.load({**wanted_properties})
    data = Series({"a": "a_old", "b": "b_old", "c": "old_c"})
    prop = get_properties(data)
    assert isinstance(prop, Series)
    assert "properties" in prop
    assert "a" in prop['properties']
    assert "b" in prop['properties']
    assert "c" not in prop['properties']
# END test__get_properties

def test__get_properties_none():
    wanted_properties = {"property_keys": []}
    store.load({**wanted_properties})
    data = Series({"a": "a_old", "b": "b_old", "c": "old_c"})
    prop = get_properties(data)
    assert isinstance(prop, Series)
    assert "properties" in prop
    assert prop['properties'] == {}

# END test__get_properties_none


