from config import fte_dataset_table as table_config
from pandas import DataFrame

from ..constants import INDEX_COL
from .make_ebs_connection import make_ebs_connection

QUERY = (
    f"""
    SELECT * 
    FROM {table_config}
    """
)


def parse_effective_date(data: DataFrame) -> DataFrame:
    date_ms = data['EFFECTIVE_DATE'].astype('int64') / 1e6
    data['EFFECTIVE_DATE'] = date_ms
    return data
# END parse_effective_date


def retrieve_fte_data() -> DataFrame:

    connection = make_ebs_connection()

    try:
        cursor = connection.cursor()
        cursor.execute(QUERY)

        columns = [row[0] for row in cursor.description]

        data = (
            DataFrame(cursor, columns=columns)
            .pipe(DataFrame.set_index, keys=INDEX_COL)
            .pipe(parse_effective_date)
        )
    finally:
        connection.close()
    # END TRY

    return data
# END retrieve_fte_data
