from config import confluent_kafka as config
from confluent_kafka import Producer
from credentials import confluent_kafka as credentials


def make_confluent_producer() -> Producer:
    """
    Returns a connection to Confluent Kafka in the Data Management Platform that can be used to push change events.
    """

    return Producer(**config, **credentials)
# END make_confluent_producer
