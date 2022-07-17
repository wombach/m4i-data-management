
from config import fte_dataset_index
from pandas import DataFrame
from vox_data_management import format_change_events

from ..constants import INDEX_COL, TEST_PRODUCER_NAME

OUT_PATH = "out\\fte_dataset_test.csv"


def propagate_fte_dataset(changes: DataFrame):
    change_events = format_change_events(
        events=changes,
        event_index_name=INDEX_COL,
        source_name=TEST_PRODUCER_NAME,
        target_index_name=fte_dataset_index
    )

    change_events.to_csv(OUT_PATH)
# END propagate_fte_dataset
