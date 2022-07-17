from pandas import DataFrame, read_excel

from ..constants import INDEX_COL

DATA_PATH = "data\\fte_dataset_test_new.xlsx"


def retrieve_new_data() -> DataFrame:

    data = (
        read_excel(DATA_PATH)
        .pipe(DataFrame.set_index, keys=INDEX_COL)
    )

    return data
# END retrieve_new_data
