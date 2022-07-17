from pandas import Series
from .....config import ConfigStore




def get_auth(old_row: Series, new_row: Series) -> Series:
    """"
    Get parameters that are used in the authorization queries in elastic. This is used to simplify the query. 
    """
    store = ConfigStore.get_instance()
    auth_fields = store.get("auth_fields")
    auth = {}
    for field in auth_fields:
        field_auth_name = field + "_auth"
        auth.update({field_auth_name: [old_row[field], new_row[field]]})

    return Series({"auth": auth})
