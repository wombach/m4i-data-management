from pandas import Series
from .....config import ConfigStore


def get_properties(new_row: Series) -> Series:
    """
    Get the properties that would like to be recorded to help identify the data row.
    This requires in a variable in the config called "property_keys"
    which should be a list of the column names desired to be in properties.

    new_row: Row to get the properties from as a Series

    Returns: a Series containing a dictionary of the property keys with their value from the row.
    """
    store = ConfigStore.get_instance()
    property_keys = store.get("property_keys")
    props = new_row[property_keys].to_dict()
    return Series({"properties": props})
