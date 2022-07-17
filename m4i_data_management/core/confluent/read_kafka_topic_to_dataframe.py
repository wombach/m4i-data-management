from pandas import DataFrame
from . import read_messages_from_topic, make_deserializing_consumer


def read_kafka_topic_to_dataframe(source_topic: str, timeout: int = 30) -> DataFrame:
    """
    Read Kafka Topic, remove empty messages and create a dataframe with the messages from the topic and index as the doc ID.
    :param source_topic: The name of the source topic to read from
    :param timeout:
    :return:
        A data frame containing the messages in the topic, with the index as the doc id in the message
    """

    consumer = make_deserializing_consumer(
        topic_name=source_topic,
        value_schema_type="avro",
        enable_auto_commit=False
    )

    messages = read_messages_from_topic(
        source_topic,
        consumer=consumer,
        timeout=timeout
    )

    # Filter empty messages since these will mess up the dataframe
    messages_not_empty = (
        (key, value)
        for key, value in messages
        if value is not None
    )

    try:
        keys, values = zip(*messages_not_empty)
        data = DataFrame(data=values, index=keys)

    except ValueError:
        data = DataFrame(data=messages_not_empty)

    return data
