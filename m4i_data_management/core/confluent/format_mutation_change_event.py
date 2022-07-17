from time import time
from uuid import uuid4 as uuid

from pandas import DataFrame, Series, notnull

from m4i_data_management.core.cdc import CDCChangeType

from ..cdc import CHANGE_TYPE_COLUMN
from ..utils import omit


def format_mutation_change_event(event: Series, source_name: str, target_index_name: str) -> dict:
    """
    Returns a standardized change event message based on the given change `event`.
    """

    id = str(uuid())
    change_type = event[CHANGE_TYPE_COLUMN].value
    mutationsList = event["mutationsList"]
    properties = event["properties"]
    auth = event["auth"]
    event = event.drop("mutationsList")
    event = event.drop("properties")
    event = event.drop("auth")
    timestamp = int(time())


    payload = None

    if event[CHANGE_TYPE_COLUMN] != CDCChangeType.REMOVED:
        # Convert the event to a dict. Replaces `nan` values with `None`.
        event_dict = event.where(notnull(event), None).to_dict()

        payload = omit(
            event_dict,
            CHANGE_TYPE_COLUMN
        )
    # END IF

    message = {
        "id": id,
        "change_type": change_type,
        "source": source_name,
        "target": target_index_name,
        "timestamp": timestamp,
        "mutationsList": mutationsList,
        "properties": properties,
        "auth": auth,
        "payload": payload
    }

    return message


# END format_mutation_change_event


def format_mutation_change_events(events: DataFrame, source_name: str, target_index_name: str) -> Series:
    """
    Returns a Series of all given change events as standardized change event messages.
    """

    return events.apply(
        format_mutation_change_event,
        axis=1,
        source_name=source_name,
        target_index_name=target_index_name
    )
# END format_mutation_change_events
