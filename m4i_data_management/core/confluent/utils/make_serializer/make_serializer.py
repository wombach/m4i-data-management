from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.schema_registry.json_schema import JSONSerializer
from confluent_kafka.serialization import (SerializationContext,
                                           StringSerializer)

from ..make_schema_registry_client import make_schema_registry_client


class UnspecifiedSchemaException(Exception):
    """
    Raised when neither a schema id or schema name are specified
    """
# END UnspecifiedSchemaException


def make_serializer(
    schema_id: str = None,
    schema_name: str = None,
    schema_type: str = "string",
    schema_registry_client: SchemaRegistryClient = None,
    to_dict=None,
    conf=None
) -> SerializationContext:
    """
    Makes a serializer for the given `schema_type`.
    When serializing to `json` or `avro`, a `schema_id` or `schema_name` must be passed.

    When passing a `schema_name`, the latest version of that schema is used.

    When serializing to `json`or `avro`, and no `schema_id` or `schema_name` are given, raises an `UnspecifiedSchemaException`.
    """

    if schema_type == "string":
        return StringSerializer("utf-8")
    # END IF

    if schema_registry_client is None:
        schema_registry_client = make_schema_registry_client()
    # END IF

    if schema_id is not None:
        schema = schema_registry_client.get_schema(schema_id)
    elif schema_name is not None:
        registered_schema = schema_registry_client.get_latest_version(schema_name)
        schema = registered_schema.schema
    else:
        raise UnspecifiedSchemaException(
            "Please specify either a schema id or a schema name."
        )
    # END IF

    serializers = {
        "avro": lambda: AvroSerializer(
            schema_str=schema.schema_str,
            schema_registry_client=schema_registry_client,
            to_dict=to_dict,
            conf=conf
        ),
        "json": lambda: JSONSerializer(
            schema_str=schema.schema_str,
            schema_registry_client=schema_registry_client,
            to_dict=to_dict,
            conf=conf
        ),
        "string": lambda: StringSerializer("utf-8")
    }

    serializer_factory = serializers.get(schema_type, serializers["string"])

    return serializer_factory()
# END make_serializer
