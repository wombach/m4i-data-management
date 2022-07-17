import logging
from typing import Callable, Iterable

from pandas import DataFrame, Series

log = logging.getLogger(__name__)


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

        # In case of duplicate index, take the first entry
        if isinstance(old_row, DataFrame):
            log.warning(f"Found multiple old records for index {index}, picking the first occurrance from the old data")
            old_row = old_row.iloc[0]
        # END IF

        are_rows_equal = is_equal(old_row, new_row)

        if not are_rows_equal:
            yield new_row
        # END IF
    # END LOOP
# END find_changed_rows
