
from config import fte_dataset_index as elastic_index
from pandas import DataFrame
from vox_data_management.core.elastic import retrieve_elastic_data as get_data

from ..constants import INDEX_COL

def retrieve_elastic_data() -> DataFrame:

    data = (
        get_data(index_name=elastic_index)
        .pipe(DataFrame.set_index, keys=INDEX_COL)
    )

    return data
# END retrieve_elastic_data
