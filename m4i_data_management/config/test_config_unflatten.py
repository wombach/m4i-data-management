from .config_unflatten import *


def test_config_unflatten_keys():
    data = {'foo_0': 'val', 'foo_1': 'bar'}
    expected = {'foo_0': 'val', 'foo_1': 'bar'}
    result = config_unflatten(data)
    assert expected == result

def test_config_unflatten_list():
    data = {'foo__0': 'val', 'foo__1': 'bar'}
    expected = {'foo': ['val', 'bar']}
    result = config_unflatten(data)
    assert expected == result

def test_config_unflatten_nested():
    data = {'foo__bar': 'val'}
    expected = {'foo': {'bar': 'val'}}
    result = config_unflatten(data)
    assert expected == result

def test_config_unflatten_list_list():
    data = {'foo__0__0': 'val'}
    expected = {'foo': [['val']]}
    result = config_unflatten(data)
    assert expected == result

def test_config_unflatten_complex():
    data = {'foo__0__bar': 'val', 'foo__1__baz': 'x'}
    expected = {'foo': [{'bar': 'val'}, {'baz': 'x'}]}
    result = config_unflatten(data)
    assert expected == result
