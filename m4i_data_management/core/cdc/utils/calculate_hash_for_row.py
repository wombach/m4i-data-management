from dict_hash import dict_hash
from pandas import Series


def calculate_hash_for_row(row: Series) -> str:
    row_dict = row.dropna().to_dict()
    row_hash = dict_hash(row_dict)
    return str(row_hash)
# END calculate_hash_for_row
