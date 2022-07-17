from json import dumps

from pandas import Series

from .utils import make_confluent_producer


def propagate_change_events(changes: Series, topic_name: str):
    """
    Propagates the given `changes` to the Confluent Kafka topic with the given `topic_name`.
    """

    producer = make_confluent_producer()

    for index, change in changes.iteritems():
        message = dumps(change)
        producer.produce(topic_name, key=str(index), value=message)
    # END LOOP

    producer.flush()
# END propagate_fte_dataset
