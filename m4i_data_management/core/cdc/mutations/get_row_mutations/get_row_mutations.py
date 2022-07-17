from deepdiff import DeepDiff
import re

from pandas import Series


def get_row_mutations(old_row: Series, new_row: Series) -> Series:
    """
    Compare 2 rows and returns mutationsList of the differences with the changed column,
    old value and new value for each difference. This is now considered the "mutations"

    :param old_row: The old row as a Pandas Series
    :param new_row: The new row as a Pandas Series
    :return: a Pandas Series with ket mutationList and value list of the difference
    with the changed column, old value and new value for each difference.
    """
    mutations_list = []

    diff = DeepDiff(old_row.to_dict(), new_row.to_dict())

    if "values_changed" in diff:
        # Reformat into our desired Shape with values_changed.
        for key in diff["values_changed"]:
            change = diff["values_changed"][key]
            mutation = {}
            mutation["new_value"] = str(change["new_value"])
            mutation["old_value"] = str(change["old_value"])
            mutation["changed_column"] = re.findall(r"\'(.*?)\'", key)[0]
            mutations_list.append(mutation)

    return Series({"mutationsList": mutations_list})
