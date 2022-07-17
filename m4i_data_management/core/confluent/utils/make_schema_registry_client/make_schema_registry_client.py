from confluent_kafka.schema_registry import SchemaRegistryClient

from .....config import ConfigStore

config = ConfigStore.get_instance()


def make_schema_registry_client() -> SchemaRegistryClient:
    """
    Returns a connection to Confluent Kafka Schema Registry in the Data Management Platform that can be used to define and retrieve schema definitions.
    """

    url, key, secret = config.get_many(
        "confluent_schema_registry_url",
        "confluent_schema_registry_key",
        "confluent_schema_registry_secret",
        required={
            "confluent_schema_registry_url": True,
            "confluent_schema_registry_key": True,
            "confluent_schema_registry_secret": True
        }
    )

    basic_auth = f"{key}:{secret}"

    schema_registry_config = {
        "url": url,
        "basic.auth.user.info": basic_auth
    }

    return SchemaRegistryClient(schema_registry_config)
# END make_schema_registry_client
