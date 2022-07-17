from pandas import Series

from .get_row_mutations import get_row_mutations


def test__get_row_mutations_change():
    old_row = {"a": "a_old", "b": "b_old"}
    new_row = {"a": "a_old", "b": "b_new"}
    diff = get_row_mutations(Series(old_row), Series(new_row))
    assert len(diff["mutationsList"]) == 1
    assert diff["mutationsList"][0]["changed_column"] == "b"
    assert diff["mutationsList"][0]["new_value"] == "b_new"
    assert diff["mutationsList"][0]["old_value"] == "b_old"
# END test__compare_row_mutations_change

def test__get_row_mutations_same():
    old_row = {"a": "a_old", "b": "b_old"}
    new_row = {"a": "a_old", "b": "b_old"}
    diff = get_row_mutations(Series(old_row), Series(new_row))
    assert len(diff["mutationsList"]) == 0
# END test__compare_row_mutations_same

