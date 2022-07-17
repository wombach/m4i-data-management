import cx_Oracle
from config import fte_dataset_db as db_config
from credentials import fte_dataset as credentials

def make_ebs_connection() -> cx_Oracle.Connection:

    dsn = cx_Oracle.makedsn(
        **db_config
    )

    connection = cx_Oracle.connect(
        **credentials,
        dsn=dsn
    )

    return connection
# END make_ebs_connection
