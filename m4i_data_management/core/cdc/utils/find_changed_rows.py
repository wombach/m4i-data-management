from typing import Callable, Iterable

from pandas import DataFrame, Series


def find_changed_rows(
    old: DataFrame,
    new: DataFrame,
    is_equal: Callable[[Series, Series], bool]
) -> Iterable[Series]:

    for index, new_row in new.iterrows():

        if index not in old.index:
            continue
        # END IF

        old_row = old.loc[index, :]

        are_rows_equal = is_equal(old_row, new_row)

        if not are_rows_equal:
            yield new_row
        # END IF
    # END LOOP
# END find_changed_rows
