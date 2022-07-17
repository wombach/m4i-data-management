from confluent_kafka import Producer

from .....config import ConfigStore

config = ConfigStore.get_instance()


def make_confluent_producer() -> Producer:
    """
    Returns a connection to Confluent Kafka in the Data Management Platform that can be used to push change events.
    """

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
        "security.protocol": "SASL_SSL"
    }

    return Producer(**producer_config)
# END make_confluent_producer
