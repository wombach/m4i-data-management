from confluent_kafka import SerializingProducer

from .....config import ConfigStore
from ..make_schema_registry_client import make_schema_registry_client
from ..make_serializer import make_serializer

config = ConfigStore.get_instance()


def make_serializing_producer(
    value_schema_id: str = None,
    value_schema_type: str = "string",
    key_schema_id: str = None,
    key_schema_type: str = "string",
    topic_name: str = None
) -> SerializingProducer:
    """
    Returns a serializing producer.

    You can specify the serialization format by passing `key_schema_type` and `value_schema_type` respectively.

    You can specify a schema by passing `key_schema_id` and `value_schema_id`.

    If no schema ids are given, the given `topic_name` is used to retrieve the latest version of the schema based on the default naming strategy.

    If no `key_schema_id` or `value_schema_id` are given, the default `StringSerializer` is used for the respective fields.
    """

    schema_registry_client = make_schema_registry_client()

    key_serializer = make_serializer(
        schema_id=key_schema_id,
        schema_type=key_schema_type,
        schema_registry_client=schema_registry_client,
        schema_name=f"{topic_name}-key"
    )

    value_serializer = make_serializer(
        schema_id=value_schema_id,
        schema_type=value_schema_type,
        schema_registry_client=schema_registry_client,
        schema_name=f"{topic_name}-value"
    )

    bootstrap_server_url, username, password = config.get_many(
        "confluent_kafka_bootstrap_servers",
        "confluent_auth_sasl_username",
        "confluent_auth_sasl_password",
        required={
            "confluent_kafka_bootstrap_servers": True,
            "confluent_auth_sasl_username": True,
            "confluent_auth_sasl_password": True
        }
    )

    producer_config = {
        "bootstrap.servers": bootstrap_server_url,
        "sasl.mechanisms": "PLAIN",
        "sasl.password": password,
        "sasl.username": username,
        "security.protocol": "SASL_SSL",
        "key.serializer": key_serializer,
        "value.serializer": value_serializer
    }

    return SerializingProducer(producer_config)
# END make_serializing_producer
