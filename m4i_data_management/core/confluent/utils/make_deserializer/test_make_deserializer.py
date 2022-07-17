import pytest
from confluent_kafka.schema_registry import SchemaRegistryError
from .....config import ConfigStore
from .make_deserializer import UnspecifiedSchemaException, make_deserializer
"""

to run these tests add config to the Store

config= {
    "confluent_schema_registry_url":    YOUR URL,
    "confluent_schema_registry_key":  KEY,
    "confluent_schema_registry_secret": SECRET
    }
store = ConfigStore.get_instance()
store.load(config)
"""


def test__make_avro_deserializer_for_value_schema_from_schema_name():

    schema_name = "ebs--public--fte-v2--transient-value"

    deserializer = make_deserializer(schema_name=schema_name, schema_type="avro")

    assert deserializer._reader_schema['name'] == 'com.vanoord.nxtgen.dev.ebs__public__fte__transient__value'
# END test__make_avro_deserializer_for_value_schema_from_schema_name


def test__make_avro_deserializer_for_key_schema():
    schema_id = "100008"

    deserializer = make_deserializer(schema_id=schema_id, schema_type="avro")

    assert deserializer._reader_schema == 'string'
# END test__make_avro_deserializer


def test__make_avro_deserializer_for_value_schema():
    schema_id = "100065"

    deserializer = make_deserializer(schema_id=schema_id, schema_type="avro")

    assert deserializer._reader_schema['name'] == 'avro.test.value'
# END test__make_avro_deserializer


def test__make_avro_deserializer_for_non_existing_schema():
    schema_name = "non_existing"

    with pytest.raises(SchemaRegistryError):
        make_deserializer(schema_name=schema_name, schema_type="avro")
    # END WITH
# END test__make_avro_deserializer


def test__make_avro_deserializer_without_specified_schema():
    with pytest.raises(UnspecifiedSchemaException):
        make_deserializer(schema_type="avro")
    # END WITH
# END test__make_avro_deserializer
