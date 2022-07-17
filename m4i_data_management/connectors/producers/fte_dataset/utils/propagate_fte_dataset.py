from config import fte_dataset_index, fte_dataset_kafka_topic
from pandas import DataFrame
from vox_data_management import format_change_events, propagate_change_events

from ..constants import FTE_DATASET_PRODUCER_NAME, INDEX_COL

def propagate_fte_dataset(changes: DataFrame):

    change_events = format_change_events(
        events=changes,
        event_index_name=INDEX_COL,
        source_name=FTE_DATASET_PRODUCER_NAME,
        target_index_name=fte_dataset_index
    )

    propagate_change_events(
        changes=change_events,
        topic_name=fte_dataset_kafka_topic,
    )
# END propagate_fte_dataset
