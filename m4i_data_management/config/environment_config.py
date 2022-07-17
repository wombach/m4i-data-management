import os
from .config_store import ConfigStore
from .config_unflatten import config_unflatten
from dotenv import dotenv_values


def lookup_env(prefix: str) -> dict:
    """
    Lookup the environment variables, take key, values for keys that start with the prefix assigned.
    :param prefix: The prefix of the keys to take
    :return: A dictionary of the key,value environment variables that start with the prefix
    """
    config = {}
    for k, v in os.environ.items():
        if k.startswith(prefix):
            config.update({k: v})
    return config
# END lookup_env

def remove_prefix(config: dict, prefix: str) -> dict:
    """
    Remove the given prefix from keys inside of the given config dictionary
    :param config: The Dictionary to check
    :param prefix: The prefix to look for and remove
    :return: The dictionary where the given prefix are removed from the keys, if the prefix was there.
    """
    config_no_prefix = {}
    for k, v in config.items():
        if k.startswith(prefix):
            new_k = k[len(prefix):]
            config_no_prefix.update({new_k: v})
        else:
            config_no_prefix.update({k: v})
    return config_no_prefix
# END remove_prefix

def load_config_from_env(filename:str= 'config_env', prefix:str= 'config_'):
    """
    Get the configuration from a local file (config_env) if available, else take the configuration from environment variables.
    :param filename:
    :param prefix:
    :return:
    """
    # Load the config
    store = ConfigStore.get_instance()
    config = {}

    # Look for config in local file
    if os.path.exists(filename):
        config = dotenv_values(filename)

    # Look for config in Environment Variables with prefix
    if config == {}:
        config = lookup_env(prefix)

    # unflattening environment variables, making lists and dicts if needed
    config = config_unflatten(config)

    # Remove Prefix
    config_list = remove_prefix(config, prefix)
    store.load(config_list)
