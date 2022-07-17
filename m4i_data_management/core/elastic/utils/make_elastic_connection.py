from elasticsearch import Elasticsearch

from ....config import ConfigStore

config = ConfigStore.get_instance()


def make_elastic_connection() -> Elasticsearch:
    """
    Returns a connection with the ElasticSearch database in the Data Management Platform
    """

    cloud_id, username, password = config.get_many(
        "elastic_cloud_id",
        "elastic_cloud_username",
        "elastic_cloud_password",
        all_required=True
    )

    connection_config = {
        "cloud_id": cloud_id,
        "basic_auth": (
            username,
            password
        )
    }

    connection = Elasticsearch(
        **connection_config
    )

    return connection
# END make_elastic_connection
