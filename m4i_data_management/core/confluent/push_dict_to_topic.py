from . import produce_message, SerializingProducer

def push_dict_to_topic(destination_topic: str, index: str, row_value: dict, producer: SerializingProducer, flush: bool =True):
    """
    Send a single message (the row value) to a kafka topic, with index provided
    :param destination_topic: The Topic name to push the message to
    :param row_value: The message that is to be sent to the kafka topic as a dict
    :param index: The index to set it to this will be the doc id as a string
    :param flush: A boolean default True where after the message is pushed to flush the producer. If multiple messages need to be pushed then it's possible to set this to False, however the producer.flush needs to still be called once all the messages are sent. Please remember then to add this.
    :return:
    produced message to kafka topic of given name
    """

    try:
        produce_message(
            producer=producer,
            topic_name=destination_topic,
            key=index,
            value=row_value)
    except BufferError:
        produce_message(
            producer=producer,
            topic_name=destination_topic,
            key=index,
            value=row_value,
            poll_duration=10
        )
    finally:
        if flush:
            producer.flush()
    # END TRY
