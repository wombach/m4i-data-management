from confluent_kafka import Consumer

from .....config import ConfigStore

config = ConfigStore.get_instance()


def make_confluent_consumer(enable_auto_commit: bool = True) -> Consumer:
    bootstrap_server_url, group_id, username, password = config.get_many(
        "confluent_kafka_bootstrap_servers",
        "confluent_kafka_group_id",
        "confluent_auth_sasl_username",
        "confluent_auth_sasl_password",
        required={
            "confluent_kafka_bootstrap_servers": True,
            "confluent_kafka_group_id": True,
            "confluent_auth_sasl_username": True,
            "confluent_auth_sasl_password": True
        }
    )

    consumer_config = {
        "auto.offset.reset": "earliest",
        "bootstrap.servers": bootstrap_server_url,
        "enable.auto.commit": enable_auto_commit,
        "group.id": group_id,
        "sasl.mechanisms": "PLAIN",
        "sasl.password": password,
        "sasl.username": username,
        "security.protocol": "SASL_SSL"
    }

    return Consumer(consumer_config)
# END make_confluent_consumer
